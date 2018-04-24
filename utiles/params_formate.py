#!/usr/bin/env python
# encoding: utf-8


"""
@version: python2.7
@author: ‘eric‘
@license: Apache Licence 
@contact: steinven@qq.com
@site: 00123.ml:8000
@software: PyCharm
@file: params_formate.py
@time: 18/4/24 下午1:21
"""

import pprint,urllib3
from urllib.parse import unquote
str = '''

User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Connection: keep-alive
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Host: ddl.escience.cn
Origin: https://passport.escience.cn
Referer: https://passport.escience.cn/oauth2/authorize?response_type=code&redirect_uri=http://ddl.escience.cn/system/login/token&client_id=87142&theme=full&state=http://ddl.escience.cn/pan/list
Upgrade-Insecure-Requests: 1
Cookie: JSESSIONID=2DD7CEAF782F66C6905615EBD968606F-n1; AUTO_FILL="761701732@qq.com"

'''
params_dict = {}
if ':'  in str:
    str = str.split('\n')
    str = [i for i in str if len(i)>0]

    for i in str :
        m = i.split(': ')
        params_dict.update({m[0]:m[1]})
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(params_dict)

else:
    str = unquote(str).strip()
    str = str.split('&')
    for i in str:
        m = i.split('=')
        params_dict.update({m[0]:m[1]})
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(params_dict)



