from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from Login.Login import login_smarty
from Dashboard.search_Dashboard_V2 import page_dashboard


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

        for i in range(2):
            print('ลูป 2 รอบ')
            page_dashboard(self.driver) # ตรวจสอบหน้า Pending
            if page_dashboard:
                print('Test Page Dashboard : Pass')
                print('--------------------------------')
            else:
                print('Fail')
                break
            pass

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dizny/Desktop/Smarty/1.Register'))