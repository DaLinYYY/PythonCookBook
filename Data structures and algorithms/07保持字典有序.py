#!/usr/bin/env python
# encoding: utf-8
'''
@Topic: 07保持字典有序
@desc:
@contact : dalin.strive@gmail.com    @author : dalin
@time: 2019/7/7 13:56
'''

from collections import OrderedDict


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])
