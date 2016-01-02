#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import redis

__author__ = 'zhuzw'


class RedisConnection:

    def __init__(self, dbargs):
        self.connect = redis.Redis(host=dbargs['host'], port=dbargs['post'],db=0)
        self.pipe = self.connect.pipeline()

    def exp_grid(self, grid):
        _prefix = 'GRID_'
        key = _prefix + grid
        return self.connect.hvals(key)