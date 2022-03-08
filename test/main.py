# -*- coding: utf-8 -*- 
# Time: 2022-03-07 18:49
# Copyright (c) 2022
# author: Euraxluo

from .conftest import *
import unittest
from loguru import logger
import logging

import HTMLReport.src.tools.result as test_result
import HTMLReport.src.test_runner as test_runner

logger.getLogger = logging.getLogger
test_result.logging = logger
test_runner.logging = logger


class Test(unittest.TestCase):
    def test_project(self):
        """
        对整个项目进行测试,包括所有的测试用例和,__init__
        :return:
        """
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().discover('.', pattern='test_*', top_level_dir='.'))
        print([j for i in suite._tests for j in i])
        runner = test_runner.TestRunner(report_file_name='test',
                                        output_path='report',
                                        title='distance-matrix test report',
                                        description='summer',
                                        sequential_execution=False,
                                        thread_count=1,
                                        lang='en'
                                        )

        runner.run(suite)
