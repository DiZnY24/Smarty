from selenium import webdriver
import time
import unittest
import HtmlTestRunner

from Login.Login import login_smarty

# TC_1_บริหารลูกบ้าน
from V2.TC_1.Add import test_page_add_invoice
from V2.TC_2.search_Edit import test_page_search_edit
from V2.TC_3.Edit import test_page_staus_edit




class WebTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get('https://msm-smarty-cms-staging.hr-impact.co/login')
        cls.driver.set_window_size(1600, 1000)
        cls.driver.implicitly_wait(30)

    def test_all_smarty(self):                                                    
        
        login_smarty(self.driver) # การล็อกอินหน้าเว็ป
        if login_smarty:
            print('Test Login Smarty :',(True))
            print('--------------------------------')
        else:
            self.fail('Fail', (False))


        # test_page_add_invoice(self.driver) # ตรวจสอบหน้า เพิ่มใบแจ้งหนี้
        # if test_page_add_invoice:
        #     print('Test Add Invoice Already :',(True))
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))


        # test_page_search_edit(self.driver) # ตรวจสอบหน้า ค้นหาพร้อมแก้ไข ใบแจ้งหนี้
        # if test_page_search_edit:
        #     print('Test serach Edit Already :',(True))
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))


        test_page_staus_edit(self.driver) # ตรวจสอบหน้า บริหารลูกบ้าน
        if test_page_staus_edit:
            print('Test resident :',(True))
            print('--------------------------------')
        else:
            self.fail('Fail',(False))






    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dizny/Desktop/Smarty/1.Register'))