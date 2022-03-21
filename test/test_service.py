# -*- coding: utf-8 -*- 
# Time: 2022-03-01 11:23
# Copyright (c) 2022
# author: Euraxluo


from .conftest import register
from unittest import TestCase

from amap_distance_matrix.services.service import *
from amap_distance_matrix.services.geo import *


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

    def test_distance_matrix_all(self):
        import time
        s = time.perf_counter()
        for i in range(100):
            # points = [(116.1425, 39.7733), (116.1223, 39.7198), (116.1708, 39.7122), (116.1917, 39.7391), (116.2068, 39.7563), (116.2247, 39.7346), (116.1425, 39.7733), (116.1425, 39.7733), (116.1425, 39.7733)]
            # points = [(116.1425, 39.7733), (116.1223, 39.7198), (116.1708, 39.7122), (116.1917, 39.7391), (116.2068, 39.7563), (116.2247, 39.7346), (116.1425, 39.7733)]
            # points = [(123.347735, 41.78451), (123.506014, 41.643884), (123.487702, 41.789835), (123.539088, 41.81769), (123.379353, 41.76286), (123.50595905831017, 41.643812432484395)]
            points = [(116.4459, 39.8696), (116.4015, 39.8999), (116.4023, 39.9002), (116.4041, 39.9002),
                      (116.4051, 39.9003), (116.4059, 39.9003), (116.4066, 39.8962), (116.4066, 39.8963),
                      (116.4066, 39.896), (116.4067, 39.8968),
                      (116.4068, 39.8933), (116.4068, 39.8963), (116.4068, 39.8965), (116.4068, 39.8966),
                      (116.4077, 39.9003), (116.4092, 39.9005), (116.4128, 39.9004), (116.4158, 39.9006),
                      (116.4287, 39.9004), (116.4309, 39.9003),
                      (116.4641, 39.8659), (116.4459, 39.8696), (116.4459, 39.8696), (116.4459, 39.8696)]

            res, _, _ = distance_matrix(*points)
            print(time.perf_counter() - s)
