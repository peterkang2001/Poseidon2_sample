#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2020/3/1
"""
import pytest
class Foo:
    def __init__(self, val):
        self.val = val
    def __eq__(self, other):
        return self.val == other.val

class Test2:
    import logging
    logger = logging.getLogger("peter")
    def test2_1(self):
        self.logger.warning("This is 2_1 waning_1")
        self.logger.error("This is 2_1 error_1")
        self.logger.warning("This is 2_1 waning_2")

        print("This is test2_1")

    def test2_2(self):
        assert 0
        print("This is test2_2")
        self.logger.warning("This is 2_2 waning_1")
        self.logger.error("This is 2_2 error_1")
        self.logger.warning("This is 2_2 waning_2")



# @pytest.mark.parametrize("input, expected",
    #                          [("input_1", "expected_1"),
    #                           ("input_2", "expected_2")
    #                           ])
    # def test2_3(self, input, expected):
    #     print(f"input::{input}, expected:{expected}")
    #     print("This is test2_3")


    # def test2_4(self):
    #     f1 = Foo(1)
    #     f2 = Foo(2)
    #     assert f1 == f2
    #     print("This is test2_4")

class Test3:
    def test3_1(self):
            print("This is test3_1")
    def test3_2(self):
        print("This is test3_1")