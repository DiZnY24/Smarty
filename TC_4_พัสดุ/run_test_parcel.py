from selenium import webdriver
import time
import unittest
import HtmlTestRunner

from Login.Login import login_smarty
from TC_1_จัดการพัสดุ.V2.Add_parcel_V2 import page_parcel
from TC_1_จัดการพัสดุ.V2.search_Parcel_V2 import page_search
from TC_2_จัดการขนส่ง.V2.Add_transportation_V2 import page_transport
from TC_2_จัดการขนส่ง.V2.delete_V2 import page_dalete

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
            print('Fail', (False))

        # TC_1_จัดการพัสดุ

        # page_parcel(self.driver) # ตรวจสอบหน้า parcel
        # if page_parcel:
        #     print('Test Page parcel :',(True))
        #     print('--------------------------------')
        # else:
        #     print('Fail',(False))

        # page_search(self.driver)
        # if page_search:
        #     print('Test search parcel :',(True))
        #     print('--------------------------------')
        # else:
        #     print('Fail',(False))

# ----------------------------------------------------------------------

        # TC_2_จัดการขนส่ง

        # page_transport(self.driver)
        # if page_transport:
        #     print('Test Transport Already:',(True)) # ตรวจสอบการ สร้างปีเพิ่ม
        #     print('--------------------------------')
        # else:
        #     print('Fail',(False))

        page_dalete(self.driver)
        if page_dalete:
            print('Test Delete Already :',(True)) # ตรวจสอบการ Test delere
            print('--------------------------------')
        else:
            print('Fail',(False))

# ----------------------------------------------------------------------

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dizny/Desktop/Smarty/1.Register'))