
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
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



    def test_page_Resident(self):

        try:
                # หน้า การบริหาร - ผู้ใช้งาน

                self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/users')
                self.driver.implicitly_wait(30)

                # คีย์ หมายเลขบัตรประชาชน

                Key_Text = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div/input')) #คีย์ เลขประชาชน
                )
                assert Key_Text.is_displayed(), 'Element is not displayed!'
                assert Key_Text.is_enabled(), 'Element is not enabled!'
                Key_Text.send_keys('0000000000000')
        
                textbox_element = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div/input")  
                textbox_value = textbox_element.get_attribute("value")
                text_to_check = "0000000000000"
                self.assertIn(text_to_check, textbox_value, f"ไม่พบ '{text_to_check}' ในกล่องข้อความ")

                element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/p')
                expected_text = 'หมายเลขบัตรประชาชน'
                self.assertEqual(element.text, expected_text)
                time.sleep(0.1)

                # คีย์ ชื่อ

                key_name = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/input')) #คีย์ ชื่อ
                )
                assert key_name.is_displayed(), 'Element is not displayed!'
                assert key_name.is_enabled(), 'Element is not enabled!'
                key_name.send_keys('kanapok')

                textbox_element = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/input")  
                textbox_value = textbox_element.get_attribute("value")
                text_to_check = "kanapok"
                self.assertIn(text_to_check, textbox_value, f"ไม่พบ '{text_to_check}' ในกล่องข้อความ")

                element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div/div[1]/p')
                expected_text = 'ชื่อ'
                self.assertEqual(element.text, expected_text)
                time.sleep(0.1)

                # เลือก สถานะ

                status = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div'))
                )
                assert status.is_displayed(), 'Element is not displayed!'
                assert status.is_enabled(), 'Element is not enabled!'  
                status.click()

                element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[1]/p')
                expected_text = 'สถานะ'
                self.assertEqual(element.text, expected_text)
                time.sleep(0.1)

                # เลือก สถานะ มีห้อง

                room = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]')) # เลือกห้องที่มี
                )
                assert room.is_displayed(), 'Element is not displayed!'
                assert room.is_enabled(), 'Element is not enabled!'
                room.click()

                # ค้นหา

                search = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/button[2]')) # ค้นหา
                )
                assert search.is_displayed(), 'Element is not displayed!'
                assert search.is_enabled(), 'Element is not enabled!'
                search.click()
        
                time.sleep(0.1)

                element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, 
                "/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
                )
                print("Wait Show Element :",True )
                
                button = self.driver.find_element(By.XPATH, '//div/div/div[2]/div[2]/div/div/div/div/div[2]/div')
                assert button.text == 'kanapok', f"Expected 'Expected Button Text' but got '{button.text}'"
                time.sleep(2)

                # ล้างข้อมความทั้งหมด

                element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/button[1]')) # ล้างข้อมความทั้งหมด
                )
                element.click()
                time.sleep(0.1)

        except ArithmeticError as e:
            print(f'ตรวจสอบไม่สำเร็จ: {e}')
        except NoSuchElementException as b:
            print(f'ไม่พบองค์ประกอบของ Elenemt: {b}')
        except Exception as n:
            print(f'เงื่อนไขไม่ตรงตามที่คาดหวัง: {n}')
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



