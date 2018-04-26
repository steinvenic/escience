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

import click


import click

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    click.echo(param)
    ctx.exit()

@click.command()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
@click.option('--name', default='Ethan', help='name')
@click.option('--param', default='', help='name')
def hello(name):
    click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()