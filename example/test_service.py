# -*- coding: utf-8 -*- 
# Time: 2022-03-01 11:23
# Copyright (c) 2022
# author: Euraxluo


from .conftest import register
from unittest import TestCase

from distance_matrix.services.service import *
from distance_matrix.services.geo import *


class TestHelper(TestCase):
    def test_distance_matrix(self):
        # res = geo_addr_city([("大兴", "北京")])
        res = geo_addr_city([("四川科技馆", "成都"), ("天府广场", "成都"), ("太古里", "成都"), ("成都IFS", "成都")])
        a, b, c = distance_matrix(*res, time_slot='30', strictly_constrained=False)
        for i, vs in a.items():
            for j, v in vs.items():
                print(i, j, v)
        print("=========================================")
        for i, vs in b.items():
            for j, v in vs.items():
                print(i, j, v)
        print("=========================================")
        for i, vs in c.items():
            for j, v in vs.items():
                print(i, j, v)
        time.sleep(3)

    def test_route_waypoints(self):
        res = geo_addr_city([("天府五街", "成都"), ("太古里", "成都"), ("天府三街", "成都")])
        print(res)
        res = waypoints_route(*res, time_slot='17', strictly_constrained=False)
        for i in res:
            print(i)
        time.sleep(2)
