
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from pynput.keyboard import Key, Controller 
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

            Key_Password = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input'))
            )
            assert Key_Password.is_displayed(), 'Element is not displayed!'
            assert Key_Password.is_enabled(), 'Element is not enabled!'
            Key_Password.send_keys('00000') 


            input_key = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input')
            input_value = input_key.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}')    
            
            Click_Otp = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/button'))
            )
            assert Click_Otp.is_displayed(), 'Element is not displayed!'
            assert Click_Otp.is_enabled(), 'Element is not enabled!'
            Click_Otp.click() 

            if Click_Otp:
                print('กดคลิกขอ Otp สำเร็จ : Pass')
            else:
                print('กดคลิกขอ Otp ไม่สำเร็จ : Fail')

        # รอให้ Element คลิกได้  # คลิกขอ เข้าสู่ระบบ
            Click_submit = WebDriverWait(self.driver, 30).until(
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



    def test_page_search_edit(self):
        # หน้า จัดการลูกหนี้
        self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/invoice')
        self.driver.implicitly_wait(10)

        # คีย์ โครงการ

        project = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div[2]/div/div/input'))
        )
        assert project.is_displayed(), 'Element is not displayed!'
        assert project.is_enabled(), 'Element is not enabled!'
        project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)

        # คีย์ ชั้น / ห้อง

        floor_room = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div/input'))
        )
        assert floor_room.is_displayed(), 'Element is not displayed!'
        assert floor_room.is_enabled(), 'Element is not enabled!'
        floor_room.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(0.1)

# คีย์ ค้นหารายชื่อ
        search_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div/div/div/div'))
        )
        assert search_name.is_displayed(), 'Element is not displayed!'
        assert search_name.is_enabled(), 'Element is not enabled!'
        search_name.click()
        time.sleep(0.5)

        click = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[4]/button[1]').click()

        key_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/input'))
        )
        assert key_name.is_displayed(), 'Element is not displayed!'
        assert key_name.is_enabled(), 'Element is not enabled!'
        key_name.send_keys('รายการใหม่' + Keys.ARROW_DOWN + Keys.ENTER)

        time.sleep(1)

# วันที่ วันที่ออกเอกสาร

        Date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div/div/div'))
        )
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

        Date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[3]'))
        )
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

# วันที่ วันที่ครบกำหนดชำระ (เริ่มต้น)

        Date = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div')
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

        Date = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/button[3]')
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

# วันที่ วันที่ครบกำหนดชำระ (สิ้นสุด)

        Date = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div/div')
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

        Date = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/button[7]')
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

# วันที่สร้างเอกสาร (เริ่มต้น)

        Date = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[4]/div/div/div')
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

        Date = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[1]')
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

# วันที่สร้างเอกสาร (สิ้นสุด)

        Date = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[5]/div/div/div')
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

        Date = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[2]')
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

# วันประกาศใบแจ้งหนี้

        Date = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[6]/div/div/div')
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

        Date = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[3]')
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

# ที่อยู่จัดส่งเอกสาร

        Date = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[7]/div[2]/div/div/div')
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

        Date = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

# ค้นหา เลขที่เอกสาร

        Date = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[1]/div/div[2]/div/div/input')
        Date.send_keys('IW2024092200001')
        time.sleep(0.1)

# ค้นหา ชื่อ

        Date = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[2]/div/div[2]/div/div/input')
        Date.send_keys('คุณอมรกิจ')
        time.sleep(0.1)

# Refresh

        Refresh = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/button')
        assert Refresh.is_displayed(), 'Element is not displayed!'
        assert Refresh.is_enabled(), 'Element is not enabled!'
        Refresh.click()
        time.sleep(0.1)

        
# รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
        element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]")) 
        )
# หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
        print("Element is visible. Proceeding with the next step.")
        time.sleep(0.1) 


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()   

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



