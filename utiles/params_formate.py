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
path=&sortType=&tokenKey=1524916899135&keyWord=jira
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



