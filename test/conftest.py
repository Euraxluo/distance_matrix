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
    """
    redis==2.10.6
    redis-py-cluster==1.3.6
    """

    def __init__(self, host='localhost', port='6379', db=0, password='redis',
                 decode_responses=False):
        self.pool = redis.ConnectionPool(host=host, port=port, db=db, password=password,
                                         decode_responses=decode_responses)
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

register.setup(keys=["8011e4f922fbfdc87874848d256baa09"], logger=logger, osrm_host="", conn=rdb,
               persistence_uri="mysql+pymysql://root:mysql@localhost:3306", database="distance_matrix",
               geohashing_keys="{test}:" + "distance_matrix:geohashing_keys",
               edge_key="{test}:" + "distance_matrix:edge_hash",
               geo_key="{test}:" + "distance_matrix:geohashing"
               )
