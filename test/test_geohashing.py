# -*- coding: utf-8 -*- 
# Time: 2022-03-02 15:32
# Copyright (c) 2022
# author: Euraxluo


from .conftest import register
from unittest import TestCase

from amap_distance_matrix.services.geo import *
from amap_distance_matrix.services.geohashing import *


class Test(TestCase):
    def test_geo_add(self):
        res = geo_addr_city([("天安门", "北京"), ("大兴", "北京")])
        print(res)
        geo_add(*res)

    def test_geo_radius(self):
        res = geo_addr_city([("天安门", "北京"), ("大兴", "北京")])
        print(res)
        geo_add(*res)
        res = geo_addr_city([("故宫博物馆", "北京")])
        print(res)
        res = geo_radius(res[0], 0, 'km')
        print(res)

    def test_geo_add2(self):
        res = geo_add([116, 45.0011])

    def test_georadius2(self):
        res = geo_radius([116.001, 39.001])
        print(res)
        res = geo_radius([116.001, 45.001])
        print(res)
