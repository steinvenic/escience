# encoding: utf-8
"""
@version: python3.6
@author: ‘eric‘
@license: Apache Licence 
@contact: steinven@qq.com
@site: 00123.ml:8000
@software: PyCharm
@file: download_file.py
@time: 2018/4/22 20:50
"""

import requests

User_Agent = r'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
X_Requested = 'XMLHttpRequest'
def get_cookie():
    params = {}
    url = 'http://ddl.escience.cn/pan/list'
    header = {
        'Host':'ddl.escience.cn',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':str(User_Agent),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    params.update({'cookie':requests.get(url,headers=header).cookies})
    return params

def login():
    params = get_cookie()
    cookie = params['cookie']
    url = 'https://passport.escience.cn/oauth2/authorize'
    header = {
        'Host':'passport.escience.cn',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Origin':'https://passport.escience.cn',
        'User-Agent':User_Agent,
        'X-Requested-With':X_Requested,
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer':'https://passport.escience.cn/oauth2/authorize',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
    }
    data = {
        'userName':'761701732@qq.com',
        'password':'Aaa00123',
        'clientId':'87142',
        'clientName':'团队文档库',
        'pageinfo':'checkPassword',
    }
    r = requests.post(url,headers=header,cookies=cookie,verify=False,data=data).headers
    return params

def oauth2():
    params = login()
    cookie = params['cookie']
    url = 'https://passport.escience.cn/oauth2/authorize?client_id=87142&redirect_uri=http://ddl.' \
          'escience.cn/system/login/token&response_type=code&state=http://ddl.escience.cn/pan/list&theme=full'

    header = {
        'Host': 'passport.escience.cn',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Origin': 'https://passport.escience.cn',
        'User-Agent': User_Agent,
        'X-Requested-With': X_Requested,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://passport.escience.cn/oauth2/authorize',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    data = {
        'userName':'761701732@qq.com',
        'password':'Aaa00123',
        'act':'Validate',
        'pageinfo':'userinfo',
        'theme':'full',
    }
    r = requests.post(url,headers=header,cookies=cookie,data=data,verify=False)
    return params

def get_file():
    url = 'http://ddl.escience.cn/pan/download?path=%2FLinux_Chales_crack_4.2.5.tar.gz'
    params = oauth2()
    cookie = params['cookie']
    headers = {
        'Host': 'ddl.escience.cn',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://ddl.escience.cn/pan/list',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    res = requests.get(url, headers=headers,cookies=cookie,verify=False)
    print(res)
    res.raise_for_status()
    playFile = open('Linux_Chales_crack_4.2.5.tar.gz', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()

get_file()








