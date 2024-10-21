
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



    def test_page_User(self):

        try:
                # หน้า การบริหาร - ผู้ใช้งาน
                self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/residents')
                self.driver.implicitly_wait(30)

                # เพิ่มลูกบ้าน

                Add = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div[1]/div[1]/div[2]/button[2]'))
                )
                assert Add.is_displayed(), 'Element is not displayed!'
                assert Add.is_enabled(), 'Element is not enabled!'
                Add.click()

                if Add:
                    print('Click Add Already :', True)
                else:
                    print('Cannot Click Add :',False)
                    

                # Upload image

                # อัพโหลดรูปภาพ Mac Os
                upload = self.driver.find_element(by=By.XPATH , value='//div/div/div/div/div/div/form/div/div[1]/input')
                upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')
                time.sleep(0.5)

                # คีย์ ชื่อ

                # self.click = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[2]/div[1]/div/div[2]/div/div')
                # self.click.click()
                # time.sleep(0.1)

                key_name = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[2]/div[1]/div/div[2]/div/div/input'))
                )
                assert key_name.is_displayed(), 'Element is not displayed!'
                assert key_name.is_enabled(), 'Element is not enabled!'
                key_name.send_keys('สมศรี')

                textbox_element = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[2]/div[1]/div/div[2]/div/div/input")  
                textbox_value = textbox_element.get_attribute("value")
                text_to_check = "สมศรี"
                self.assertIn(text_to_check, textbox_value, f"ไม่พบ '{text_to_check}' ในกล่องข้อความ")

                element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[2]/div[1]/div/div[1]/p')
                expected_text = 'ชื่อ'
                self.assertEqual(element.text, expected_text)
                time.sleep(0.1)

                # คีย์ นามสกุล

                Key_Text = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[2]/div[2]/div/div[2]/div/div/input'))
                )
                assert Key_Text.is_displayed(), 'Element is not displayed!'
                assert Key_Text.is_enabled(), 'Element is not enabled!'
                Key_Text.send_keys('พร้อมจ่าย')

                textbox_element = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[2]/div[2]/div/div[2]/div/div/input")  
                textbox_value = textbox_element.get_attribute("value")
                text_to_check = "พร้อมจ่าย"
                self.assertIn(text_to_check, textbox_value, f"ไม่พบ '{text_to_check}' ในกล่องข้อความ")

                element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[2]/div[2]/div/div[1]/p')
                expected_text = 'นามสกุล'
                self.assertEqual(element.text, expected_text)
                time.sleep(0.1)

                # คีย์ Email 

                key_email = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[3]/div[1]/div/div[2]/div/div/input'))
                )
                assert key_email.is_displayed(), 'Element is not displayed!'
                assert key_email.is_enabled(), 'Element is not enabled!'
                key_email.send_keys('sss@gmail.com')
                
                textbox_element = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[3]/div[1]/div/div[2]/div/div/input")  
                textbox_value = textbox_element.get_attribute("value")
                text_to_check = "sss@gmail.com"
                self.assertIn(text_to_check, textbox_value, f"ไม่พบ '{text_to_check}' ในกล่องข้อความ")

                element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[3]/div[1]/div/div[1]/p')
                expected_text = 'อีเมล'
                self.assertEqual(element.text, expected_text)
                time.sleep(0.1)


                # เบอร์โทรศัพท์
                
                key_number = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[3]/div[2]/div/div[2]/div/div/input'))
                )
                assert key_number.is_displayed(), 'Element is not displayed!'
                assert key_number.is_enabled(), 'Element is not enabled!'
                key_number.send_keys('0924296825')
                

                textbox_element = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[3]/div[2]/div/div[2]/div/div/input")  
                textbox_value = textbox_element.get_attribute("value")
                text_to_check = "0924296825"
                self.assertIn(text_to_check, textbox_value, f"ไม่พบ '{text_to_check}' ในกล่องข้อความ")

                element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[3]/div[2]/div/div[1]/p')
                expected_text = 'เบอร์โทรศัพท์'
                self.assertEqual(element.text, expected_text)
                time.sleep(0.1)

                # เลขปประจำตัวประชาชน

                key_number = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[4]/div/div[2]/div/div/input'))
                )
                assert key_number.is_displayed(), 'Element is not displayed!'
                assert key_number.is_enabled(), 'Element is not enabled!'
                key_number.send_keys('012345678912')

                textbox_element = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[4]/div/div[2]/div/div/input") 
                textbox_value = textbox_element.get_attribute("value")
                text_to_check = "012345678912"
                self.assertIn(text_to_check, textbox_value, f"ไม่พบ '{text_to_check}' ในกล่องข้อความ")

                element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[4]/div/div[1]/p')
                expected_text = 'เลขประจำตัวประชาชน'
                self.assertEqual(element.text, expected_text)
                time.sleep(0.1)

                # Save

                # Save = WebDriverWait(self.driver, 10).until(
                # EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/button'))
                # )
                # assert Save.is_displayed(), 'Element is not displayed!'
                # assert Save.is_enabled(), 'Element is not enabled!'
                # Save.click()

                # if Save:
                #     print('Click Save Already :', True)
                # else:
                #     print('Cannot Click Save :',False)

                # # ดึงตำแหน่งของ element
                # location = element.location  # dictionary ที่มี 'x' และ 'y'
                # size = element.size          # dictionary ที่มี 'width' และ 'height'
                
                # print(f'Button : Save')
                # print(f"ตำแหน่งของ element: {location}")
                # print(f"ขนาดของ element: {size}")

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
        print('___Test Pass__')
        cls.driver.quit()   

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



