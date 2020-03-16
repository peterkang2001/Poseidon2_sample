#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2020/3/6
"""

#  这个文件可以放到 pip包里
#  这个文件只处理生成对象、初始化，并返回，没有任何业务逻辑
class Poseidon:
    @property
    def log(self):
        import logging
        logger = logging.getLogger("peter")
        return logger

    # @property
    # def redis(self):
    #     print("This is redis")

po = Poseidon()