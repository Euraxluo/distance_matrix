# -*- coding: utf-8 -*- 
# Time: 2022-03-02 15:49
# Copyright (c) 2022
# author: Euraxluo

# -*- coding: utf-8 -*-
# Time: 2022-02-11 11:59
# Copyright (c) 2022
# author: Euraxluo


import redis
import json
from typing import Union, Callable


class RedisHelper(object):

    def __init__(self, host='127.0.0.1', port='6379', db=1, password='redis', decode_responses=False):
        redis.ConnectionPool()
        self.pool = redis.ConnectionPool(host=host, port=port, db=db, password=password, decode_responses=decode_responses)
        self.r = redis.Redis(connection_pool=self.pool)

    def rdb(self) -> redis.Redis:
        return self.r

    @staticmethod
    def encode(data: dict, default: dict = {}):
        if data:
            return json.dumps(data)
        return json.dumps(default)

    @staticmethod
    def decode(data: Union[str, bytes], instance: Callable = str):
        if data:
            return json.loads(data)
        return instance().__dict__()


rdb = RedisHelper().rdb()
from amap_distance_matrix.services.register import register
from loguru import logger

register.setup(keys=["4396fb03833e27e6438dde36c7457cc3", "4396fb03833e27e6438dde36c7457cc3"], logger=logger, osrm_host="", conn=rdb,
               persistence_uri="mysql+pymysql://root:mysql@localhost:3306",database="distance_matrix")
