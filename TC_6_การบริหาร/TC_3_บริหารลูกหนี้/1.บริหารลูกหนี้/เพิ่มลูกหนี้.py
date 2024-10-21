
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

        wait = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div/div/div/div[3]/ul/div'))
            )
        print('รอจนหน้าเว็ปโหลดเสร็จ : Pass')

        print('-------------------------------')


    def test_page_add_debtor(self):
            
        try: 
    # หน้า การบริหาร - ผู้ใช้งาน
            self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/debtors')
            self.driver.implicitly_wait(30)

    # เพิ่มลูกหนี้

            Add = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[1]/button'))
            )
            assert Add.is_displayed(), 'Element is not displayed!'
            assert Add.is_enabled(), 'Element is not enabled!'
            Add.click() 
            time.sleep(0.1) 

    # คีย์ โครงการ

            key_projet = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[1]/div/div/div/div[2]/div/div/input'))
            )
            assert key_projet.is_displayed(), 'Element is not displayed!'
            assert key_projet.is_enabled(), 'Element is not enabled!'
            key_projet.click() 
            time.sleep(0.1) 

            key_projet = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[1]/div/div/div/div[2]/div/div/input'))
            )
            assert key_projet.is_displayed(), 'Element is not displayed!'
            assert key_projet.is_enabled(), 'Element is not enabled!'
            key_projet.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
            time.sleep(0.1)

            # ชั้น / ห้อง

    # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
            floor = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[2]/div/div/div/div[2]/div/div"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
    # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)

            click_floor = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[2]/div/div/div/div[2]/div/div'))
            )
            assert click_floor.is_displayed(), 'Element is not displayed!'
            assert click_floor.is_enabled(), 'Element is not enabled!'
            click_floor.click() 
            time.sleep(0.1)

            key_floor = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[2]/div/div/div/div[2]/div/div/input'))
            )
            assert key_floor.is_displayed(), 'Element is not displayed!'
            assert key_floor.is_enabled(), 'Element is not enabled!'
            key_floor.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)

    # # สถานะ

            status = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[2]/div[2]/div/div/div"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.5)

            # element = WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[2]/div[2]/div/div'))
            # )
            # self.assertTrue(element.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
            # self.assertTrue(element.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
            # element.click()

            click_status = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[2]/div[2]/div/div')
            click_status.click()

            time.sleep(1)

            click_status = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[1]'))
            )
            assert click_status.is_displayed(), 'Element is not displayed!'
            assert click_status.is_enabled(), 'Element is not enabled!'
            click_status.click() 

            time.sleep(1)

            element_2 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/button")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
            time.sleep(1)

    # Detele

            # delete = WebDriverWait(self.driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[6]/table/tbody/tr[1]/td[3]/button'))
            # )
            # assert delete.is_displayed(), 'Element is not displayed!'
            # assert delete.is_enabled(), 'Element is not enabled!'
            # delete.click() 
    # Save  

            # Save = WebDriverWait(self.driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/button'))
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click() 
            # time.sleep(1)
            # self.search_box = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/button')
            
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



