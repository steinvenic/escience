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
'''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://ddl.escience.cn/pan/list
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: fullscr=; QRCode=QRCode; JSESSIONID=CD6088E81C119FD037592BFAF1C235CF-n1; decreaseScore=test



'''
headers = {
    'Host':'ddl.escience.cn',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer':'http://ddl.escience.cn/pan/list',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cookie':'fullscr=; QRCode=QRCode; JSESSIONID=CD6088E81C119FD037592BFAF1C235CF-n1; decreaseScore=test',

}



res = requests.get('http://ddl.escience.cn/pan/download?path=%2FLinux_Chales_crack_4.2.5.tar.gz',headers=headers)
res.raise_for_status()
playFile = open('Linux_Chales_crack_4.2.5.tar.gz', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()