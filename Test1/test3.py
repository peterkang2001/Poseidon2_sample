#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2020/2/26
   测试fixture scope
"""
import time

import pytest


# @pytest.fixture(scope="function")
# @pytest.fixture(scope="session")
# @pytest.fixture(scope="module")
# @pytest.fixture(scope="class")
@pytest.fixture(autouse=True)
def hellofixture():
    str = time.time()
    return str


class Test3():
    def test1(self, hellofixture):
        print("This is test1 {0}".format(hellofixture))
        # assert 0

    def test2(self, hellofixture):
        print("This is test2 {0}".format(hellofixture))
        # assert 0

    # def test3(self, hellofixture):
    #     print("This is test3")
    #     assert 0
