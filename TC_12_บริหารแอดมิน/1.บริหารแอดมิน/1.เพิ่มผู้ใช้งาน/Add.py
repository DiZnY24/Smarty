
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
from selenium.common.exceptions import NoSuchElementException 
from  selenium.common.exceptions import NoSuchElementException,TimeoutException


class WebTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(login):

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        login.driver = webdriver.Chrome(options=options)
        login.driver.get('https://msm-smarty-cms-staging.hr-impact.co/login')
        login.driver.set_window_size(1600, 1000)
        login.driver.implicitly_wait(10)

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



    def test_page_add_user(self):
                
        try:
        # หน้า การบริหาร - ผู้ใช้งาน
                self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/admin')
                self.driver.implicitly_wait(20)


        #เพิ่มผู้ใช้งาน    
                click_add = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div[2]/div[1]/div[1]/button'))
                )
                assert click_add.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert click_add.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                click_add.click()
                time.sleep(1) 

                element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[3]/div/div[1]/div/div[2]/div[1]/h6")) 
                )
                print("Element is visible. Proceeding with the next step.")
                time.sleep(1)

        # เลือกผู้ใช้งาน

                select_username = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div/div')
                select_username.click()
                time.sleep(0.1)

                wait = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div/div/input'))
                )
                print(True)

                input('รอจนกว่ารายชื่อจะปรากฏ ENTER')

                key_name = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div/div/input'))
                )
                key_name.send_keys("Karis Matchaparn (อิม)" + Keys.ARROW_DOWN)
                key_name.send_keys(Keys.ENTER)
                time.sleep(1)

                # บทบาท 

                Role = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[2]/div/div/div'))
                )
                assert Role.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert Role.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                Role.click()
                time.sleep(1.5) 

                # element = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[2]/div/div/div')
                # actions = ActionChains(self.driver)
                # self.assertTrue(element.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า")
                # self.assertTrue(element.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
                # actions.move_to_element(element).click().perform()
                # time.sleep(0.1)

                # button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[2]/div/div/div')
                # self.assertTrue(button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า")
                # self.assertTrue(button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
                # button.click()
                # time.sleep(0.1)

                Role = self.driver.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[1]')
                assert Role.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                assert Role.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                Role.click()
                time.sleep(0.5)

        # จัดการเลือกโครงการ 

                button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[4]/div[2]/div/div/div')
                assert button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                assert button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                button.click()
                time.sleep(1.5)

                button1 = self.driver.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[1]')
                assert button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                assert button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                button1.click()
                time.sleep(0.5)


                element_2 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/button")

                self.driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
                time.sleep(1)

        # Save

                # Save = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/button') 
                # Save.click()

        # Refresh

                # try:
                #         element = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div/div[3]/button")
                #         assert element.is_displayed(), "Element is not visible"  
                #         self.assertTrue(element.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
                #         self.assertTrue(element.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
                #         element.click()
                # except NoSuchElementException:
                #         print("Element not found")
                #         time.sleep(0.1)


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
        # print('___Test Pass__')
        cls.driver.quit()   

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



