
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys
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

    def test_page_title(self):
        driver = self.driver
        self.assertEqual(driver.title, 'Smarty msm | Pre-register')  # ตรวจสอบว่า title ของหน้าเว็บถูกต้อง

    def test_Login_Smarty(self):
        result = None
        time.sleep(1)
        driver = self.driver
        try:
        # ป้อนรหัสผ่าน
            element = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div/div[1]/div/div[1]/p')
            expected_text = 'เบอร์โทรศัพท์ / รหัสพนักงาน'
            assert element.text == expected_text, f"ข้อความไม่ตรงกัน: คาดว่า '{expected_text}' แต่ได้ '{element.text}'"
            time.sleep(0.1)

            Key_Passwprd = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input')
            Key_Passwprd.send_keys('00000')

        # ตรวจสอบค่าที่ป้อนในกล่องข้อความ
            textbox_element = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input")  
            textbox_value = textbox_element.get_attribute("value")
            text_to_check = "00000"
            assert text_to_check in textbox_value, f"ไม่พบ '{text_to_check}' ในกล่องข้อความ"
            
            Click = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/button')  # ขอ OTP
            assert Click.is_displayed(), 'Element is not displayed!'
            assert Click.is_enabled(), 'Element is not enabled!'
            Click.click()  # คลิกขอ OTP

        # รอให้ Element คลิกได้  # คลิกขอ เข้าสู่ระบบ
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/button')) # คลิกขอ เข้าสู่ระบบ
            )
            assert element.is_displayed(), 'Element is not displayed!'
            assert element.is_enabled(), 'Element is not enabled!'
            element.click()
        # จับข้อผิดพลาดนี้เมื่อไม่พบองค์ประกอบ และเรียกใช้ self.fail() เพื่อบอกว่าการทดสอบล้มเหลว
        except NoSuchElementException:
            self.fail('Element not Found')
        # จับข้อผิดพลาดเมื่อการตรวจสอบไม่สำเร็จ
        except AssertionError as e:
            self.fail(str(e))
        # จับข้อผิดพลาดทั่วไปที่ไม่อยู่ในเงื่อนไขอื่น ๆ
        except Exception as o:
            self.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว')

        try:
        # ทดสอบการคลิก Element
            result_elemet = self.driver.find_element(By.XPATH, '/html/body/div/div/main/nav/div/div/div/ul/div[3]/li/div/div[2]')    
            self.assertIsNotNone(result_elemet)
        except NoSuchElementException as e:
            self.fail('Element not Found')
        # การคืนค่าจากฟังก์ชันช่วยให้เราสามารถรู้สถานะของการล็อกอินได้ โดยในที่นี้คืนค่าที่แสดงว่าล็อกอินสำเร็จหรือไม่
        return result
    
    def test_page_pending(self):
        driver = self.driver
# *** เปิดหน้า รายชื่อคนลงทะเบียน (รออนุมัติ) ***
        
        try:
            # คลิกเลือกตึก
            select_building = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div[1]/div[1]/div/div/div/div/input')) 
            )
            select_building.send_keys('อาคาร C1' + Keys.ARROW_DOWN + Keys.ENTER + Keys.ESCAPE)
            self.assertIn("อาคาร C1", driver.page_source)

            input_key = driver.find_element(By.XPATH, 
            '/html/body/div/div/main/div/div/div/div[1]/div[1]/div/div/div/div/input')
            input_value = input_key.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}')

            # พิมพ์ ชั้น / ห้อง

            floor_room = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div/div')) 
            )
            assert floor_room.is_displayed(), 'Element is not displayed!'
            assert floor_room.is_enabled(), 'Element is not enabled!'
            floor_room.click()
            time.sleep(1)

            floor_room = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div/div/input')) 
            )
            floor_room.send_keys('04/02' + Keys.ARROW_DOWN + Keys.ENTER)
            self.assertIn("04/02", driver.page_source)

            # ค้นหาจาก ชื่อ / นามสกุล / เลขบัตรประชาชน
            Search_by_name = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/input')) 
            )
            Search_by_name.send_keys('0935909660' + Keys.ARROW_DOWN + Keys.ENTER)
            
            # คลิกวันที่สร้าง 
            date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[3]/div[1]/div/div')) 
            )
            assert date.is_displayed(), 'Element is not displayed!'
            assert date.is_enabled(), 'Element is not enabled!'
            date.click()

            # เลือกวันที่
            date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[2]')) 
            )
            assert date.is_displayed(), 'Element is not displayed!'
            assert date.is_enabled(), 'Element is not enabled!'
            date.click()      

            # วันที่สิ้นสุด
            date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div')) 
            )
            assert date.is_displayed(), 'Element is not displayed!'
            assert date.is_enabled(), 'Element is not enabled!'
            date.click()

            # เลือกวันที่
            date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[2]')) 
            )
            assert date.is_displayed(), 'Element is not displayed!'
            assert date.is_enabled(), 'Element is not enabled!'
            date.click()
            
            # บทบาท
            Role = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div/div/div')) 
            )
            assert Role.is_displayed(), 'Element is not displayed!'
            assert Role.is_enabled(), 'Element is not enabled!'
            Role.click()
            
            # เลือกบทบาท
            Role = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')) 
            )
            assert Role.is_displayed(), 'Element is not displayed!'
            assert Role.is_enabled(), 'Element is not enabled!'
            Role.click()

        except NoSuchElementException:
            self.fail('Element not Found')
        # จับข้อผิดพลาดเมื่อการตรวจสอบไม่สำเร็จ
        except AssertionError as e:
            self.fail(str(e))
        # จับข้อผิดพลาดทั่วไปที่ไม่อยู่ในเงื่อนไขอื่น ๆ
        except Exception as o:
            self.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว')

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print('___Test Pass___')
        cls.driver.quit()    

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\1.Register\\Reports'))