# -*- coding: utf-8 -*- 
# Time: 2022-03-01 11:23
# Copyright (c) 2022
# author: Euraxluo


from .conftest import register
from unittest import TestCase

from amap_distance_matrix.services.persistence import *


class TestHelper(TestCase):
    def test_persistence(self):
        c = time.perf_counter()
        res = edge_persistence()
        print(time.perf_counter() - c)

    def test_get_edge(self):
        res = get_edge(start=[116.002, 39.002], end=[116.002, 45.002], t='18')
        print(res)
