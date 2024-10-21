
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys 
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
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
        self.assertEqual(driver.title, 'Smarty msm | Dashboard')  # ตรวจสอบว่า title ของหน้าเว็บถูกต้อง

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


    def test_page_dashboard(self):
# *** เปิดหน้า รายชื่อคนลงทะเบียน (อนุมัติ)***
        
        self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/dashboard')
        self.driver.implicitly_wait(10)
        time.sleep(1)

        # คลิกเลือกโครงการ

        Project = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div/div/main/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div')) 
        )
        assert Project.is_displayed(), 'Element is not displayed!'
        assert Project.is_enabled(), 'Element is not enabled!'
        Project.click()
        time.sleep(0.5)  

        Project = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div/div/main/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/input')) 
        )
        assert Project.is_displayed(), 'Element is not displayed!'
        assert Project.is_enabled(), 'Element is not enabled!'
        Project.send_keys('อาคาร C1' + Keys.ARROW_DOWN + Keys.ENTER + Keys.ESCAPE)
        time.sleep(1.5)

        # คลิกวันที่สร้าง 

        start_date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div/div/main/div/div/div/div/div[1]/div/div[2]/div/div')) 
        )
        assert start_date.is_displayed(), 'Element is not displayed!'
        assert start_date.is_enabled(), 'Element is not enabled!'
        start_date.click()
        time.sleep(0.3)

        # เลือกวันที่

        select_day = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[1]')) 
        )
        assert select_day.is_displayed(), 'Element is not displayed!'
        assert select_day.is_enabled(), 'Element is not enabled!'
        select_day.click()
        time.sleep(0.3)    

        # วันที่สินสุด

        date_end = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div[1]/div/main/div/div/div/div/div[1]/div/div[3]/div/div')) 
        )
        assert date_end.is_displayed(), 'Element is not displayed!'
        assert date_end.is_enabled(), 'Element is not enabled!'
        date_end.click()
        time.sleep(1)

        # เลือกวันที่
        select_day = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '//div/div[2]/div/div/div[2]/div/div[5]/button[2]')) 
        )
        assert select_day.is_displayed(), 'Element is not displayed!'
        assert select_day.is_enabled(), 'Element is not enabled!'
        select_day.click()
        time.sleep(0.3)     

        # เลือกปี
        
        select_year = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div/div/main/div/div/div/div/div[3]/div/div[1]/div/div[2]/div/div/div'))
        )
        assert select_year.is_displayed(), 'Element is not displayed!'
        assert select_year.is_enabled(), 'Element is not enabled!'
        select_year.click()
        time.sleep(0.5)

        # คลิก 2024
        
        select_year = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '//div[2]/div/div/div/div/div[125]/button'))
        )
        assert select_year.is_displayed(), 'Element is not displayed!'
        assert select_year.is_enabled(), 'Element is not enabled!'
        select_year.click()

    @classmethod
    
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()    

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\2.Dashboard\\Reports'))