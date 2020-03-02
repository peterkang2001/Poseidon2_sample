#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2020/3/1
"""

# 1_Bootstrapping hooks
# def pytest_load_initial_conftests(early_config, parser, args):
#     ...
#
# def pytest_cmdline_preparse(config, args):
#     ...
#
# def pytest_cmdline_parse(pluginmanager, args):
#     ...
#
# def pytest_cmdline_main(config):
#     ...
#
# # 2_Initialization hooks
# def pytest_addoption(parser, pluginmanager):
#     ...
#
# def pytest_addhooks(pluginmanager):
#     ...
#
# def pytest_configure(config):
#     ...
#
# def pytest_unconfigure(config):
#     ...
#
# def pytest_sessionstart(session):
#     ...
#
# def pytest_sessionfinish(session, exitstatus):
#     ...
#
# def pytest_plugin_registered(plugin, manager):
#     ...



def hello():
    print("********hello")

# 3_Test running hooks
# def pytest_runtestloop(session):
#     """
#     貌似仅仅就表示循环开始，目前没有发现有用得价值
#     """
#     print("开始  3_1_pytest_runtestloop")

# def pytest_runtest_protocol(item, nextitem):
#     """
#     可以获取当前需要执行的用例和下一个准备执行的用例
#     item.nodeid  nextitem.nodeid
#     """
#     print("开始  3_2_pytest_runtest_protocol")

# def pytest_runtest_logstart(nodeid, location):
#     """
#     感觉要比pytest_runtest_protocol更好，
#     能直接获得用例的nodeid和location
#     如果用param参数化用例的话nodeid和location就非常有用了
#     """
#     print("开始  3_3_pytest_runtest_logstart")

# def pytest_runtest_logfinish(nodeid, location):
#     """暂时没有发现有用的地方"""
#     print("开始 3_9_pytest_runtest_logfinish ")

# def pytest_runtest_setup(item):
#     """暂时没有发现有用的地方"""
#     print("开始 3_4_pytest_runtest_setup ")
# def pytest_runtest_makereport(item, call):
#     """call.start 可以记录用例开始执行的世界"""
#     print("开始 3_5_pytest_runtest_makereport ")
#
# def pytest_runtest_call(item):
#     """暂时没有发现有用的地方"""
#     print("开始 3_6_pytest_runtest_call ")

# def pytest_pyfunc_call(pyfuncitem):
#     """暂时没有发现有用的地方"""
#     print("开始 3_7_pytest_pyfunc_call ")

# def pytest_runtest_teardown(item, nextitem):
#     """暂时没有发现有用的地方"""
#     print("开始 3_8_pytest_runtest_teardown ")




# # 4_Collection hooks
# def pytest_collection(session):
#     ...
#
# def pytest_ignore_collect(path, config):
#     ...
#
# def pytest_collect_directory(path, parent):
#     ...
#
# def pytest_collect_file(path, parent):
#     ...
#
# def pytest_pycollect_makemodule(path, parent):
#     ...
#
# def pytest_pycollect_makeitem(collector, name, obj):
#     ...
#
# def pytest_generate_tests(metafunc):
#     ...
#
# def pytest_collection_modifyitems(session, config, items):
#     ...
#
# def pytest_collection_finish(session):
#     ...
#
# # 5_Reporting hooks
# def pytest_report_header(config, startdir):
#     """暂时没有发现有价值的地方"""
#     print("开始  5_1_pytest_report_header")

# def pytest_collectstart(collector):
#     """暂时没有发现有价值的地方"""
#     print("开始  5_2_pytest_collectstart")

# def pytest_make_collect_report(collector):
#     """暂时没有发现有价值的地方"""
#     print("开始  5_3_pytest_make_collect_report")

# def pytest_itemcollected(item):
#     """暂时没有发现有价值的地方"""
#     print("开始  5_4_pytest_itemcollected")

# def pytest_report_collectionfinish(config, startdir, items):
#     """暂时没有发现有价值的地方"""
#     print("开始  5_5_pytest_report_collectionfinish")

# def pytest_report_teststatus(report, config):
#     """这个是用例setup之后在第一行代码执行前执行的，
#     所以可以在这里获取用例的基本信息
#     觉得要比pytest_runtest_logstart 获取的信息更好完整一些
#     """
#     print("开始  5_6_pytest_report_teststatus")

# def pytest_runtest_logreport(report):
#     """作用不大暂时忽略"""
#     print("开始  5_7_pytest_runtest_logreport")

# def pytest_terminal_summary(terminalreporter, exitstatus, config):
#     """
#     重要：
#     exitstatus
#     terminalreporter.stats
#     terminalreporter._sessionstarttime ？？
#     如一个目录2个测试文件，一个 测试文件里分别有2个测试类，每个测试类中有2个测试用例
#     这个方法只会使用1次
#     """
#     print("开始  5_8_pytest_terminal_summary")

# def pytest_collectreport(report):
#     """
#     1. 在一次执行多个用例时使用， 比如一个类多个测试方法，一个测试文件多个测试类等
#     2. 并且是在一行测试代码没有执行的时候执行的
#     3. 用来收集用例名称，并设置result字段，
#         如一个测试类有2个测试方法，就会在result中生成2个数据的list
#         如一个测试文件有2个测试类，每个测试类有2个测试方法，会执行两次上面的操作，
#             另外再生成一次将两个测试类组装起来
#     """
#     print("开始  pytest_collectreport")





# def pytest_assertrepr_compare(config, op, left, right):
#     """
#     只有使用到对象的的方法的时候才会进来，普通字符串是不会进来的
#     这个扩展我想应该是用户在自定义的时候才会使用到，
#     因为类对象的比较只有碰到实际业务才能确定，所以暂时不处理
#     """
#     print("1111开始  pytest_assertrepr_compare")

# def pytest_assertion_pass(item, lineno, orig, expl):
#     """关系到assert，设置了断点但是没有跟踪进来，不知道什么原因，放在后面处理"""
#     print("1111开始  pytest_assertion_pass")


# def pytest_deselected(items):
#     """不知道怎么使用，暂时不处理"""
#     print("开始  pytest_deselected")
# def pytest_fixture_setup(fixturedef, request):
#     """关系到fixture，放到后面处理"""
#     print("开始  pytest_fixture_setup")
#
# def pytest_fixture_post_finalizer(fixturedef, request):
#     """关系到fixture，放到后面处理"""
#     print("开始  pytest_fixture_post_finalizer")

# def pytest_warning_captured(warning_message, when, item, location):
#         """这个报location错误，感觉用不到，所以不关注"""
#     print("开始  pytest_warning_captured")

# # 6_Debugging/Interaction hooks
# def pytest_internalerror(excrepr, excinfo):
#     ...
#
# def pytest_keyboard_interrupt(excinfo):
#     ...
#
def pytest_exception_interact(node, call, report):
    """
    call.excinfo
    report.nodeid
    report.longrepr

    """
    print("pytest_exception_interact")
#
# def pytest_enter_pdb(config, pdb):
#     ...