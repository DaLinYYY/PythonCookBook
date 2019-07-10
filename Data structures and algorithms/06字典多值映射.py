#!/usr/bin/env python
# encoding: utf-8
'''
@Topic: 字典多值映射
@desc:
@contact : dalin.strive@gmail.com    @author : dalin
@time: 2019/7/7 12:16
'''

from collections import defaultdict


def multi_dict():
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)

    d = {} # A regular dictionary
    d.setdefault('a', []).append(1)
    d.setdefault('a', []).append(2)
    d.setdefault('b', []).append(4)