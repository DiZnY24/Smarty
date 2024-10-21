
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


    def test_page_create(self):

        try:
            # หน้า จัดการลูกหนี้
            self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/debtors')
            self.driver.implicitly_wait(10)
            time.sleep(1)

    # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
            element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[8]/div/div"))  
            )
    # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)


            # สร้างใบปลอดหนี้แบบมีเงื่อนไข

            management = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[8]/div/div')) 
            )
            assert management.is_displayed(), 'Element is not displayed!'
            assert management.is_enabled(), 'Element is not enabled!'
            management.click()
            time.sleep(0.5)

            management = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')) 
            )
            assert management.is_displayed(), 'Element is not displayed!'
            assert management.is_enabled(), 'Element is not enabled!'
            management.click()
            time.sleep(0.1)


    # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
            element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[1]/div/div/div")) 
            )
    # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)
            

            # วันที่ กรอกฟอร์ม

            Date = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[1]/div/div/div')) 
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            Date = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//div/div/div/div[2]/div/div[2]/div/div/div[10]/button')) 
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            Date = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[125]/button')) 
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.send_keys(Keys.ESCAPE)
            time.sleep(0.1)


            # Input Text ข้าพเจ้าบริษัท

            Input_Text = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[2]/div/div/input')) 
            )
            assert Input_Text.is_displayed(), 'Element is not displayed!'
            assert Input_Text.is_enabled(), 'Element is not enabled!'
            Input_Text.send_keys('Impact')
            time.sleep(0.1)

            # Input Text  โดย

            Input_Text = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[3]/div/div/input')) 
            )
            assert Input_Text.is_displayed(), 'Element is not displayed!'
            assert Input_Text.is_enabled(), 'Element is not enabled!'
            Input_Text.send_keys(Keys.CONTROL + 'a' + Keys.DELETE) 
            Input_Text.send_keys('อาม ม่อน เสิน 23')
            time.sleep(0.1)

            # Input Text มีภาระหนี้สินจำนวน

            Input_Text = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[5]/div[3]/div/input')) 
            )
            assert Input_Text.is_displayed(), 'Element is not displayed!'
            assert Input_Text.is_enabled(), 'Element is not enabled!'
            Input_Text.send_keys('1500')
            time.sleep(0.1)

            # Input Text ลงชื่อ ผู้จัดการนิติบุคคลอาคารชุด

            Input_Text = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[7]/div/div/div/input')) 
            )
            assert Input_Text.is_displayed(), 'Element is not displayed!'
            assert Input_Text.is_enabled(), 'Element is not enabled!'
            Input_Text.send_keys('Test')
            time.sleep(0.1)


            # วันที่ 1. นับตั้งจดทะเบียนนิติบุคคลอาคารชุด - วันที่

            Date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[4]/div/div/div'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            Date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/button[4]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)
        
            Date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[4]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.send_keys(Keys.ESCAPE)
            time.sleep(0.1)       

            # วันที่ 2. ระหว่างวันที่

            Date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[5]/div[1]/div/div'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            Date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/button[5]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)
        
            Date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/button[5]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.send_keys(Keys.ESCAPE)
            time.sleep(0.1)       

            # วันที่ - วันที่

            Date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[5]/div[2]/div/div'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            Date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/button[6]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)
        
            Date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/button[6]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.send_keys(Keys.ESCAPE)
            time.sleep(0.1)       

    # วันที่ 3. ระหว่างวันที่


            Date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[6]/div/div/div'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            Date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/button[7]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)
        
            Date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/button[7]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.send_keys(Keys.ESCAPE)
            time.sleep(0.1)       

    # ทดสอบการคลิก Element - บันทึก - คลิกออก
            result_element = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[2]/button[1]')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)    

            result_element = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[2]/button[2]')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

    # เช็คข้อความในปุ่ม Back - บันทึก 
            button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[2]/button[1]')
            assert button.text == 'ยกเลิก', f"Expected 'Expected Button Text' but got '{button.text}'"
            time.sleep(0.1)

            button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[2]/button[2]')
            assert button.text == 'บันทึก', f"Expected 'Expected Button Text' but got '{button.text}'"
            time.sleep(0.1)

    # Button Save 

            # Save = WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[2]/button[2]'))
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click()
            # time.sleep(0.1)   

    # Button ยกเลิก

            cancel = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[2]/button[1]'))
            )
            assert cancel.is_displayed(), 'Element is not displayed!'
            assert cancel.is_enabled(), 'Element is not enabled!'
            cancel.click()
            time.sleep(0.1)   
        
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
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



