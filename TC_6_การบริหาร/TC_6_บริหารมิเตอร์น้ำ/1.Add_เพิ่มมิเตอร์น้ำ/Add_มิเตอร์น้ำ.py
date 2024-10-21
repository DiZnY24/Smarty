
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

        wait = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '//div/div/div/div[3]/ul/div'))
            )
        print('รอจนหน้าเว็ปโหลดเสร็จ : Pass')

        print('-------------------------------')

    
    def test_page_add_water_meter(self):

        try:
            # หน้า บริหารโครงการ
            self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/water-meter')
            self.driver.implicitly_wait(20)

        # เพิ่มมิเตอร์น้ำ

            water_meter = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[1]/div[1]/div/button'))
            )
            assert water_meter.is_displayed(), 'Element is not displayed!'
            assert water_meter.is_enabled(), 'Element is not enabled!'
            water_meter.click()
            time.sleep(0.5)   

        # โครงการ

            Project = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
            )
            assert Project.is_displayed(), 'Element is not displayed!'
            assert Project.is_enabled(), 'Element is not enabled!'
            Project.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Project.send_keys('อาคาร C8' + Keys.ARROW_DOWN + Keys.ENTER)
            time.sleep(0.1) 

        # ชั้น / ห้อง

            floor = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/input'))
            )
            assert floor.is_displayed(), 'Element is not displayed!'
            assert floor.is_enabled(), 'Element is not enabled!'
            floor.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)
            time.sleep(0.1) 

        # หมายเลขมิเตอร์น้ำ 

            number_water_meter = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[3]/div[1]/div/div[2]/div/div/input'))
            )
            assert number_water_meter.is_displayed(), 'Element is not displayed!'
            assert number_water_meter.is_enabled(), 'Element is not enabled!'
            number_water_meter.send_keys('950')
            time.sleep(0.1) 

        # ค่ามาตรวัดเริ่มต้น

            number_water_meter = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[3]/div[2]/div/div[2]/div/div/input'))
            )
            assert number_water_meter.is_displayed(), 'Element is not displayed!'
            assert number_water_meter.is_enabled(), 'Element is not enabled!'
            number_water_meter.send_keys('150')       
            time.sleep(0.1) 
        # ขนาดมาตรน้ำ

            size_water_meter = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[3]/div[3]/div/div[2]/div/div/input'))
            )
            assert size_water_meter.is_displayed(), 'Element is not displayed!'
            assert size_water_meter.is_enabled(), 'Element is not enabled!'
            size_water_meter.send_keys('32')       
            time.sleep(0.1) 

        # สถานะมิเตอร์

            status_water_meter = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[3]/div[4]/div[2]/div/div/div'))
            )
            assert status_water_meter.is_displayed(), 'Element is not displayed!'
            assert status_water_meter.is_enabled(), 'Element is not enabled!'
            status_water_meter.click()       
            time.sleep(0.1) 

            status_water_meter = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]'))
            )
            assert status_water_meter.is_displayed(), 'Element is not displayed!'
            assert status_water_meter.is_enabled(), 'Element is not enabled!'
            status_water_meter.click()       
            time.sleep(0.1) 

        # วันที่ลงทะเบียน

            Registration = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[4]/div/div/div'))
            )
            assert Registration.is_displayed(), 'Element is not displayed!'
            assert Registration.is_enabled(), 'Element is not enabled!'
            Registration.click()       
            time.sleep(0.1) 

            Registration = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[2]'))
            )
            assert Registration.is_displayed(), 'Element is not displayed!'
            assert Registration.is_enabled(), 'Element is not enabled!'
            Registration.click()       
            time.sleep(0.1) 

    # บันทึก

            # Save = WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[1]/div[2]/div/button[2]'))
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click()       
            # time.sleep(0.1) 
            

        except NoSuchElementException:
            self.fail('Element not Found')
        except AssertionError as e:
            self.fail(str(e))
        except Exception as o:
            self.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว')

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()   

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



