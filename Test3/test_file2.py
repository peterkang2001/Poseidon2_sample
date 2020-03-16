#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2020/3/2
"""

from business.bus_test3.aa import clz_aa as biz
from poseidon import po
class Test4:
    def test5_1(self):
        po.log.error(f"{po}::test5_1 这个是 poseidon log")
        print("This is test5_1")

    def test5_2(self):
        po.log.error(f"{po}::test5_2 这个是 poseidon log")
        print("This is test5_2")