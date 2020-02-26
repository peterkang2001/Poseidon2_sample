#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2020/2/26
"""
from contextlib import contextmanager

class MyResource:
    def query(self):
        print("Query data")

@contextmanager
def make_myresource():
    print("start connect to resource")
    yield MyResource()
    print("end connect to resource")

if __name__ == '__main__':
    with make_myresource() as r:
        r.query()
