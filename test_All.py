from selenium import webdriver
import time
import unittest
import HtmlTestRunner

# TC_1_Register

from TC_1_Register.Login.Login import login_smarty 
from TC_1_Register.Approved.search_Approved_V2 import page_approved
from TC_1_Register.Pending.search_Pending_V2 import page_pending
from TC_1_Register.Rejected.search_Rejected_V2 import page_rejected

# TC_2_Dashboard

from TC_2_Dashboard.Dashboard.search_Dashboard_V2 import page_dashboard

# TC_3_ข่าวสาร

# จัดการข่าวสาร
from TC_3_ข่าวสาร.จัดการข่าวสาร.V2.Add_News_V2 import page_news
from TC_3_ข่าวสาร.จัดการข่าวสาร.V2.Add_News_Call_to_Action_V2 import add_call_to_action_v1
from TC_3_ข่าวสาร.จัดการข่าวสาร.V2.Add_News_Call_to_Action_V2_1 import add_call_to_action_v2

from TC_3_ข่าวสาร.จัดการข่าวสาร.V2.Edit_V2 import page_edit_news
from TC_3_ข่าวสาร.จัดการข่าวสาร.V2.Edit_Call_to_Action_V2 import page_edit_call_to_action_v1
from TC_3_ข่าวสาร.จัดการข่าวสาร.V2.Edit_Call_to_Action_V2_1 import page_edit_call_to_action_v2

from TC_3_ข่าวสาร.จัดการข่าวสาร.V2.delete_V2 import page_delete

# จัดการแบนเนอร์
from TC_3_ข่าวสาร.จัดการแบนเนอร์.V2.Add_Banner_V2 import add_banner
from TC_3_ข่าวสาร.จัดการแบนเนอร์.V2.Edit_Banner_V2 import page_edit_banner

from TC_3_ข่าวสาร.จัดการแบนเนอร์.V2.Add_Banner_Call_to_Action_V2 import add_banner_call_to_action_v1
from TC_3_ข่าวสาร.จัดการแบนเนอร์.V2.Edit_Banner_Call_to_Action_V2 import page_edit_banner_call_to_action_v1

from TC_3_ข่าวสาร.จัดการแบนเนอร์.V2.Add_Banner_Call_to_Action_V2_1 import add_banner_call_to_action_v2
from TC_3_ข่าวสาร.จัดการแบนเนอร์.V2.Edit_Banner_Call_to_Action_V2_1 import page_edit_banner_call_to_action_v2

from TC_3_ข่าวสาร.จัดการแบนเนอร์.V2.Delete_Banner_V2 import check_delete


# TC_4_พัสดุ

from TC_4_พัสดุ.TC_1_จัดการพัสดุ.V2.Add_parcel_V2 import page_parcel
from TC_4_พัสดุ.TC_1_จัดการพัสดุ.V2.search_Parcel_V2 import page_search
from TC_4_พัสดุ.TC_2_จัดการขนส่ง.V2.Add_transportation_V2 import page_transport
from TC_4_พัสดุ.TC_2_จัดการขนส่ง.V2.delete_V2 import page_dalete

# TC_5_การประชุมลูกบ้าน

from TC_5_การประชุมลูกบ้าน.TC_1_ตั้งค่าปีจัดประชุม.V2.Add_year_V2 import page_year
from TC_5_การประชุมลูกบ้าน.TC_1_ตั้งค่าปีจัดประชุม.V2.Edit_year_V2 import page_edit_year
from TC_5_การประชุมลูกบ้าน.TC_2_จัดการการประชุม.V2.Add_meeting_V2 import page_meeting
from TC_5_การประชุมลูกบ้าน.TC_2_จัดการการประชุม.V2.Search_meeting_V2 import page_search
from TC_5_การประชุมลูกบ้าน.TC_2_จัดการการประชุม.V2.Edit_meeting_V2 import page_edit_meeting
from TC_5_การประชุมลูกบ้าน.TC_2_จัดการการประชุม.V2.Check_in_V2 import page_check_in
from TC_5_การประชุมลูกบ้าน.TC_2_จัดการการประชุม.V2.Participants_V2 import page_participants
from TC_5_การประชุมลูกบ้าน.TC_2_จัดการการประชุม.V2.print_document_V2 import page_print

