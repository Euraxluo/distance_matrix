# -*- coding: utf-8 -*- 
# Time: 2022-03-01 11:23
# Copyright (c) 2022
# author: Euraxluo


from .conftest import register
from unittest import TestCase

from amap_distance_matrix.helper import *


class TestHelper(TestCase):
    def test_time_slot(self):
        res = time_slot_wmh()
        print(res)
        print(res[-2:])

    def test_point_pairing_sorted(self):
        res = point_pairing_sorted(*[(1, 2), (1, 2), (1, 2), (1, 2), (9, 10), (7, 9), ])
        print(res)

    def test_point_pairing_sorted_cache(self):
        # res = calculation_point_list([(116.1425, 39.7733), (116.1223, 39.7198), (116.1708, 39.7122), (116.1917, 39.7391), (116.2068, 39.7563), (116.2247, 39.7346), (116.1425, 39.7733)])
        # print(res)
        for i in range(1000):
            # res = point_pairing_sorted(*[(116.1425, 39.7733), (116.1223, 39.7198), (116.1708, 39.7122), (116.1917, 39.7391), (116.2068, 39.7563), (116.2247, 39.7346), (116.1425, 39.7733)])
            # print(res)
            res = point_pairing_sorted(*[(123.347735, 41.78451), (123.506014, 41.643884), (123.487702, 41.789835), (123.539088, 41.81769), (123.379353, 41.76286), (123.50595905831017, 41.643812432484395)])
            # res = point_pairing_sorted(*[1, 2, 3, 4, 5, 6])
            # res = point_pairing_sorted(*[(123.347735, 41.78451), (123.506014, 41.643884), (123.487702, 41.789835), (123.539088, 41.81769), (123.379353, 41.76286), (123.50595905831017, 41.643812432484395)])
            print(res)
