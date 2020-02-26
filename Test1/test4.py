#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2020/2/26
   确定一下fixture写在测试类里面还是外面
"""
import pytest
@pytest.fixture()
def aa(request):
    print("fixture start....::{}".format(request.function))
    a = Man("peter22", 20)
    yield a
    print("fixture end....")

class Man():
    name = ""
    age = 0
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def __str__(self):
        return "name = {0}, age = {1}".format(self.name, self.age)

class Test4():

    @pytest.fixture()
    def bb(request):
        print("bb fixture start....::")
        a = Man("peter22", 20)
        yield a
        print("bb fixture end....")

    def test43(self,bb):
        print("This is test43 {}".format(bb))

    # def test41(self,aa):
    #     print("This is test41 {}".format(aa))
    #
    # def test42(self, aa):
    #     print("This is test42 {}".format(aa))


