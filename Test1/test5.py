#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2020/2/27
   测试python3 最新的模板语法
"""
import logging
def test1():
    print("hello {}".format("peter"))
    aa = {"name": "peter", "age": 20}
    # 使用了最新的模板语法

    logger = logging.getLogger("peter")

    logger.warning(f"helo {aa['name']}, {aa.get('age')}")