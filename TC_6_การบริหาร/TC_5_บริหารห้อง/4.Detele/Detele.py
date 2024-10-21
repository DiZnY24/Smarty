
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



    def test_page_delete(self):
        # หน้า การบริหาร - ผู้ใช้งาน
        self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/units')
        self.driver.implicitly_wait(10)
        resutl = None

        try:
            # Detele

            delete = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[9]/div/button'))
            )
            assert delete.is_displayed(), 'Element is not displayed!'
            assert delete.is_enabled(), 'Element is not enabled!'
            if delete:
                delete.click()
                print('Click delete Already :', True)
            elif delete:
                print('Cannot Click delete :',False)
            else:
                print('ไม่ตรงกับเงื่อนไขใดๆ',False)

            time.sleep(0.5)

            cancel = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[1]')
            assert cancel.is_displayed(), 'Element is not displayed!'
            assert cancel.is_enabled(), 'Element is not enabled!'
            
            if cancel:
                cancel.click()
                print('Click Cancel Already :', True)
            elif cancel:
                print('Cannot Click Cancel :',False)
            else:
                print('ไม่ตรงกับเงื่อนไขใดๆ',False)
            
            # comfirm = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]')
            # assert comfirm.is_displayed(), 'Element is not displayed!'
            # assert comfirm.is_enabled(), 'Element is not enabled!'
            # comfirm.click()

            # เช็คข้อความในปุ่ม เพิ่มห้อง
            button = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[1]/div/button')
            assert button.text == 'เพิ่มห้อง', f"Expected 'Expected Button Text' but got '{button.text}'"

            # เช็คข้อความในปุ่ม ดาวโหลดข้อมูล
            button = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[2]/div/div/button')
            assert button.text == 'ดาวโหลดข้อมูล', f"Expected 'Expected Button Text' but got '{button.text}'"

            # เช็คข้อความในปุ่ม อัพโหลดข้อมูล
            button = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[2]/div/button')
            assert button.text == 'อัพโหลดข้อมูล', f"Expected 'Expected Button Text' but got '{button.text}'"

            # หาองค์ประกอบที่เราต้องการตรวจสอบ
            element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[1]/p')
            # ใช้คำสั่ง if, elif, else เพื่อดำเนินการตามเงื่อนไข
            if element.text == 'โครงการ':
                print('ข้อความตรงกัน')
                # ทำสิ่งที่ต้องการเมื่อข้อความตรงกัน
            elif element.text == 'โครงการผิดพลาด':
                print('ข้อความเป็นอีกแบบ')
                # ทำสิ่งที่ต้องการเมื่อข้อความเป็นอีกแบบ
            else:
                print('ข้อความไม่ตรงกับเงื่อนไขใด ๆ')
                # ทำสิ่งที่ต้องการเมื่อข้อความไม่ตรงกับเงื่อนไขใด ๆ
            
            # คลิก

        except NoSuchElementException:
            self.fail('Element not Found')
        except AssertionError as e:
            self.fail(str(e))
        except Exception as n:
            self.fail(f'An unexpected error occurred: {n}')
        except TimeoutException as m:
            self.fail(f'การรอองค์ประกอบล้มเหลว: {m}')
        return resutl


    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()   

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



