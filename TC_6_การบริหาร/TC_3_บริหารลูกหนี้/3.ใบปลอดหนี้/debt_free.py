
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


    def test_page_debt_free(self):
        
        try:
            # หน้า จัดการลูกหนี้
            self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/debtors')
            self.driver.implicitly_wait(10)

            # คลิก ใบปลอดหนี้

            click = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div/div/button[2]'))
            )
            assert click.is_displayed(), 'Element is not displayed!'
            assert click.is_enabled(), 'Element is not enabled!'
            click.click()
            time.sleep(0.1)

    # เช็คข้อความในปุ่ม - ดาวน์โหลด 
            button = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[1]/button')
            assert button.text == 'ดาวน์โหลด', f"Expected 'Expected Button Text' but got '{button.text}'"
            time.sleep(0.1)


            element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)

            # โครงการ

            Project = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/input'))
            )
            assert Project.is_displayed(), 'Element is not displayed!'
            assert Project.is_enabled(), 'Element is not enabled!'
            Project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
            time.sleep(0.1)

            # คีย์ ชั้น / ห้อง

            floor_room = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div'))
            )
            assert floor_room.is_displayed(), 'Element is not displayed!'
            assert floor_room.is_enabled(), 'Element is not enabled!'
            floor_room.click()
            time.sleep(0.1)

            element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/input"))  
            )

            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)

            floor_room = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/input'))
            )
            assert floor_room.is_displayed(), 'Element is not displayed!'
            assert floor_room.is_enabled(), 'Element is not enabled!'
            floor_room.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)
            time.sleep(0.1)

            # ค้นหารายชื่อ

            Key_name = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/input'))
            )
            assert Key_name.is_displayed(), 'Element is not displayed!'
            assert Key_name.is_enabled(), 'Element is not enabled!'
            Key_name.send_keys('นายนิธิศ สมทรัพย์เสถียร')
            time.sleep(0.1)

    # สถานะ

            status = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div'))
            )
            assert status.is_displayed(), 'Element is not displayed!'
            assert status.is_enabled(), 'Element is not enabled!'
            status.click()
            time.sleep(0.1)

            status = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[3]'))
            )
            assert status.is_displayed(), 'Element is not displayed!'
            assert status.is_enabled(), 'Element is not enabled!'
            status.click()
            time.sleep(0.1)
            
    # เลขที่เอกสาร

            Document_number = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/div[2]/div/div/input'))
            )
            assert Document_number.is_displayed(), 'Element is not displayed!'
            assert Document_number.is_enabled(), 'Element is not enabled!'
            Document_number.send_keys('2024085400001')
            time.sleep(0.1)        

    # Refresh

            Refresh = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/button'))
            )
            assert Refresh.is_displayed(), 'Element is not displayed!'
            assert Refresh.is_enabled(), 'Element is not enabled!'
            Refresh.click()
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



