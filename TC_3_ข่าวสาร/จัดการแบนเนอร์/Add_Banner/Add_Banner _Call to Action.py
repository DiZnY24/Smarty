
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller 
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException


class WebTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(login):

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        login.driver = webdriver.Chrome(options=options)
        # login.driver = webdriver.Chrome()  # หรือใช้ webdriver.Firefox(), webdriver.Edge(), etc.
        login.driver.get('https://msm-smarty-cms-staging.hr-impact.co/login')
        login.driver.set_window_size(1600, 1000)
        login.driver.implicitly_wait(10)

    # def test_page_title(self):
    #     driver = self.driver
    #     self.assertEqual(driver.title, 'Smarty msm')  # ตรวจสอบว่า title ของหน้าเว็บถูกต้อง

    def test_login_smarty(self):
        result = None
        time.sleep(1)

        try:
            wait = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input'))
            )
            print('รอจนกว่าจะสามารถกรอกรหัสได้ : Pass')

        # ป้อนรหัสผ่าน
            element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div/div[1]/div/div[1]/p')
            expected_text = 'เบอร์โทรศัพท์ / รหัสพนักงาน'
            assert element.text == expected_text, f"ข้อความไม่ตรงกัน: คาดว่า '{expected_text}' แต่ได้ '{element.text}'"
            time.sleep(0.1)

            Key_Passwprd = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input')
            Key_Passwprd.send_keys('00000')

            input_key = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input')
            input_value = input_key.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}')    
            
            Click_Otp = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/button')  # ขอ OTP
            assert Click_Otp.is_displayed(), 'Element is not displayed!'
            assert Click_Otp.is_enabled(), 'Element is not enabled!'
            Click_Otp.click()  # คลิกขอ OTP

            if Click_Otp:
                print('กดคลิกขอ Otp สำเร็จ : Pass')
            else:
                print('กดคลิกขอ Otp ไม่สำเร็จ : Fail')

        # รอให้ Element คลิกได้  # คลิกขอ เข้าสู่ระบบ
            Click_submit = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/button')) # คลิกขอ เข้าสู่ระบบ
            )
            assert Click_submit.is_displayed(), 'Element is not displayed!'
            assert Click_submit.is_enabled(), 'Element is not enabled!'
            Click_submit.click()

            if Click_submit:
                print('กดคลิกขอ เข้าสู่ระบบ สำเร็จ : Pass')
            else:
                print('กดคลิกขอ เข้าสู่ระบบ ไม่สำเร็จ : Fail')

        except NoSuchElementException:
            self.fail('Element not Found')
        except AssertionError as e:
            self.fail(str(e))
        except Exception as o:
            self.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว')

        wait = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div/div/div/div[3]/ul/div'))
            )
        print('รอจนหน้าเว็ปโหลดเสร็จ : Pass')

        print('-------------------------------')

    def test_page_add_banner_call_to_action(self):    

        # หน้า ข่าวสาร
        self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/banner')
        self.driver.implicitly_wait(30)


        Add_Banner = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div[1]/div/main/div/div/div/div/div[1]/div/div/button'))
        )
        assert Add_Banner.is_displayed(), 'Element is not displayed!'
        assert Add_Banner.is_enabled(), 'Element is not enabled!'
        Add_Banner.click()   

        # ชื่อแบนเนอร์

        Add_name = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/input'))
            )
        assert Add_name.is_displayed(), 'Element is not displayed!'
        assert Add_name.is_enabled(), 'Element is not enabled!'
        Add_name.send_keys('Tester_Kub')         

        # อัพโหลดรูปภาพ Mac Os

        upload = self.driver.find_element(by=By.XPATH , value='/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[1]/div/div/div/input')
        upload.send_keys('/Users/dizny/Downloads/Image/image Test/Logo.jpg.jpg')

        # date วันที่ วันที่เผยแพร่

        date = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[3]/div[2]/div/div'))
            )
        assert date.is_displayed(), 'Element is not displayed!'
        assert date.is_enabled(), 'Element is not enabled!'
        date.click() 

        select_date = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div/div/div[2]/div/div[5]/button[2]'))
            )
        assert select_date.is_displayed(), 'Element is not displayed!'
        assert select_date.is_enabled(), 'Element is not enabled!'
        select_date.click()   

        # ต้องการเพิ่มปุ่ม Call to Action?

        Call_to_Action = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[2]/div/div/div[2]/div/label/span[1]'))
            )
        assert Call_to_Action.is_displayed(), 'Element is not displayed!'
        assert Call_to_Action.is_enabled(), 'Element is not enabled!'
        Call_to_Action.click()   

        # ------------------------------------------------------------------------------------------------------------------------------------------

        # บริการในแอปพลิเคชันที่ต้องการพาผู้ใช้งานไป (DeepLink)

        # Internal = WebDriverWait(self.driver, 30).until(
        #         EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div'))
        #     )
        # assert Internal.is_displayed(), 'Element is not displayed!'
        # assert Internal.is_enabled(), 'Element is not enabled!'
        # Internal.click()           

        # Internal_1 = WebDriverWait(self.driver, 30).until(
        #         EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[3]'))
        #     )
        # assert Internal_1.is_displayed(), 'Element is not displayed!'
        # assert Internal_1.is_enabled(), 'Element is not enabled!'
        # Internal_1.click()           
         
        # ------------------------------------------------------------------------------------------------------------------------------------------

        External = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div[2]/div/div/div/div[1]/div[2]/div/div/div'))
            )
        assert External.is_displayed(), 'Element is not displayed!'
        assert External.is_enabled(), 'Element is not enabled!'
        External.click()           

        External_1 = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div[2]/div[3]/ul/li[2]'))
            )
        assert External_1.is_displayed(), 'Element is not displayed!'
        assert External_1.is_enabled(), 'Element is not enabled!'
        External_1.click()           

        Url = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/input'))
            )
        assert Url.is_displayed(), 'Element is not displayed!'
        assert Url.is_enabled(), 'Element is not enabled!'
        Url.send_keys('https://msm-smarty-cms-staging.hr-impact.co/banner/51/edit')

        # ------------------------------------------------------------------------------------------------------------------------------------------

        Save = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[1]/div[2]/button[2]'))
            )
        assert Save.is_displayed(), 'Element is not displayed!'
        assert Save.is_enabled(), 'Element is not enabled!'
        Save.click()  

# รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
        element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[2]/div[1]/div/table/tbody/tr[1]/td[1]/p"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
        )
# หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
        print('Element Show :',(True))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() 

if __name__ == '__main__':
    unittest.main()
             


# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\3.ข่าวสาร\\Reports'))
           






