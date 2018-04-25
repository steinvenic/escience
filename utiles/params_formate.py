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
{"tokenKey":"1524672146487","total":3,"currentResource":{"shared":null,"createTime":"2018-04-21 01:27","fileType":"","parentRid":"\/","itemType":"Folder","lastEditor":"杨力","contentType":"","size":"0 B","searchResult":false,"lastEditorUid":"761701732@qq.com","rid":"","lastVersion":0,"fileName":null,"modofyTime":"2018-04-21 01:27"},"order":"timeDesc","nextBeginNum":"0","path":[],"children":[{"shared":false,"createTime":"2018-04-25 01:19","fileType":"","parentRid":"","itemType":"Folder","lastEditor":"杨力","contentType":"","size":"0 B","searchResult":false,"lastEditorUid":"761701732@qq.com","rid":"%2Fdir_1","lastVersion":15,"fileName":"dir_1","modofyTime":"2018-04-25 01:18"},{"shared":false,"createTime":"2018-04-21 17:11","fileType":"gz","parentRid":"","itemType":"DFile","lastEditor":"杨力","contentType":"application\/x-gzip","size":"59.6 MB","searchResult":false,"lastEditorUid":"761701732@qq.com","rid":"%2FLinux_Chales_crack_4.2.5.tar.gz","lastVersion":10,"fileName":"Linux_Chales_crack_4.2.5.tar.gz","modofyTime":"2018-04-21 17:11"},{"shared":false,"createTime":"2018-04-21 01:30","fileType":"gz","parentRid":"","itemType":"DFile","lastEditor":"杨力","contentType":"application\/x-gzip","size":"307.5 MB","searchResult":false,"lastEditorUid":"761701732@qq.com","rid":"%2Fjira.tar.gz","lastVersion":1,"fileName":"jira.tar.gz","modofyTime":"2018-04-21 01:30"}],"showSearch":true,"size":3}
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



