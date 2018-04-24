#!/usr/bin/env python
# encoding: utf-8


"""
@version: python2.7
@author: ‘eric‘
@license: Apache Licence 
@contact: steinven@qq.com
@site: 00123.ml:8000
@software: PyCharm
@file: demo.py
@time: 18/4/24 下午2:41
"""

import requests

def get_oauth():
    global_params = {}
    url ='https://passport.escience.cn/oauth2/authorize?response_type=code&redirect_uri=http://ddl.escience.cn/system/login/token&client_id=87142&theme=full&state=http://ddl.escience.cn/pan/list'
    headers = {   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'passport.escience.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    global_params.update({'cookies':requests.get(url,headers=headers,verify=False).cookies})
    return global_params

def oauth():
    global_params = get_oauth()
    cookies = global_params['cookies']
    headers = {   'Accept': 'application/json, text/javascript, */*; q=0.01',
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
    data = {   'clientId': '87142',
                'clientName': '团队文档库',
                'pageinfo': 'checkPassword',
                'password': 'Aaa00123',
                'userName': '761701732@qq.com'}
    requests.post(url,headers=headers,cookies=cookies,verify=False,data=data)
    return global_params

def oauth_1():
    global_params = oauth()
    cookies = global_params['cookies']
    url = 'https://passport.escience.cn/oauth2/authorize?client_id=87142&redirect_uri=http://' \
          'ddl.escience.cn/system/login/token&response_type=code&state=http://ddl.escience.cn/pan/list&theme=full'
    headers ={   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
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
    data ={   'act': 'Validate',
    'pageinfo': 'userinfo',
    'password': 'Aaa00123',
    'theme': 'full',
    'userName': '761701732@qq.com'}
    r = requests.post(url,headers=headers,data=data,verify=False,cookies=cookies,allow_redirects=False)
    r_location = r.headers['Location']
    global_params.update({'url_location':r_location})
    return global_params

def location():
    global_params = oauth_1()
    location_url = global_params['url_location']
    cookies = global_params['cookies']
    headers = {   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
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
    r = requests.get(url=location_url,headers=headers,cookies=cookies,allow_redirects=False)
    global_params.update({'cookies':r.cookies})
    return global_params


def get_file():
    global_params = location()
    cookies = global_params['cookies']
    url = 'http://ddl.escience.cn/pan/download?path=%2FLinux_Chales_crack_4.2.5.tar.gz'
    headers = {   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'ddl.escience.cn',
    'Referer': 'http://ddl.escience.cn/pan/list',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

    res = requests.get(url,headers=headers,verify=False,cookies=cookies)
    res.raise_for_status()
    playFile = open('Linux_Chales_crack_4.2.5.tar.gz', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()


get_file()


