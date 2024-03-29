#!/usr/bin/env python
# encoding: utf-8
'''
@Topic: 06优先级队列
@desc:
@contact : dalin.strive@gmail.com    @author : dalin
@time: 2019/7/7 12:15
'''
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
