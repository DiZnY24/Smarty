from selenium import webdriver
import time
import unittest
import HtmlTestRunner

from Login.Login import login_smarty
from TC_1_ตั้งค่าปีจัดประชุม.V2.Add_year_V2 import page_year
from TC_1_ตั้งค่าปีจัดประชุม.V2.Edit_year_V2 import page_edit_year
from TC_2_จัดการการประชุม.V2.Add_meeting_V2 import page_meeting
from TC_2_จัดการการประชุม.V2.Search_meeting_V2 import page_search
from TC_2_จัดการการประชุม.V2.Edit_meeting_V2 import page_edit_meeting
from TC_2_จัดการการประชุม.V2.Check_in_V2 import page_check_in
from TC_2_จัดการการประชุม.V2.Participants_V2 import page_participants
from TC_2_จัดการการประชุม.V2.print_document_V2 import page_print

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

        # TC_1_ตั้งค่าปีจัดประชุม

        # page_year(self.driver) # ตรวจสอบหน้า Year 
        # if page_year:
        #     print('Test Page Year :',(True))
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

        # page_edit_year(self.driver) # ตรวจสอบหน้า Edit Year
        # if page_edit_year:
        #     print('Test Edit Year Already :',(True))
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

# ----------------------------------------------------------------------

        # TC_2_จัดการการประชุม

        page_meeting(self.driver)
        if page_meeting:
            print('Test Meeting Already:',(True)) # ตรวจสอบการ สร้างวาระ
            print('--------------------------------')
        else:
            self.fail('Fail',(False))

        page_search(self.driver)
        if page_search:
            print('Test Search Already :',(True)) # ตรวจสอบการ การค้นหาเมื่อสร้างแล้ว
            print('--------------------------------')
        else:
            self.fail('Fail',(False))

        page_edit_meeting(self.driver)
        if page_edit_meeting:
            print('Test Edit Already:',(True)) # ตรวจสอบการ สร้างวาระ
            print('--------------------------------')
        else:
            self.fail('Fail',(False))

        page_check_in(self.driver)
        if page_check_in:
            print('Test Check in  Already :',(True)) # ตรวจสอบการ หน้าของการลงทะเบียนเช็คอิน
            print('--------------------------------')
        else:
            self.fail('Fail',(False))

        page_participants(self.driver)
        if page_participants:
            print('Test Participants  Already :',(True)) # ตรวจสอบการ จัดการผู้เข้าร่วม
            print('--------------------------------')
        else:
            self.fail('Fail',(False))

        page_print(self.driver)
        if page_print:
            print('Test print  Already :',(True)) # ตรวจสอบการ การพิมเอกสารออกมา pdf
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