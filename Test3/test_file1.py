#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2020/3/2
"""
import Test3


from poseidon import po
from business.bus_test3.aa import clz_aa as biz
class Test4:
    def test4_1(self):

        po.log.error(f"{po}::这个是 poseidon log")
        biz.bus_func_aaa()

    def test4_2(self):
        po.log.error(f"{po}::这个是 poseidon log")
        print("This is test4_1")

    def test4_3(self):
        print(__import__())