# TC_6_การบริหาร

# TC_1_บริหารลูกบ้าน
from TC_6_การบริหาร.V2.TC_1_บริหารลูกบ้าน.Search_residents_V2 import test_page_Resident

# TC_2_บริหารผู้ใช้งาน
from TC_6_การบริหาร.V2.TC_2_บริหารผู้ใช้งาน.User_management_V2 import test_page_User
from TC_6_การบริหาร.V2.TC_2_บริหารผู้ใช้งาน.search_V2 import test_page_search
from TC_6_การบริหาร.V2.TC_2_บริหารผู้ใช้งาน.Edit_V2 import test_page_edit

# TC_3_บริหารลูกหนี้
from TC_6_การบริหาร.V2.TC_3.เพิ่มลูกหนี้ import test_page_add_debtor
from TC_6_การบริหาร.V2.TC_3.สร้างใบปลอดหนี้แบบมีเงื่อนไข import test_page_create
from TC_6_การบริหาร.V2.TC_3.debt_free import test_page_debt_free
from TC_6_การบริหาร.V2.TC_3.search_Edit import test_page_search_edit

# TC_4_บริหารโครงการ
from TC_6_การบริหาร.V2.TC_4.Add_รายละเอียด import test_page_add_bank1
from TC_6_การบริหาร.V2.TC_4.Add_ธนาคาร import test_page_add_bank2
from TC_6_การบริหาร.V2.TC_4.search import test_page_search1
from TC_6_การบริหาร.V2.TC_4.Edit import test_page_edit1
from TC_6_การบริหาร.V2.TC_4.Detele import test_page_delete

# TC_5_บริหารห้อง
from TC_6_การบริหาร.V2.TC_5.Add_เพิ่มห้อง import test_page_add_room
from TC_6_การบริหาร.V2.TC_5.search import test_page_search_room
from TC_6_การบริหาร.V2.TC_5.Edit import test_page_edit_room
from TC_6_การบริหาร.V2.TC_5.Detele import test_page_delete_room

# TC_6_บริหารมิเตอร์น้ำ
from TC_6_การบริหาร.V2.TC_6.add_water_meter import test_page_add_water_meter
from TC_6_การบริหาร.V2.TC_6.search_Edit_QR_เช็คมิเตอร์_Delete import test_page_search_edit1


# TC_7_ใบแจ้งหนี้

# TC_1_บริหารลูกบ้าน
from TC_7_ใบแจ้งหนี้.V2.TC_1.Add import test_page_add_invoice
from TC_7_ใบแจ้งหนี้.V2.TC_2.search_Edit import test_page_search_edit
from TC_7_ใบแจ้งหนี้.V2.TC_3.Edit import test_page_staus_edit

# TC_8_ใบเสร็จรับเงิน

from TC_8_ใบเสร็จรับเงิน.V2.TC_1.Add import test_page_add_receipt
from TC_8_ใบเสร็จรับเงิน.V2.TC_2.search_Edit import test_page_serach_edit

# TC_9_ใบลดหนี้

from TC_9_ใบลดหนี้.V2.TC_1.search import test_page_search_edit

# TC_10_ใบเตือน

from TC_10_ใบเตือน.V2.TC_1.สร้างใบเตือนรายบุคคล import test_page_create_warning1
from TC_10_ใบเตือน.V2.TC_1.สร้างใบเตือนรายโครงการ import test_page_create_warning

from TC_10_ใบเตือน.V2.TC_2.search_Edit import test_page_search_edit

# TC_11_รายงาน

from TC_11_รายงาน.V2.TC_1.report_day import test_page_report

# TC_12_บริหารแอดมิน

from TC_12_บริหารแอดมิน.V2.TC_1.Add import test_page_add_user
from TC_12_บริหารแอดมิน.V2.TC_2.search_Edit import test_page_serach
from TC_12_บริหารแอดมิน.V2.TC_3.Edit import test_page_edit
from TC_12_บริหารแอดมิน.V2.TC_4.Roly import test_page_roly

# TC_14_Logout

from TC_14_Logout.V2.TC_1.Logout import test_page_logout





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