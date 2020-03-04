#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2020/3/3
"""
import pytest
@pytest.fixture()
def hello():
    print("This is 你好")
