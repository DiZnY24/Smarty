from selenium import webdriver
import unittest
import HtmlTestRunner

from Login.Login import login_smarty


from V2.TC_1.สร้างใบเตือนรายบุคคล import test_page_create_warning1
from V2.TC_1.สร้างใบเตือนรายโครงการ import test_page_create_warning

from V2.TC_2.search_Edit import test_page_search_edit

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


        test_page_create_warning1(self.driver) # ตรวจสอบหน้า สร้างใบเตือนรายบุคคล
        if test_page_create_warning1:
            print('Test Create Warning Already :',(True))
            print('--------------------------------')
        else:
            self.fail('Fail',(False))

        test_page_create_warning(self.driver) # ตรวจสอบหน้า สร้างใบเตือนรายโครงการ
        if test_page_create_warning:
            print('Test Create Warning1 Already :',(True))
            print('--------------------------------')
        else:
            self.fail('Fail',(False))

        test_page_search_edit(self.driver) # ตรวจสอบหน้า ค้นหาพร้อมแก้ไข
        if test_page_search_edit:
            print('Test Search Edit Already :',(True))
            print('--------------------------------')
        else:
            self.fail('Fail',(False))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dizny/Desktop/Smarty/1.Register'))