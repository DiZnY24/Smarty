from selenium import webdriver
import time
import unittest
import HtmlTestRunner

from Login.Login import login_smarty
from จัดการข่าวสาร.V2.Add_News_V2 import page_news
from จัดการข่าวสาร.V2.Add_News_Call_to_Action_V2 import add_call_to_action_v1
from จัดการข่าวสาร.V2.Add_News_Call_to_Action_V2_1 import add_call_to_action_v2

from จัดการข่าวสาร.V2.Edit_V2 import page_edit_news
from จัดการข่าวสาร.V2.Edit_Call_to_Action_V2 import page_edit_call_to_action_v1
from จัดการข่าวสาร.V2.Edit_Call_to_Action_V2_1 import page_edit_call_to_action_v2

from จัดการข่าวสาร.V2.delete_V2 import page_delete

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

#         page_news(self.driver) # ตรวจสอบหน้า news
#         if page_news:
#             print('Test Page News :',(True))
#             print('--------------------------------')
#         else:
#             print('Fail',(False))

#         page_edit_news(self.driver)
#         if page_edit_news:
#             print('Test Edit News :',(True))
#             print('--------------------------------')
#         else:
#             print('Fail',(False))

# # ----------------------------------------------------------------------

#         add_call_to_action_v1(self.driver)
#         if add_call_to_action_v1:
#             print('Test Add Call to Action 1 :',(True)) # เปิด Internal
#             print('--------------------------------')
#         else:
#             print('Fail',(False))

#         page_edit_call_to_action_v1(self.driver)
#         if page_edit_call_to_action_v1:
#             print('Test Add Call to Action 1 :',(True)) # เปิด  Internal
#             print('--------------------------------')
#         else:
#             print('Fail',(False))

# # ----------------------------------------------------------------------

        add_call_to_action_v2(self.driver)
        if add_call_to_action_v2:
            print('Test Add Call to Action 2 :',(True)) # เปิด External
            print('--------------------------------')
        else:
            print('Fail',(False))

        page_edit_call_to_action_v2(self.driver)
        if page_edit_call_to_action_v2:
            print('Test Edit Call to Action 2 :',(True)) # แก้ไข External
            print('--------------------------------')
        else:
            print('Fail',(False))
            

        # for i in range(2):
        #     print('Loop 2 ลบครั้ง')

        #     page_delete(self.driver)
        #     if page_delete:
        #         print('Test Delete :',(True))
        #     else:
        #         print ('Fail',(False))  
        

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dizny/Desktop/Smarty/1.Register'))