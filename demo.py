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
proxies = { "http": "192.168.1.163:8888" }
def pan_list():
    params = {}
    headers = {   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'ddl.escience.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 '
                  'Safari/537.36'}
    url = 'http://ddl.escience.cn/pan/list'
    params.update({'cookies':requests.get(url,headers=headers,proxies=proxies).cookies})
    return params

def system_login():
    params = pan_list()
    cookies = params['cookies']
    url = 'http://ddl.escience.cn/system/login?&vwb.requesturl=http%3A%2F%2Fddl.escience.cn%2Fpan%2Flist'
    headers = {   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'ddl.escience.cn',
    'Referer': 'http://ddl.escience.cn/pan/list',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 '
                  'Safari/537.36'}
    r = requests.get(url,headers=headers,cookies=cookies,proxies=proxies)

system_login()
