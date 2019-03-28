#!/usr/bin/env python
# encoding: utf-8
"""
@version: python2.7
@author: ‘eric‘
@license: Apache Licence 
@contact: steinven@qq.com
@site: 00123.ml:8000
@software: PyCharm
@file: escience.py
@time: 18/4/24 下午2:41
"""
import os
import sys
from contextlib import closing
from urllib.parse import unquote

import click
import configparser
import json
import requests
from prettytable import PrettyTable

from utiles.logger import logger
from utiles.process_bar import ProgressBar

requests.packages.urllib3.disable_warnings()
conf = configparser.ConfigParser()
conf.read('conf.cfg')
userName = conf.get('user_info', 'userName')
passwd = conf.get('user_info', 'passwd')
download_dir = conf.get('file', 'download_path')


# global_params保存每次请求的返回参数

class escience:
    def __init__(self, userName, passwd):
        self.userName = userName
        self.passwd = passwd
        self.session = requests.session()
        self.header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Connection': 'keep-alive',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'Host': 'ddl.escience.cn',
                   'Origin': 'http://ddl.escience.cn',
                   'Referer': 'http://ddl.escience.cn/pan/list',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) '
                                 'AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 '
                                 'Safari/7046A194A',
                   'X-Requested-With': 'XMLHttpRequest'}

    def oauth_page(self):
        url = 'https://passport.escience.cn/oauth2/authorize?response_type=code&redirect_uri=' \
              'http://ddl.escience.cn/system/login/token&client_id=87143&theme=full&state=' \
              'http://ddl.escience.cn/pan/list'
        self.session.get(url, headers=self.header, verify=False)

    def oauth(self):
        url = 'https://passport.escience.cn/oauth2/authorize'
        data = {'clientId': '87142',
                'clientName': '团队文档库',
                'pageinfo': 'checkPassword',
                'password': '%s' % self.passwd,
                'userName': '%s' % self.userName}
        r = self.session.post(url, headers=self.header, verify=False, data=data)
        if 'true' not in r.text:
            logger().error('登录失败！请在配置文件填写正确的账号和密码')
            sys.exit(0)

    def oauth_again(self):
        url = 'https://passport.escience.cn/oauth2/authorize?client_id=87142&redirect_uri=http://' \
              'ddl.escience.cn/system/login/token&response_type=code&state=http://ddl.escience.cn/pan/list&theme=full'
        data = {'act': 'Validate',
                'pageinfo': 'userinfo',
                'password': '%s' % passwd,
                'theme': 'full',
                'userName': '%s' % userName}
        r = self.session.post(url, headers=self.header, data=data, verify=False, allow_redirects=False)
        r_location = r.headers['Location']
        return r_location

    def location(self):
        location_url = self.oauth_again()
        self.session.post(url=location_url, headers=self.header, allow_redirects=False)

    def list_file(self, search_keyword):
        url = 'http://ddl.escience.cn/pan/list?func=query'
        data = {

            'path': '',
            'sortType': '',
            'tokenKey': '1524672146487',
            'keyWord': '%s' % search_keyword,

        }

        r = self.session.post(url=url, headers=self.header, data=data, allow_redirects=False)
        r_dict = json.loads(r.text)['children']  # 搜索到的结果集
        d = [i for i in r_dict if i['itemType'] != 'Folder']
        x = PrettyTable()
        x.field_names = ["ID", "FileName", "CreateTime", "Size"]

        m = 0  # 文件ID
        id_file_dict = {}
        global_params = {}
        for i in d:
            x.add_row([m, i['fileName'], i['modofyTime'], i['size']])
            id_file_dict.update({m: i['rid']})
            m += 1
        global_params.update({'id_file_dict': id_file_dict})
        global_params.update({'table_list': x})
        return global_params


@click.command()
@click.option('-d', default=0, help='Download Files By Index Number')
@click.option('-s', default='', help='Search Files')
def get_file(**options):
    e = escience(userName, passwd)
    e.oauth_page()
    e.oauth()
    e.oauth_again()
    e.location()
    search_keyord = options['s']
    download_id = options['d']
    global_params = e.list_file(search_keyord)
    if search_keyord != '':
        conf.set('user_info', 'search_keyord', search_keyord)
        conf.write(open("conf.cfg", "w"))
        e.list_file(search_keyord)
        print(global_params['table_list'])
        return
    search_keyord = conf.get('user_info', 'search_keyord')
    global_params = e.list_file(search_keyord)
    id_file_dict = global_params['id_file_dict']
    logger().info('id_file_dict:'+str(id_file_dict))
    try:
        file_path = id_file_dict[download_id]
    except KeyError:
        logger().error("ID对应文件不存在，请检查，或重新搜索！")
        sys.exit(0)

    url = 'http://ddl.escience.cn/pan/download?path=%s' % file_path

    with closing(e.session.get(url, headers=e.header, verify=False, stream=True)) as response:
        chunk_size = 1024  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 内容体总大小
        file_name = '%s' % unquote(file_path.split('%2F')[-1])
        progress = ProgressBar(file_name, total=content_size,
                               unit="KB", chunk_size=chunk_size, run_status="正在下载", fin_status="下载完成")
        with open(os.path.join(download_dir, file_name), "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                progress.refresh(count=len(data))

        file.close()
        print('文件下载路径[%s]' % download_dir)


if __name__ == '__main__':
    get_file()
