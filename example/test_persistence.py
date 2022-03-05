# -*- coding: utf-8 -*- 
# Time: 2022-03-01 11:23
# Copyright (c) 2022
# author: Euraxluo


from .conftest import register
from unittest import TestCase

from distance_matrix.services.persistence import *


class TestHelper(TestCase):
    def test_persistence(self):
        c = time.perf_counter()
        res = edge_persistence()
        print(time.perf_counter() - c)
