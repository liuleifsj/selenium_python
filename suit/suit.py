#-*- coding:utf-8 -*-
#导入单元测试包
import unittest

from unit import login,shopping
#导入自动化测试报告
import HTMLTestRunner

#设置系统编码格式
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#实例化套件
suit = unittest.TestSuite()
#将单元测试加入测试套件里面
suit.addTest(unittest.makeSuite(login.Login))
# suit.addTest(unittest.makeSuite(shopping.Shipping))
#指定自动化测试报告的路径
filename = "D://jdwb.html"
#指定流的读写模式
output = open(filename,'wb')
#运行自动化测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=output,title="京东登录模块",description="登录测试用例")
runner.run(suit)
