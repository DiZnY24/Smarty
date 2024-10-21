
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


    def test_page_add_bank2(self):

        try:
                # หน้า บริหารโครงการ
                self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/properties')
                self.driver.implicitly_wait(30)

                # เพิ่มโครงการ

                Project = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[1]/div[1]/div/button'))
                )
                assert Project.is_displayed(), 'Element is not displayed!'
                assert Project.is_enabled(), 'Element is not enabled!'
                Project.click()
                time.sleep(0.5)

                # บัญชีธนาคาร

                bank = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[1]/div[2]/div/button[2]'))
                )
                assert bank.is_displayed(), 'Element is not displayed!'
                assert bank.is_enabled(), 'Element is not enabled!'
                bank.click()
                time.sleep(0.1)

                button = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[1]/div[2]/div/button[2]')
                assert button.text == 'บัญชีธนาคาร', f"Expected 'Expected Button Text' but got '{button.text}'"
                time.sleep(0.1)

                wait_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/input")) 
                )
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1) 

                # ชื่อบัญชี

                Key_Text = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/input'))
                )
                assert Key_Text.is_displayed(), 'Element is not displayed!'
                assert Key_Text.is_enabled(), 'Element is not enabled!'
                Key_Text.send_keys('นิติบุคคลอาคารชุด ดับเบิ้ลเลค คอนโดมิเนียม เฟส 2')
                time.sleep(0.1)

                # ชนิดบัญชี
                
                Key_Text = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/input'))
                )
                assert Key_Text.is_displayed(), 'Element is not displayed!'
                assert Key_Text.is_enabled(), 'Element is not enabled!'
                Key_Text.send_keys('ออมทรัพย์')
                time.sleep(0.1)

                # ธนาคาร

                bank = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div/input'))
                )
                assert bank.is_displayed(), 'Element is not displayed!'
                assert bank.is_enabled(), 'Element is not enabled!'
                bank.send_keys('กสิกรไทย')
                time.sleep(0.1)
                
                # สาขา

                branch = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/input'))
                )
                assert branch.is_displayed(), 'Element is not displayed!'
                assert branch.is_enabled(), 'Element is not enabled!'
                branch.send_keys('สำนักแจ้งวัฒนะเมืองทองธานี')
                time.sleep(0.1)
                
                # เลขที่บัญชี

                number = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[3]/div/div/div[2]/div/div/input'))
                )
                assert number.is_displayed(), 'Element is not displayed!'
                assert number.is_enabled(), 'Element is not enabled!'
                number.send_keys('0053987656')
                time.sleep(0.1)


                # เลขประจำตัวผู้เสียภาษี
                # self.search_box = self.driver.find_element(By.XPATH, '')
                # self.search_box.send_keys('0994001106649')
                # time.sleep(0.1)
                
                # Suffix-code   

                number_code = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div/div/input'))
                )
                assert number_code.is_displayed(), 'Element is not displayed!'
                assert number_code.is_enabled(), 'Element is not enabled!'
                number_code.send_keys('72')
                time.sleep(0.1)
                
                # QR CODE

        #         Add_image = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[4]/div/div/div')
        #         self.assertTrue(Add_image.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
        #         self.assertTrue(Add_image.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
        #         Add_image.click()
        #         time.sleep(1)

                # อัพโหลดรูปภาพ

                # อัพโหลดรูปภาพ Mac Os
                upload = self.driver.find_element(by=By.XPATH , value='/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[4]/div/input')
                upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')
                time.sleep(1)

                # ใช้งาน Cross Bank

                Cross_bank = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[2]/label/span[1]'))
                )
                assert Cross_bank.is_displayed(), 'Element is not displayed!'
                assert Cross_bank.is_enabled(), 'Element is not enabled!'
                Cross_bank.click()
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
        # print('___Test Pass__')
        cls.driver.quit()   

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



