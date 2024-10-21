from selenium import webdriver
import time
import unittest
import HtmlTestRunner

from Login.Login import login_smarty

from จัดการแบนเนอร์.V2.Add_Banner_V2 import add_banner
from จัดการแบนเนอร์.V2.Edit_Banner_V2 import page_edit_banner

from จัดการแบนเนอร์.V2.Add_Banner_Call_to_Action_V2 import add_banner_call_to_action_v1
from จัดการแบนเนอร์.V2.Edit_Banner_Call_to_Action_V2 import page_edit_banner_call_to_action_v1

from จัดการแบนเนอร์.V2.Add_Banner_Call_to_Action_V2_1 import add_banner_call_to_action_v2
from จัดการแบนเนอร์.V2.Edit_Banner_Call_to_Action_V2_1 import page_edit_banner_call_to_action_v2

from จัดการแบนเนอร์.V2.Delete_Banner_V2 import check_delete

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

        add_banner(self.driver) # ตรวจสอบหน้า สร้างแอดแบนเนอร์ 

        if add_banner:
            print('Test Add Banner :',(True))
            print('--------------------------------')
        else:
            print('Fail',(False))

        page_edit_banner(self.driver) # ตรวจสอบหน้า แก้ไขแบนเนอร์
        if page_edit_banner:
            print('Test Edit Banner :',(True))
            print('--------------------------------')
        else:
            print('Fail',(False))


# ----------------------------------------------------------------------------------------------------------------
        
        add_banner_call_to_action_v1(self.driver) # ตรวจสอบหน้า การเพิ่ม  Banner - Internal
        if add_banner:
            print('Test Add Banner call to action 1 :',(True))
            print('--------------------------------')
        else:
            print('Fail',(False))
        
        page_edit_banner_call_to_action_v2(self.driver) # ตรวจสอบหน้า External
        if page_edit_banner_call_to_action_v2:
            print('Test Edit Banner call to action 2 :',(True))
            print('--------------------------------')
        else:
            print('Fail',(False))
        
# ----------------------------------------------------------------------------------------------------------------
  
        add_banner_call_to_action_v2(self.driver) # ตรวจสอบหน้า External
        if add_banner:
            print('Test Add Banner call to action 2 :',(True))
            print('--------------------------------')
        else:
            print('Fail',(False))

        page_edit_banner_call_to_action_v1(self.driver) # ตรวจสอบหน้า Internal
        if page_edit_banner_call_to_action_v1:
            print('Test Edit Banner call to action 1 :',(True))
            print('--------------------------------')
        else:
            print('Fail',(False))
        
# ----------------------------------------------------------------------------------------------------------------

        # for i in range(4):
        # check_delete(self.driver) # ตรวจสอบการ ลบ แบนเนอร์
        # if check_delete:
        #     print('Test Delete :',(True))
        #     print('--------------------------------')
        # else:
        #     print('Fail',(False))
                # break


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dizny/Desktop/Smarty/1.Register'))