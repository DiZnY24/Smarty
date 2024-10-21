
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
from datetime import datetime
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






    def test_page_report(self):

        try:            
            # หน้า จัดการลูกหนี้
            self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/report/daily')
            self.driver.implicitly_wait(10)
            time.sleep(1)


    # วันเริ่มต้น

    #         Date = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div/div[1]/div/div')
    #         self.assertTrue(Date.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
    #         self.assertTrue(Date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
    #         Date.click()
    #         time.sleep(0.1)

    #         Date = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/button[1]')
    #         self.assertTrue(Date.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
    #         self.assertTrue(Date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
    #         Date.click()
    #         time.sleep(0.1)

    #         ESC = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/button[1]')
    #         ESC.send_keys(Keys.ESCAPE)

    # # # วันสิ้นสุด

    #         Date = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div/div[2]/div/div')
    #         self.assertTrue(Date.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
    #         self.assertTrue(Date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
    #         Date.click()
    #         time.sleep(0.1)

    #         Date = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/button[7]')
    #         self.assertTrue(Date.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
    #         self.assertTrue(Date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
    #         Date.click()
    #         time.sleep(0.1)

    #         ESC = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/button[7]')
    #         ESC.send_keys(Keys.ESCAPE)


    # # ทดสอบการคลิก Element
            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[1]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            Download = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[1]/div/button').click()
            time.sleep(0.1)
            print('ดาวโหลด นิติบุคคลอาคารชุด ดับเบิ้ลเลค คอนโดมิเนียม เฟส 2 เรียบร้อย')

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[2]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(2.5)
            
            Download = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[2]/div/button').click()
            time.sleep(0.1)
            print('ดาวโหลด testhi เรียบร้อย')

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[3]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(2.5)

            Download = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[3]/div/button').click()
            time.sleep(0.1)
            print('ดาวโหลด นิติบุคคลอาคารชุด เมืองทอง เรียบร้อย')

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[4]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[5]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[6]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[7]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[8]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[9]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

    # ค้นหา element ที่ต้องการให้มองเห็น
            element_2 = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div[17]/div/p")

    # ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
            time.sleep(1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[10]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[11]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[12]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[13]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[14]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)
            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[15]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[16]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[17]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[18]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[19]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[20]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[21]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[22]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[23]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[24]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[25]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

    # ค้นหา element ที่ต้องการให้มองเห็น
            element_2 = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div[30]/div/p")

    # ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
            time.sleep(1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[26]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[27]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[28]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[29]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[30]/div/button')    
            self.assertIsNotNone(result_element)
            time.sleep(0.1)

            self.driver.execute_script("window.scrollTo(0, 0);")  
            time.sleep(1)

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



