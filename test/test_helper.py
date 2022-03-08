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
