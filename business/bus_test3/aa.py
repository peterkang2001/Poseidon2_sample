#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2020/3/6
"""
from poseidon import po
class Business_clazz_aa:
    def bus_func_aaa(self):
        po.log.warning(f"{po}::这个是buiness warning")

clz_aa = Business_clazz_aa()