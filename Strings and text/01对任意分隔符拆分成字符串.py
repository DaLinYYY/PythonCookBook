#!/usr/bin/env python
# encoding: utf-8
'''
@Topic: 01对任意分隔符拆分成字符串
@desc:
@contact : dalin.strive@gmail.com    @author : dalin
@time: 2019/7/10 23:10
'''

import re


def split_str():
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    print(re.split(r'[;,\s]\s*', line))
    print(re.split(r'(;|,|\s)\s*', line))
    fields = re.split(r'(;|,|\s)\s*', line)
    values = fields[::2]
    delimiters = fields[1::2] + ['']
    print(''.join(v+d for v,d in zip(values, delimiters)))

if __name__ == '__main__':
    split_str()
