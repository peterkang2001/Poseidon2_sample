#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2020/2/25
"""
import sys
def test_needfiles(capsys):
    sys.stdout.write("This is stdout\n")
    print("This is print out")
    sys.stderr.write("This is error\n")
    capsys.readouterr()

def test_pytestconfig(pytestconfig):
    a = pytestconfig.getoption("assertmode")
    print("hell")

def test_log(caplog):

    import logging
    logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    # logger.info("Start print log")
    # logger.debug("Do something")
    logger.warning("12Something maybe fail.")
    logger.warning("2Something maybe fail.")

    print(caplog.record_tuples)