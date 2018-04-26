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
import sys,configparser,pprint
from prettytable import PrettyTable

def search_list():

    d = [{'shared': False, 'createTime': '2018-04-25 01:19', 'fileType': '', 'parentRid': '', 'itemType': 'Folder', 'lastEditor': '杨力', 'contentType': '', 'size': '0 B', 'searchResult': False, 'lastEditorUid': '761701732@qq.com', 'rid': '%2Fdir_1', 'lastVersion': 15, 'fileName': 'dir_1', 'modofyTime': '2018-04-25 01:18'}, {'shared': False, 'createTime': '2018-04-26 20:21', 'fileType': '7z', 'parentRid': '', 'itemType': 'DFile', 'lastEditor': '杨力', 'contentType': 'application/octet-stream', 'size': '1 KB', 'searchResult': False, 'lastEditorUid': '761701732@qq.com', 'rid': '%2F%E4%BD%A0%E4%BC%9A%E8%A7%89%E5%BE%97%E7%83%A6test.7z', 'lastVersion': 20, 'fileName': '你会觉得烦test.7z', 'modofyTime': '2018-04-26 20:21'}, {'shared': False, 'createTime': '2018-04-26 20:21', 'fileType': '7z', 'parentRid': '', 'itemType': 'DFile', 'lastEditor': '杨力', 'contentType': 'application/octet-stream', 'size': '1 KB', 'searchResult': False, 'lastEditorUid': '761701732@qq.com', 'rid': '%2Ftest.7z', 'lastVersion': 19, 'fileName': 'test.7z', 'modofyTime': '2018-04-26 20:21'}, {'shared': False, 'createTime': '2018-04-26 20:21', 'fileType': '7z', 'parentRid': '', 'itemType': 'DFile', 'lastEditor': '杨力', 'contentType': 'application/octet-stream', 'size': '1 KB', 'searchResult': False, 'lastEditorUid': '761701732@qq.com', 'rid': '%2Fetst.7z', 'lastVersion': 18, 'fileName': 'etst.7z', 'modofyTime': '2018-04-26 20:21'}, {'shared': False, 'createTime': '2018-04-26 20:21', 'fileType': '7z', 'parentRid': '', 'itemType': 'DFile', 'lastEditor': '杨力', 'contentType': 'application/octet-stream', 'size': '1 KB', 'searchResult': False, 'lastEditorUid': '761701732@qq.com', 'rid': '%2F11test33.7z', 'lastVersion': 17, 'fileName': '11test33.7z', 'modofyTime': '2018-04-26 20:21'}, {'shared': False, 'createTime': '2018-04-21 17:11', 'fileType': 'gz', 'parentRid': '', 'itemType': 'DFile', 'lastEditor': '杨力', 'contentType': 'application/x-gzip', 'size': '59.6 MB', 'searchResult': False, 'lastEditorUid': '761701732@qq.com', 'rid': '%2FLinux_Chales_crack_4.2.5.tar.gz', 'lastVersion': 10, 'fileName': 'Linux_Chales_crack_4.2.5.tar.gz', 'modofyTime': '2018-04-21 17:11'}, {'shared': False, 'createTime': '2018-04-21 01:30', 'fileType': 'gz', 'parentRid': '', 'itemType': 'DFile', 'lastEditor': '杨力', 'contentType': 'application/x-gzip', 'size': '307.5 MB', 'searchResult': False, 'lastEditorUid': '761701732@qq.com', 'rid': '%2Fjira.tar.gz', 'lastVersion': 1, 'fileName': 'jira.tar.gz', 'modofyTime': '2018-04-21 01:30'}]
    d = [i for i in d if i['itemType']!='Folder']
    x = PrettyTable()
    x.field_names = ["ID", "FileName", "CreateTime", "Size"]
    m = 0
    id_file_dict = {}
    for i in d:
        x.add_row([m,i['fileName'],i['modofyTime'],i['size']])
        id_file_dict.update({m:i['rid']})
        m+=1
    print(x)
    return id_file_dict


if __name__ == '__main__':
    search_list()

# d = [1,2,4,5,6,7,78]
# m = [m for m in d if m>5 ]
# print(m)