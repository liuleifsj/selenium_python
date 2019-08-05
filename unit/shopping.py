#-*- coding:utf-8 -*-
from selenium import webdriver
#导入类
from util import urlutli
#导入单元测试包
import unittest
#导入休眠包
import time
#导入鼠标包
from selenium.webdriver.common.action_chains import ActionChains

#定义一个类
class Shipping(unittest.TestCase):

      #测试用例执行之前，执行的方法
      def setUp(self):
        #打开浏览器
        self.driver = webdriver.Firefox()
        #设置网页最大化
        self.driver.maximize_window()
        #打开网页
        self.driver.get(urlutli.JD_MANI)
        #休眠五秒
        time.sleep(2)

        #查找控件
        self.key = self.driver.find_element_by_id("key")#输入框
        self.button = self.driver.find_element_by_class_name("button")#搜索按钮


        pass
      #测试用例执行之后，执行的方法
      def tearDown(self):
        time.sleep(2)
          #关闭当前界面
        self.driver.quit()
        pass

      #测试用例shopping
      def test_shop(self):
        # 输入内容
        self.key.send_keys(u"娃娃")
        self.button.click()
        time.sleep(2)

        # 获取控件
        self.m_list = self.driver.find_element_by_class_name("m-list")
        # 使用js定位
        self.driver.execute_script("arguments[0].scrollIntoView(true)", self.m_list)
        # 休眠5秒
        time.sleep(3)

        #获取当前界面
        self.spss = self.driver.current_window_handle
        #获取选购的商品控件id
        self.p_name_type_2 = self.driver.find_element_by_class_name("skcolor_ljg")
        self.p_name_type_2.click()
        time.sleep(3)

        #获取所有界面
        self.sy = self.driver.window_handles
        #切换界面
        for window in self.sy:
            if window != self.spss:
                self.driver.switch_to_window(window)
            #获取titel
        titel = self.driver.title
             #断言
        self.assertEqual(titel,u"新款大号泰迪熊公仔抱枕毛绒玩具布娃娃抱抱熊大熊猫狗熊玩偶靠垫靠枕生日礼物送女生 米白色款-丝带熊 1米【图片 价格 品牌 报价】-京东")
        time.sleep(3)

        #进入选中的商品界面后，选中商品的颜色
        self.yanshe = self.driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/div[4]/div[6]/div[1]/div[2]/div[2]/a")
        self.yanshe.click()
        time.sleep(3)

        #获取图片的集合
        self.tupian_list = self.driver.find_element_by_id("spec-list")
        #使用js定位，查看图片
        imp = self.driver.find_element_by_xpath("/html/body/div[7]/div/div[1]/div/div[2]/div/ul/li[2]/img")
        chain = ActionChains(self.driver)
        chain.move_to_element(imp).perform()
        time.sleep(2)

        imp2 = self.driver.find_element_by_xpath("/html/body/div[7]/div/div[1]/div/div[2]/div/ul/li[3]/img")
        chain.move_to_element(imp2).perform()
        time.sleep(2)
        #
        # imp3 = self.driver.find_element_by_xpath("/html/body/div[7]/div/div[1]/div/div[2]/div/ul/li[4]/img")
        # chain.move_to_element(imp3).perform()
        # time.sleep(2)
        #
        # imp4 = self.driver.find_element_by_xpath("/html/body/div[7]/div/div[1]/div/div[2]/div/ul/li[5]/img")
        # chain.move_to_element(imp4).perform()
        # time.sleep(2)
        #
        # imp5 = self.driver.find_element_by_xpath("/html/body/div[7]/div/div[1]/div/div[2]/div/ul/li[6]/img")
        # chain.move_to_element(imp5).perform()
        # time.sleep(2)

        #宽 width 高 height
        #获取当前几面的宽高
        # width = self.driver.get_window_size("width")
        # height = self.driver.get_window_size("height")

        # js = "var q=document.documentElement.scrollTop=0"
        # self.driver.execute_script(js)
        # for index in range(0, 10):
        #   js = "var q=document.documentElement.scrollTop=" + str(height * index)
        #   self.driver.execute_script(js)
        #   time.sleep(2)



        #获取三角形
        self.sprite_arrow_next = self.driver.find_element_by_class_name("sprite-arrow-next")
        self.sprite_arrow_next.click()
        time.sleep(2)

        self.tupian_list6 = self.driver.find_element_by_xpath("/html/body/div[7]/div/div[1]/div/div[2]/div/ul/li[6]/img")
        self.tupian_list6.click()
        time.sleep(3)

        # 获取购物数量+的id
        self.btn_add = self.driver.find_element_by_class_name("btn-add")
        self.btn_add.click()
        time.sleep(2)
        #获取购物数量-的id
        self.btn_reduce = self.driver.find_element_by_class_name("btn-reduce")
        self.btn_reduce.click()
        time.sleep(2)

        #点击加入购物车
        self.InitCartUrl = self.driver.find_element_by_id("InitCartUrl")
        self.InitCartUrl.click()
        time.sleep(2)

        #获取当前界面
        self.jz = self.driver.current_window_handle

        #查找控件
        self.btn_tobback = self.driver.find_element_by_class_name("btn-tobback")
        self.btn_tobback.click()
        time.sleep(2)

        #返回界面
        self.driver.back()
        time.sleep(3)
        pass
if __name__ == '__main__':
        unittest.main()