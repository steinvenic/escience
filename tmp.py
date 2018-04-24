# encoding: utf-8
"""
@version: python3.6
@author: ‘eric‘
@license: Apache Licence 
@contact: steinven@qq.com
@site: 00123.ml:8000
@software: PyCharm
@file: tmp.py
@time: 2018/4/22 3:34
"""
import requests
import sys,configparser
conf = configparser.ConfigParser()
conf.read('conf.cfg')
name = conf.get('user_info','userName')
print(name)
