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
from contextlib import closing

import click
import requests, configparser, json
from prettytable import PrettyTable
from urllib.parse import unquote

requests.packages.urllib3.disable_warnings()
conf = configparser.ConfigParser()
conf.read('conf.cfg')
userName = conf.get('user_info', 'userName')
passwd = conf.get('user_info', 'passwd')
# global_params保存每次请求的返回参数
global_params = {}


# 请求登录界面
def oauth_page():
    '''
    client_id暂不知其作用
    :return: cookieJar
    '''
    url = 'https://passport.escience.cn/oauth2/authorize?response_type=code&redirect_uri=' \
          'http://ddl.escience.cn/system/login/token&client_id=87143&theme=full&state=' \
          'http://ddl.escience.cn/pan/list'
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Host': 'passport.escience.cn',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    global_params.update({'cookies': requests.get(url, headers=headers, verify=False).cookies})
    return global_params


# 身份认证
def oauth():
    global_params = oauth_page()
    cookies = global_params['cookies']
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Content-Length': '140',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Host': 'passport.escience.cn',
               'Origin': 'https://passport.escience.cn',
               'Referer': 'https://passport.escience.cn/oauth2/authorize?response_type=code&redirect_uri=http://ddl.escience.cn/system/login/token&client_id=87142&theme=full&state=http://ddl.escience.cn/pan/list',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest'}
    url = 'https://passport.escience.cn/oauth2/authorize'
    data = {'clientId': '87142',
            'clientName': '团队文档库',
            'pageinfo': 'checkPassword',
            'password': '%s' % passwd,
            'userName': '%s' % userName}
    requests.post(url, headers=headers, cookies=cookies, verify=False, data=data)
    return global_params


# 再次认证身份
def oauth_again():
    global_params = oauth()
    cookies = global_params['cookies']
    url = 'https://passport.escience.cn/oauth2/authorize?client_id=87142&redirect_uri=http://' \
          'ddl.escience.cn/system/login/token&response_type=code&state=http://ddl.escience.cn/pan/list&theme=full'
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'Content-Length': '87',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Host': 'passport.escience.cn',
               'Origin': 'https://passport.escience.cn',
               'Referer': 'https://passport.escience.cn/oauth2/authorize?response_type=code&redirect_uri=http://ddl.escience.cn/system/login/token&client_id=87142&theme=full&state=http://ddl.escience.cn/pan/list',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    data = {'act': 'Validate',
            'pageinfo': 'userinfo',
            'password': '%s' % passwd,
            'theme': 'full',
            'userName': '%s' % userName}
    r = requests.post(url, headers=headers, data=data, verify=False, cookies=cookies, allow_redirects=False)
    r_location = r.headers['Location']
    global_params.update({'url_location': r_location})
    return global_params


# 访问重定向地址
def location():
    global_params = oauth_again()
    location_url = global_params['url_location']
    cookies = global_params['cookies']
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'Host': 'ddl.escience.cn',
               'Origin': 'https://passport.escience.cn',
               'Referer': 'https://passport.escience.cn/oauth2/authorize?response_type=code&redirect_uri=http://ddl.escience.cn/system/login/token&client_id=87142&theme=full&state=http://ddl.escience.cn/pan/list',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    r = requests.get(url=location_url, headers=headers, cookies=cookies, allow_redirects=False)
    global_params.update({'cookies': r.cookies})
    return global_params


# 获取搜索文件的路径，供下载文件使用
def list_file(search_keyord):
    global_params = location()
    cookies = global_params['cookies']
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Content-Length': '47',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Host': 'ddl.escience.cn',
               'Origin': 'http://ddl.escience.cn',
               'Referer': 'http://ddl.escience.cn/pan/list',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) '
                             'AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 '
                             'Safari/7046A194A',
               'X-Requested-With': 'XMLHttpRequest'}
    url = 'http://ddl.escience.cn/pan/list?func=query'
    data = {

        'path': '',
        'sortType': '',
        'tokenKey': '1524672146487',
        'keyWord': '%s' % search_keyord,

    }
    r = requests.post(url=url, headers=headers, cookies=cookies, data=data, allow_redirects=False)

    r_dict = json.loads(r.text)['children']  # 搜索到的结果集
    d = [i for i in r_dict if i['itemType'] != 'Folder']
    x = PrettyTable()
    x.field_names = ["ID", "FileName", "CreateTime", "Size"]

    m = 0  # 文件ID
    id_file_dict = {}
    for i in d:
        x.add_row([m, i['fileName'], i['modofyTime'], i['size']])
        id_file_dict.update({m: i['rid']})
        m += 1
    global_params.update({'id_file_dict': id_file_dict})
    global_params.update({'cookies': cookies})
    global_params.update({'table_list': x})
    return global_params


class ProgressBar(object):

    def __init__(self, title,
                 count=0.0,
                 run_status=None,
                 fin_status=None,
                 total=100.0,
                 unit='', sep='/',
                 chunk_size=1.0):
        super(ProgressBar, self).__init__()
        self.info = "【%s】%s %.2f %s %s %.2f %s %.2f %s"
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or " " * len(self.status)
        self.unit = unit
        self.seq = sep

    def __get_info(self):
        # 【名称】状态 进度 单位 分割线 总数 单位
        _info = self.info % (self.title, self.status,
                             self.count / self.chunk_size, self.unit, self.seq, self.total / self.chunk_size, self.unit,
                             100 * (self.count / self.total), '%')
        return _info

    def refresh(self, count=1, status=None):
        self.count += count
        # if status is not None:
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = '\n'
            self.status = status or self.fin_status
        print(self.__get_info(), end=end_str)


@click.command()
@click.option('-d', default=0, help='Download Files By Index Number')
@click.option('-s', default='', help='Search Files')
def get_file(**options):
    search_keyord = options['s']
    download_id = options['d']
    if search_keyord != '':
        conf.set('user_info', 'search_keyord', search_keyord)
        conf.write(open("conf.cfg", "w"))
        list_file(search_keyord)
        print(global_params['table_list'])
        return
    search_keyord = conf.get('user_info', 'search_keyord')
    list_file(search_keyord)
    id_file_dict = global_params['id_file_dict']
    file_path = id_file_dict[download_id]
    cookies = global_params['cookies']

    url = 'http://ddl.escience.cn/pan/download?path=%s' % file_path
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Host': 'ddl.escience.cn',
               'Referer': 'http://ddl.escience.cn/pan/list',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

    with closing(requests.get(url, headers=headers, verify=False, cookies=cookies, stream=True)) as response:
        chunk_size = 1024  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 内容体总大小
        file_name = '%s' % unquote(file_path.split('%2F')[-1])
        progress = ProgressBar(file_name, total=content_size,
                               unit="KB", chunk_size=chunk_size, run_status="正在下载", fin_status="下载完成")
        with open(file_name, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                progress.refresh(count=len(data))

        file.close()


if __name__ == '__main__':
    get_file()