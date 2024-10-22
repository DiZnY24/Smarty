from selenium import webdriver
import time
import unittest
import HtmlTestRunner

from Login.Login import login_smarty

# TC_1_บริหารลูกบ้าน
from V2.TC_1_บริหารลูกบ้าน.Search_residents_V2 import test_page_Resident

# TC_2_บริหารผู้ใช้งาน
from V2.TC_2_บริหารผู้ใช้งาน.User_management_V2 import test_page_User
from V2.TC_2_บริหารผู้ใช้งาน.search_V2 import test_page_search
from V2.TC_2_บริหารผู้ใช้งาน.Edit_V2 import test_page_edit

# TC_3_บริหารลูกหนี้
from V2.TC_3.เพิ่มลูกหนี้ import test_page_add_debtor
from V2.TC_3.สร้างใบปลอดหนี้แบบมีเงื่อนไข import test_page_create
from V2.TC_3.debt_free import test_page_debt_free
from V2.TC_3.search_Edit import test_page_search_edit

# TC_4_บริหารโครงการ
from V2.TC_4.Add_รายละเอียด import test_page_add_bank1
from V2.TC_4.Add_ธนาคาร import test_page_add_bank2
from V2.TC_4.search import test_page_search1
from V2.TC_4.Edit import test_page_edit1
from V2.TC_4.Detele import test_page_delete

# TC_5_บริหารห้อง
from V2.TC_5.Add_เพิ่มห้อง import test_page_add_room
from V2.TC_5.search import test_page_search_room
from V2.TC_5.Edit import test_page_edit_room
from V2.TC_5.Detele import test_page_delete_room

# TC_6_บริหารมิเตอร์น้ำ
from V2.TC_6.add_water_meter import test_page_add_water_meter
from V2.TC_6.search_Edit_QR_เช็คมิเตอร์_Delete import test_page_search_edit1




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

        # TC_1_บริหารลูกบ้าน

        # test_page_Resident(self.driver) # ตรวจสอบหน้า บริหารลูกบ้าน
        # if test_page_Resident:
        #     print('Test resident :',(True))
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

# ----------------------------------------------------------------------

        # TC_2_บริหารผู้ใช้งาน
        
        # test_page_User(self.driver) # ตรวจสอบหน้า Add User
        # if test_page_User:
        #     print('Test User Already :',(True))
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

        # test_page_search(self.driver) # ตรวจสอบ การผู้ใช้งาน
        # if test_page_search:
        #     print('Test User Already :',(True))
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

        # test_page_edit(self.driver) # ตรวจสอบหน้า Edit 
        # if test_page_edit:
        #     print('Test edit Already :',(True))
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))


# ----------------------------------------------------------------------

        # TC_3_บริหารลูกหนี้

        # test_page_add_debtor(self.driver)
        # if test_page_add_debtor:
        #     print('Test Add Debtor Already:',(True)) # ตรวจสอบการ การเพิ่มลูกหนี้
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

        # test_page_search_edit(self.driver)
        # if test_page_search_edit:
        #     print('Test Search Edit Already :',(True)) # ตรวจสอบการ การค้นหาเมื่อสร้างแล้ว และ สร้างใบปลอดหนี้แบบปกติ
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

        # test_page_create(self.driver)
        # if test_page_create:
        #     print('Test check Create Already:',(True)) # ตรวจสอบการ สร้างใบปลอดหนี้แบบมีเงื่อนไข
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

        # test_page_debt_free(self.driver)
        # if test_page_debt_free:
        #     print('Test Debt Free Already:',(True)) # ตรวจสอบการ ส่วนของหน้าใบปลอดหนี้
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

# ----------------------------------------------------------------------

        # TC_4_บริหารโครงการ
        
        # test_page_add_bank1(self.driver)
        # if test_page_add_bank1:
        #     print('Test bank1  Already :',(True)) # ตรวจสอบการ เพิ่มโครงการ แบบรายละเอียด
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

        # test_page_add_bank2(self.driver)
        # if test_page_add_bank2:
        #     print('Test bank2  Already :',(True)) # ตรวจสอบการ เพิ่มโครงการ แบบบัญชีธนาคาร
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

        # test_page_search1(self.driver)
        # if test_page_search1:
        #     print('Test search  Already :',(True)) # ตรวจสอบการ ค้นหา โครงการที่สร้าง
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

        # test_page_edit1(self.driver)
        # if test_page_edit1:
        #     print('Test edit  Already :',(True)) # ตรวจสอบการ แก้ไข
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

        # test_page_delete(self.driver)
        # if test_page_delete:
        #     print('Test delete  Already :',(True)) # ตรวจสอบการ ลบโครงการ
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

# ----------------------------------------------------------------------

        # TC_5_บริหารห้อง

        # test_page_add_room(self.driver)
        # if test_page_add_room:
        #     print('Test Add Room  Already :',(True)) # ตรวจสอบการ การเพิ่มห้อง
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

        # test_page_search_room(self.driver)
        # if test_page_search_room:
        #     print('Test Participants  Already :',(True)) # ตรวจสอบการ ค้นหาห้อง
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

        # test_page_edit_room(self.driver)
        # if test_page_edit_room:
        #     print('Test print  Already :',(True)) # ตรวจสอบการ แก้ไขห้อง
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

        # test_page_delete_room(self.driver)
        # if test_page_delete_room:
        #     print('Test delete room  Already :',(True)) # ตรวจสอบการ การพิมเอกสารออกมา pdf
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

# ----------------------------------------------------------------------

        # TC_6_บริหารมิเตอร์น้ำ

        # test_page_add_water_meter(self.driver)
        # if test_page_add_water_meter:
        #     print('Test Add Water Meter  Already :',(True)) # ตรวจสอบการ เพิ่มมิเตอร์น้ำ
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

        # test_page_search_edit1(self.driver)
        # if test_page_search_edit1:
        #     print('Test Search Edit  Already :',(True)) # ตรวจสอบการ ค้นหารายชื่อ พร้อมแก้ไข ไปพร้อมกัน
        #     print('--------------------------------')
        # else:
        #     self.fail('Fail',(False))

# ----------------------------------------------------------------------


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dizny/Desktop/Smarty/1.Register'))