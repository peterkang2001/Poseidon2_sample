#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2020/3/1
"""

# 1_Bootstrapping hooks
#
# def pytest_cmdline_preparse(config, args):
    # """
    # (**不建议使用**）在选项解析之前修改命令行参数
    # """
    # print("开始  4_1_1_pytest_cmdline_preparse")

# def pytest_cmdline_main(config):
#     """
#     要求执行主命令行操作。默认实现将调用configure钩子和runtest_mainloop。
#     """
#     print("开始  5_1_2_pytest_cmdline_main")

#
# def pytest_load_initial_conftests(early_config, parser, args):
#     """
#     实现预先加载初始conftest文件命令行选项解析。
#     注意：仅对于setuptools插件，不会为conftest.py文件调用此钩子。
#     """
#     print("开始  pytest_load_initial_conftests")
#
# def pytest_cmdline_parse(pluginmanager, args):
#     """
#       返回初始化的配置对象，解析指定的参数
#     """
#     print("开始  pytest_cmdline_parse")



# # 2_Initialization hooks
# def pytest_addhooks(pluginmanager):
#     """
#     在插件注册时调用，以允许通过调用来添加新的挂钩
#     """
#     print("开始 1_2_1_pytest_addhooks")
#
# def pytest_addoption(parser, pluginmanager):
#     """
#     注册argparse风格的选项和ini风格的配置值，这些值在测试运行开始时被调用一次。
#     parser.extra_info['rootdir']
#     parser.extra_info['inifile']
#     """
#     print("开始 2_2_2_pytest_addoption")
#
# def pytest_plugin_registered(plugin, manager):
#     """
#     一个新的pytest插件已注册
#     """
#     print("开始 3_2_3_pytest_plugin_registered")
#
# def pytest_configure(config):
#     """
#     允许插件和conftest文件执行初始配置。
#     解析了命令行选项后，将为每个插件和初始conftest文件调用此挂钩。
#     """
#     print("开始 6_2_4_pytest_configure")
#
# def pytest_sessionstart(session):
#     """
#     创建Session对象之后，执行收集并进入运行测试循环之前调用。
#     """
#     print("开始 7_2_5_pytest_sessionstart")
#
# def pytest_sessionfinish(session, exitstatus):
#     """
#     在整个测试运行完成后调用，即将退出状态返回给系统。
#     """
#     print("开始 32_2_6_pytest_sessionfinish")

# def pytest_unconfigure(config):
#     """
#     在退出测试过程之前调用。
#     """
#     print("开始 33_2_7_pytest_unconfigure")



# 3_Test running hooks
# def pytest_runtestloop(session):
#     """
#     调用以执行主要的runtest循环（收集完成后）
#     貌似仅仅就表示循环开始，目前没有发现有用得价值
#     """
#     print("开始  21_3_1_pytest_runtestloop")

# def pytest_runtest_protocol(item, nextitem):
#     """
#     为给定的测试项目实现runtest_setup / call / teardown协议，包括捕获异常和调用报告挂钩。
#     可以获取当前需要执行的用例和下一个准备执行的用例
#     item.nodeid  nextitem.nodeid
#     """
    # item.add_report_section("call", "stdout", "测试报告自定义")
    # item.add_report_section("setup", "stdout", "测试报告setup自定义")
    # item.add_report_section("teardown", "stdout", "测试报告teardown自定义")
    # print("开始  22_3_2_pytest_runtest_protocol")

# def pytest_runtest_logstart(nodeid, location):
#     """
#       发出开始运行单个测试项目的信号
#     感觉要比pytest_runtest_protocol更好，
#     能直接获得用例的nodeid和location
#     如果用param参数化用例的话nodeid和location就非常有用了
#     """
#     print("开始  23_3_3_pytest_runtest_logstart")
#
# def pytest_runtest_setup(item):
#     """
#       在pytest_runtest_call（item）之前调用
#     暂时没有发现有用的地方
#     """
#     print("开始 24_3_4_pytest_runtest_setup ")

