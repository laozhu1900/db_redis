#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

# from conf import setting
import redis

__author__ = 'zhuzw'


class RedisConnection:

    def __init__(self, db_args):
        self.connect = redis.Redis(host=db_args['host'], port=db_args['post'], db=0)
        self.pipe = self.connect.pipeline()



