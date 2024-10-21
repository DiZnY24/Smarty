
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pynput.keyboard import Key, Controller 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner
import unittest
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

    def test_page_news(self):

        try:    
            # หน้า ข่าวสาร
            self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/announcement')
            self.driver.implicitly_wait(10)

            

            # elements = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_all_elements_located((By.XPATH,'/html/body/div/div/main/div/div/div'))
            # )
            # for element in elements:
            #     print(element.text)
            
            # elements = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_all_elements_located((By.XPATH,'/html/body/div/div/main/div/div/div/div/div[2]'))
            # )
            # for element in elements:
            #     print(element.text)
            
            
    #   เพิ่ทข่าวสาร

            Add_News = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div[1]/div[1]/div/button'))
            )
            assert Add_News.is_displayed(), 'Element is not displayed!'
            assert Add_News.is_enabled(), 'Element is not enabled!'
            Add_News.click()     

            if Add_News:
                print('Click Button เพิ่มข่าว : Pass')
            else:
                print('Not Click Button เพิ่มข่าว : Fail')               
            # กรอกข้อมูล

            # ชื่อข่าว
        
            Key_name = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/input'))
            )
            assert Key_name.is_displayed(), 'Element is not displayed!'
            assert Key_name.is_enabled(), 'Element is not enabled!'
            Key_name.send_keys('ข่าวใหม่เช้านี้')   
            
            # อัพโหลดรูปภาพ

            upload = self.driver.find_element(by=By.XPATH , value='/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[1]/div/div/input')
            upload.send_keys('/Users/dizny/Downloads/Image/image Test/Logo.jpg.jpg')

            if upload:
                print('Upload image : Pass')
            else:
                print('Not Upload image : Fail')
            # คลิกวันที่
            
            date = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[3]/div[2]/div/div'))
            )
            assert date.is_displayed(), 'Element is not displayed!'
            assert date.is_enabled(), 'Element is not enabled!'
            date.click()

            if date:
                print('Click date : Pass')
            else:
                print('Not Click date : Fail')

            # # เลือกวันที่ ....

            date = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '//div/div[2]/div/div/div[2]/div/div[5]/button[2]'))
            )
            assert date.is_displayed(), 'Element is not displayed!'
            assert date.is_enabled(), 'Element is not enabled!'
            date.click()

            if date:
                print('select date : Pass')
            else:
                print('Not select date : Fail')

            # รายละเอียดข่าวสาร
            
            Key_email = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/div'))
            )
            assert Key_email.is_displayed(), 'Element is not displayed!'
            assert Key_email.is_enabled(), 'Element is not enabled!'
            Key_email.send_keys('Test1111111')  


            # ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
            self.driver.execute_script("window.scrollTo(0, 0);")  
            time.sleep(1)

            # Save

            Save = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '//div/div/div/form/div/div[1]/div/div[1]/div/button[2]'))
            )
            assert Save.is_displayed(), 'Element is not displayed!'
            assert Save.is_enabled(), 'Element is not enabled!'
            Save.click()

            if Save:
                print('Click Button Save : Pass')
            else:
                print('Not Click Button Save : Fail')

    # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
            element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[2]/div[1]/div/table/tbody/tr[1]/td[1]/p"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
    # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
            print("Wait show News New :",(True))

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
        cls.driver.quit() 

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\3.ข่าวสาร\\Reports'))