# def pytest_runtest_makereport(item, call):
#     """
#     停在第一个非无结果
#     call.start 可以记录用例开始执行的时间
#     """
#     print("开始 25_3_5_pytest_runtest_makereport ")
#
# def pytest_runtest_call(item):
#     """
#       调用以执行测试项目。
#     暂时没有发现有用的地方
#     """
#     print("开始 28_3_6_pytest_runtest_call ")
#
# def pytest_pyfunc_call(pyfuncitem):
#     """
#     调用基础测试功能。
#     暂时没有发现有用的地方
#     """
#     print("开始 29_3_7_pytest_pyfunc_call ")
#
# def pytest_runtest_teardown(item, nextitem):
#     """
#     在pytest_runtest_call之后调用
#     暂时没有发现有用的地方
#     这一步之前已经完成测试用例代码的执行
#     """
#     print("开始 30_3_8_pytest_runtest_teardown ")
#
# def pytest_runtest_logfinish(nodeid, location):
#     """
#       表示运行单个测试项目已完成
#     暂时没有发现有用的地方
#     """
#     print("开始 31_3_9_pytest_runtest_logfinish ")
#
#
# # # 4_Collection hooks
# def pytest_collection(session):
#     """
#     执行给定会话的收集协议。
#     """
#     print("开始  9_4_1_pytest_collection")

# def pytest_ignore_collect(path, config):
#     """
#     返回True以防止考虑此收集路径。在调用更具体的钩子之前，将为所有文件和目录查询该钩子
#     """
#     print("开始  10_4_2_pytest_ignore_collect")

# def pytest_collect_file(path, parent):
#     """
#     在遍历用于收集文件的目录之前调用
#     """
#     print("开始  11_4_3_pytest_collect_file")

# def pytest_pycollect_makemodule(path, parent):
#     """
#     返回给定路径的模块收集器或无。将为每个匹配的测试模块路径调用此挂钩。如果要为与测试模块不匹配的文件创建测试模块，则需要使用pytest_collect_file挂钩。
#     """
#     print("开始  12_4_4_pytest_pycollect_makemodule")

# def pytest_pycollect_makeitem(collector, name, obj):
#     """
#     返回模块中python对象的自定义项目/收集器，或者返回None。
#     """
#     print("开始  15_4_5_pytest_pycollect_makeitem")

# def pytest_generate_tests(metafunc):
#     """
#     生成对测试函数的（多个）参数化调用
#     """
#     metafunc.fixturenames=['hello']
#     print("开始  16_4_6_pytest_generate_tests")

# def pytest_collection_modifyitems(session, config, items):
#     """
#     在执行收集后调用，可能会在适当位置过滤或重新排序项目。
#
#     """
#     print("开始  18_4_7_pytest_collection_modifyitems")
#
# def pytest_collection_finish(session):
#     """在执行收集和修改之后调用"""
#     print("开始  20_4_8_pytest_collection_finish")

# def pytest_collect_directory(path, parent):
#     print("开始  pytest_collect_directory")

# def pytest_make_parametrize_id(config, val, argname):
#     """
#     返回给定val的用户友好字符串表示形式，它将由@ pytest.mark.parametrize调用使用。如果钩子不知道val，则返回None。如果需要，参数名称可以作为argname使用。
#     """
#     ...


