#-*- coding:utf-8 -*-
#导包
from selenium import webdriver
#导入单元测试包
import unittest
#导包
from util import urlutli
#休眠包
import time

from PIL import Image

#定义一个继承单元测试的类
class Login(unittest.TestCase):

     #测试用例执行前，执行的方法
     def setUp(self):
         self.driver = webdriver.Firefox()
         #窗口最大化
         self.driver.maximize_window()
         #制定打开的网页
         self.driver.get(urlutli.JD_LONGIN+urlutli.LONGIN)
         #休眠5秒
         time.sleep(5)
         #获取当前账号登录界面
         self.login_tab_r = self.driver.find_element_by_class_name("login-tab-r")
         #点击一下账号登录界面
         self.login_tab_r.click()

         #开始查找控件
         self.loginname = self.driver.find_element_by_id("loginname")#账号
         self.nloginpwd = self.driver.find_element_by_id("nloginpwd")#密码
         self.loginsubmit = self.driver.find_element_by_id("loginsubmit")#登录按钮
         pass

     #测试用例执行后，执行的用例
     def tearDown(self):
         #关闭当前界面
         self.driver.quit()
         pass

     #测试用例登录-输入准确的账号密码
     def test_us_pa_su(self):
         u"""输入准确的账号密码"""
         #输入账号和密码并点击登录
         self.loginname.send_keys("15210033534")
         self.nloginpwd.send_keys("ww970614")
         self.loginsubmit.click()
         #休眠5秒
         time.sleep(5)

         title = self.driver.title

         #进行断言
         self.assertEqual(title,u"京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！")
         pass

         #测试用例登录-不输入账号
     def test_us_pa_ti(self):
         u"""不输入账号密码"""
         #输入账号和密码并点击登录
         self.loginname.send_keys("")
         self.nloginpwd.send_keys("")
         self.loginsubmit.click()
         #休眠5秒
         time.sleep(5)

         #获取提示内容
         self.msg_error = self.driver.find_element_by_class_name("msg-error")

         username = self.msg_error.text
         #进行断言
         self.assertEqual(username,u"请输入账户名和密码")
         pass
     #测试用例登录-不输入密码
     def test_us_pa_tw(self):
         u"""不输入密码"""
         #输入账号和密码并点击登录
         self.loginname.send_keys("13591026846")
         self.nloginpwd.send_keys("")
         self.loginsubmit.click()
         #休眠5秒
         time.sleep(5)

         #获取提示内容
         self.msg_error = self.driver.find_element_by_class_name("msg-error")

         password = self.msg_error.text
         #进行断言
         self.assertEqual(password,u"请输入密码")
         pass

         # 测试用例登录-输入错误的账号
     def test_us_pa_tq(self):
             u"""输入错误的账号"""
             # 输入账号和密码并点击登录
             self.loginname.send_keys("152100335341")
             self.nloginpwd.send_keys("")
             self.loginsubmit.click()
             # 休眠5秒
             time.sleep(5)

             # 获取提示内容
             self.msg_error = self.driver.find_element_by_class_name("msg-error")

             nopassword = self.msg_error.text
             # 进行断言
             self.assertEqual(nopassword, u"账户名不存在，请重新输入")
             pass

        # 测试用例登录-输入错误的密码
     def test_us_pa_te(self):
             u"""输入错误的密码"""
             # 输入账号和密码并点击登录
             self.loginname.send_keys("152100335341")
             self.nloginpwd.send_keys("awds123")
             self.loginsubmit.click()
             # 休眠5秒
             time.sleep(5)

             # 获取提示内容
             self.msg_error = self.driver.find_element_by_class_name("msg-error")

             nousername = self.msg_error.text
             # 进行断言
             self.assertEqual(nousername, u"如需海外手机登录请添加 国际区号")
             pass

     def test_logo_jd(self):
         u"""点击京东图标"""
         login = self.driver.current_window_handle

         #获取控件
         self.logo = self.driver.find_element_by_id("logo")
         self.logo.click()
         time.sleep(3)

         logins = self.driver.window_handles
         for jd in logins:
             if jd != login:
                 self.driver.switch_to_window(jd)

             title = self.driver.title
         self.assertEqual(title,u"京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！")
         pass
     def test_jd_ys(self):
         u"""点击京东隐私政策"""
         #获取当前界面 ()
         ys = self.driver.current_window_handle
         #查找控件
         self.ys = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/p/a")
         self.ys.click()
         time.sleep(5)

         #获取所有界面
         ys1 = self.driver.window_handles
         #切换页面
         for windo in ys1:
             if windo != ys:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"京东隐私政策")
         pass

     def test_jd_dc(self):
         u"""点击登录界面调查访问"""
         #获取当前界面 ()
         dc= self.driver.current_window_handle
         #查找控件
         self.dc = self.driver.find_element_by_class_name("q-link")
         self.dc.click()
         time.sleep(5)

         #获取所有界面
         dc1 = self.driver.window_handles
         #切换页面
         for windo in dc1:
             if windo != dc:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"登录页满意度调查")
         pass

     def test_jd_qq(self):
         u"""点击QQ登录"""
         #获取当前界面 ()
         qq= self.driver.current_window_handle
         #查找控件
         self.qq = self.driver.find_element_by_class_name("pdl")
         self.qq.click()
         time.sleep(5)

         #获取所有界面
         qq1 = self.driver.window_handles
         #切换页面
         for windo in qq1:
             if windo != qq:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"QQ帐号安全登录")
         pass

     def test_jd_wx(self):
         u"""点击微信登录"""
         #获取当前界面 ()
         wx= self.driver.current_window_handle
         #查找控件
         self.wx = self.driver.find_element_by_class_name("weixin-icon")
         self.wx.click()
         time.sleep(5)

         #获取所有界面
         wx1 = self.driver.window_handles
         #切换页面
         for windo in wx1:
             if windo != wx:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"微信登录")
         pass

     def test_jd_sm(self):
         u"""点击扫码登录"""
         #获取当前界面 ()
         self.sm = self.driver.current_window_handle
         #查找控件
         self.sjjd = self.driver.find_element_by_link_text("手机京东")
         self.sjjd.click()
         time.sleep(5)

         #获取所有界面
         login_sm = self.driver.window_handles
         #切换页面
         for windo in login_sm:
             if windo != self.sm:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"手机京东 - 京东")
         pass

     def test_jd_gywm(self):
         u"""点击关于我们"""
         #获取当前界面 ()
         self.gywm = self.driver.current_window_handle
         #查找控件
         self.gywm = self.driver.find_element_by_link_text("关于我们")
         self.gywm.click()
         time.sleep(5)

         #获取所有界面
         gywm1 = self.driver.window_handles
         #切换页面
         for windo in gywm1:
             if windo != self.gywm:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"企业简介-京东商城")
         pass

     def test_jd_lxwm(self):
         u"""点击联系我们"""
         #获取当前界面 ()
         self.lxwm = self.driver.current_window_handle
         #查找控件
         self.gywm = self.driver.find_element_by_link_text("联系我们")
         self.gywm.click()
         time.sleep(5)

         #获取所有界面
         lxwm1 = self.driver.window_handles
         #切换页面
         for windo in lxwm1:
             if windo != self.lxwm:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"联系我们-京东商城")
         pass

     def test_jd_rczp(self):
         u"""点击人才招聘"""
         #获取当前界面 ()
         self.rczp = self.driver.current_window_handle
         #查找控件
         self.rczp = self.driver.find_element_by_link_text("人才招聘")
         self.rczp.click()
         time.sleep(5)

         #获取所有界面
         rczp1 = self.driver.window_handles
         #切换页面
         for windo in rczp1:
             if windo != self.rczp:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"京东招聘官网")
         pass

     def test_jd_xjrz(self):
         u"""点击商家入驻"""
         #获取当前界面 ()
         self.sjrz = self.driver.current_window_handle
         #查找控件
         self.sjrz = self.driver.find_element_by_link_text("商家入驻")
         self.sjrz.click()
         time.sleep(5)

         #获取所有界面
         sjrz1 = self.driver.window_handles
         #切换页面
         for windo in sjrz1:
             if windo != self.sjrz:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"商家入驻-入驻流程 - 京东全品类专题活动-京东")
         pass

     def test_jd_ggfw(self):
         u"""点击广告服务"""
         #获取当前界面 ()
         self.ggfw = self.driver.current_window_handle
         #查找控件
         self.ggfw = self.driver.find_element_by_link_text("广告服务")
         self.ggfw.click()
         time.sleep(5)

         #获取所有界面
         ggfw1 = self.driver.window_handles
         #切换页面
         for windo in ggfw1:
             if windo != self.ggfw:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"广告服务 - 京东全品类专题活动-京东")
         pass

     def test_jd_sjjd1(self):
         u"""点击手机京东"""
         #获取当前界面 ()
         self.sjjd = self.driver.current_window_handle
         #查找控件
         self.sjjd = self.driver.find_element_by_link_text("手机京东")
         self.sjjd.click()
         time.sleep(5)

         #获取所有界面
         sjjd1 = self.driver.window_handles
         #切换页面
         for windo in sjjd1:
             if windo != self.sjjd:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"手机京东 - 京东")
         pass

     def test_jd_yqlj(self):
         u"""点击友情链接"""
         #获取当前界面 ()
         self.yqlj = self.driver.current_window_handle
         #查找控件
         self.yqlj = self.driver.find_element_by_link_text("友情链接")
         self.yqlj.click()
         time.sleep(5)

         #获取所有界面
         yqlj1 = self.driver.window_handles
         #切换页面
         for windo in yqlj1:
             if windo != self.yqlj:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"友情链接")
         pass

     def test_jd_xslm(self):
         u"""点击销售联盟"""
         #获取当前界面 ()
         self.xslm = self.driver.current_window_handle
         #查找控件
         self.xslm = self.driver.find_element_by_link_text("销售联盟")
         self.xslm.click()
         time.sleep(5)

         #获取所有界面
         xslm1 = self.driver.window_handles
         #切换页面
         for windo in xslm1:
             if windo != self.xslm:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"京东联盟")
         pass

     def test_jd_jdsq(self):
         u"""点击京东社区"""
         #获取当前界面 ()
         self.jdsq = self.driver.current_window_handle
         #查找控件
         self.jdsq = self.driver.find_element_by_link_text("京东社区")
         self.jdsq.click()
         time.sleep(5)

         #获取所有界面
         jdsq1 = self.driver.window_handles
         #切换页面
         for windo in jdsq1:
             if windo != self.jdsq:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"京东社区 - 京东电脑、办公|游戏设备专题活动-京东")
         pass

     def test_jd_jdgy(self):
         u"""点击京东公益"""
         #获取当前界面 ()
         self.jdgy = self.driver.current_window_handle
         #查找控件
         self.jdgy = self.driver.find_element_by_link_text("京东公益")
         self.jdgy.click()
         time.sleep(5)

         #获取所有界面
         jdgy1 = self.driver.window_handles
         #切换页面
         for windo in jdgy1:
             if windo != self.jdgy:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"京东公益")
         pass

     def test_jd_englishsite(self):
         u"""点击EngliShsite"""
         #获取当前界面 ()
         self.englishsite = self.driver.current_window_handle
         #查找控件
         self.englishsite = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/a[11]")
         self.englishsite.click()
         time.sleep(5)

         #获取所有界面
         englishsite1 = self.driver.window_handles
         #切换页面
         for windo in englishsite1:
             if windo != self.englishsite:
                 self.driver.switch_to_window(windo)
         title = self.driver.title
              #断言
         self.assertEqual(title,"JD.com Global Online Shopping Site: Online Shopping for Electronics, Clothing, Toys and More")
         pass