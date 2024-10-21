from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from TC_1_Register.Login.Login import login_smarty 
# from Pending.search_Pending_V2 import page_pending
# from Approved.search_Approved_V2 import page_approved
# from Rejected.search_Rejected_V2 import page_rejected 


class WebTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get('https://msm-smarty-cms-staging.hr-impact.co/login')
        cls.driver.set_window_size(1600, 1000)
        cls.driver.implicitly_wait(15)

    def test_search_openai(self):

        login_smarty(self.driver) # การล็อกอินหน้าเว็ป
        if login_smarty:
            print('Test Login Smarty : Pass')
            print('--------------------------------')
        else:
            print('Fail')

        # page_pending(self.driver) # ตรวจสอบหน้า Pending
        # if page_pending:
        #     print('Test Page Pending : Pass')
        #     print('--------------------------------')
        # else:
        #     print('Fail')

        # page_approved(self.driver)
        # if page_approved:
        #     print('Test Page Approved : Pass')
        #     print('--------------------------------')
        # else:
        #     print('Fail')
        
        # page_rejected(self.driver)
        # if page_rejected:
        #     print('Test Page Rejected : Pass')
        # else:
        #     print('Fail')
        
        # คุณสามารถเพิ่มการตรวจสอบผลลัพธ์ที่นี่ เช่น assertIn

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dizny/Desktop/Smarty/1.Register'))