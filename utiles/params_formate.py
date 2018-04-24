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

import pprint

str = '''

Host: ddl.escience.cn
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://ddl.escience.cn/pan/list
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=DBB62FD55B2D5F163F24297740056FC3-n1

'''


str = str.split('\n')
str = [i for i in str if len(i)>0]
params_dict = {}
for i in str :
    m = i.split(': ')
    params_dict.update({m[0]:m[1]})
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(params_dict)

