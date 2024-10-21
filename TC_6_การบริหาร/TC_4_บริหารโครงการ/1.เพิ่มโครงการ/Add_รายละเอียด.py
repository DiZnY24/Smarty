
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


    def test_page_add_bank1(self):
        
        try:
            # หน้า บริหารโครงการ
            self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/properties')
            self.driver.implicitly_wait(20)

            # เพิ่มโครงการ
            Project = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[1]/div[1]/div/button'))
            )
            assert Project.is_displayed(), 'Element is not displayed!'
            assert Project.is_enabled(), 'Element is not enabled!'
            Project.click()
            time.sleep(0.1)

            # รหัสอาคาร
        
            key_password = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_password.is_displayed(), 'Element is not displayed!'
            assert key_password.is_enabled(), 'Element is not enabled!'
            key_password.send_keys('DBL2')
            time.sleep(0.1)

            # ชื่อโครงการ (เต็ม)

            key_project = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_project.is_displayed(), 'Element is not displayed!'
            assert key_project.is_enabled(), 'Element is not enabled!'
            key_project.send_keys('นิติบุคคลอาคารชุด ดับเบิ้ลเลค คอนโดมิเนียม DBL2')
            time.sleep(0.1)
        

            # ชื่อโครงการ (ย่อ)

            key_project = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/div[3]/div/div[2]/div/div/input'))
            )
            assert key_project.is_displayed(), 'Element is not displayed!'
            assert key_project.is_enabled(), 'Element is not enabled!'
            key_project.send_keys('MTTD-DBL2')
            time.sleep(0.1)

            # เลขที่โครงการ

            key_project = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_project.is_displayed(), 'Element is not displayed!'
            assert key_project.is_enabled(), 'Element is not enabled!'
            key_project.send_keys('1')
            time.sleep(0.1)

            # ขนาดพื้นที่ (ไร่)

            key_number = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys('2')
            time.sleep(0.1)

            # เบอร์ติดต่อ

            Phone_number = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[3]/div[1]/div/div[2]/div/div/input'))
            )
            assert Phone_number.is_displayed(), 'Element is not displayed!'
            assert Phone_number.is_enabled(), 'Element is not enabled!'
            Phone_number.send_keys('0659373995')
            time.sleep(0.1)

            # เลขประจำตัวผู้เสียภาษี

            key_number = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[3]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys('0994001106649')
            time.sleep(0.1)

            # อีเมล

            key_gmail = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[3]/div[3]/div/div[2]/div/div/input'))
            )
            assert key_gmail.is_displayed(), 'Element is not displayed!'
            assert key_gmail.is_enabled(), 'Element is not enabled!'
            key_gmail.send_keys('doublelake@msm-muangthong.com')
            time.sleep(0.1)

            # เลขที่อยู่

            Address_number = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[4]/div[1]/div/div[2]/div/div/input'))
            )
            assert Address_number.is_displayed(), 'Element is not displayed!'
            assert Address_number.is_enabled(), 'Element is not enabled!'
            Address_number.send_keys('84 หมู่5')
            time.sleep(0.1)

            # อาคาร

            building = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div/div/input'))
            )
            assert building.is_displayed(), 'Element is not displayed!'
            assert building.is_enabled(), 'Element is not enabled!'
            building.send_keys('-')
            time.sleep(0.1)

            # ถนน

            road = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[4]/div[3]/div/div[2]/div/div/input'))
            )
            assert road.is_displayed(), 'Element is not displayed!'
            assert road.is_enabled(), 'Element is not enabled!'
            road.send_keys('-')
            time.sleep(0.1)

            # อยู่ที่

            road = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[5]/div/div/div/div[2]/div/div/input'))
            )
            assert road.is_displayed(), 'Element is not displayed!'
            assert road.is_enabled(), 'Element is not enabled!'
            road.send_keys('บ้านใหม่ / ปากเกร็ด / นนทบุรี / 11120' + Keys.ARROW_DOWN + Keys.ENTER)
            time.sleep(0.1)

            # บันทึก

            # Save = WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[2]/button'))
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
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