#
# # # 5_Reporting hooks
# def pytest_report_header(config, startdir):
#     """
#       return a string or list of strings to be displayed as header info for terminal reporting.
#     暂时没有发现有价值的地方"""
#     print("开始  8_5_1_pytest_report_header")
#
# def pytest_collectstart(collector):
#     """
#     收集器开始收集
#     暂时没有发现有价值的地方
#     """
#     print("开始  13_5_2_pytest_collectstart")
#
# def pytest_make_collect_report(collector):
#     """
#     执行collector.collect（）并返回CollectReport。
#     暂时没有发现有价值的地方
#     """
#     print("开始 14_5_3_pytest_make_collect_report")
#
# def pytest_itemcollected(item):
#     """
#     we just collected a test item.
#     暂时没有发现有价值的地方
#     """
#     print("开始  17_5_4_pytest_itemcollected")
#
# def pytest_report_collectionfinish(config, startdir, items):
#     """
#     return a string or list of strings to be displayed after collection has finished successfully.
#     暂时没有发现有价值的地方"""
#     print("开始  19_5_5_pytest_report_collectionfinish")
#
# def pytest_report_teststatus(report, config):
#     """
#     return result-category, shortletter and verbose word for reporting.
#     这个是用例setup之后在第一行代码执行前执行的，
#     所以可以在这里获取用例的基本信息
#     觉得要比pytest_runtest_logstart 获取的信息更好完整一些
#     """
#     print("开始  26_5_6_pytest_report_teststatus")
#
# def pytest_runtest_logreport(report):
#     """
#     process a test setup/call/teardown report relating to the respective phase of executing a test.
#     作用不大暂时忽略
#     """
#     print("开始  27_5_7_pytest_runtest_logreport")
#
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
#
# def pytest_collectreport(report):
#     """
#       collector finished collecting.
#     1. 在一次执行多个用例时使用， 比如一个类多个测试方法，一个测试文件多个测试类等
#     2. 并且是在一行测试代码没有执行的时候执行的
#     3. 用来收集用例名称，并设置result字段，
#         如一个测试类有2个测试方法，就会在result中生成2个数据的list
#         如一个测试文件有2个测试类，每个测试类有2个测试方法，会执行两次上面的操作，
#             另外再生成一次将两个测试类组装起来
#     """
#     print("开始  pytest_collectreport")
#




# def pytest_assertrepr_compare(config, op, left, right):
#     """
#     只有使用到对象的的方法的时候才会进来，普通字符串是不会进来的
#     这个扩展我想应该是用户在自定义的时候才会使用到，
#     因为类对象的比较只有碰到实际业务才能确定，所以暂时不处理
#     """
#     print("1111开始  pytest_assertrepr_compare")

# def pytest_assertion_pass(item, lineno, orig, expl):
#     """
#     Experimental  New in version 5.0.
#      Hook called whenever an assertion passes
#      This hook must be explicitly enabled by the enable_assertion_pass_hook ini-file option
#     关系到assert，设置了断点但是没有跟踪进来，不知道什么原因，放在后面处理"""
#     print(f"lineno:{lineno}, orig:{orig}, expl:{expl}")
#     print("1111开始  pytest_assertion_pass")


# def pytest_deselected(items):
#     """
#       called for test items deselected, e.g. by keyword.
#     不知道怎么使用，暂时不处理
#     """
#     print("开始  pytest_deselected")
# def pytest_fixture_setup(fixturedef, request):
#     """
#         执行夹具设置执行。
#     关系到fixture，放到后面处理"""
#     print("开始  pytest_fixture_setup")
#
# def pytest_fixture_post_finalizer(fixturedef, request):
#     """
#     在设备拆除之后但在清除缓存之前调用，
#     关系到fixture，放到后面处理
#     """
#     print("开始  pytest_fixture_post_finalizer")

# def pytest_warning_captured(warning_message, when, item, location):
#         """这个报location错误，感觉用不到，所以不关注"""
#     print("开始  pytest_warning_captured")

# # 6_Debugging/Interaction hooks
# def pytest_internalerror(excrepr, excinfo):
#     ...

# def pytest_keyboard_interrupt(excinfo):
#     ...
#
# def pytest_exception_interact(node, call, report):
#     """
#     call.excinfo
#     report.nodeid
#     report.longrepr
#     """
#     print("pytest_exception_interact")
#
# def pytest_enter_pdb(config, pdb):
#     ..

