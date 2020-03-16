#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2020/3/2
"""

# from business.bus_test3.aa import clz_aa as biz
from posedion2 import po
import pytest
class Test6:
    @pytest.mark.xfail
    def test5_1(self):

        po.log.error(f"{po}::test6_1 这个是 poseidon log")
        # print("This is test5_1")


