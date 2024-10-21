
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



    def test_page_add_receipt(self):

        try:
                self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/receipt')
                self.driver.implicitly_wait(30)

        # สร้างใบแจ้งหนี้ - สร้างใบแจ้งหนี้ รายบุคคล    
                create = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[1]/div/button[1]'))
                )
                assert create.is_displayed(), 'Element is not displayed!'
                assert create.is_enabled(), 'Element is not enabled!'
                create.click()
                time.sleep(0.1) 

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/form/div/div/div[2]/div[1]/div[1]/div/div/div/div/div[2]/div/div"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

        # โครงการ
                project = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[2]/div[1]/div[1]/div/div/div/div/div[2]/div/div/input'))
                )
                assert project.is_displayed(), 'Element is not displayed!'
                assert project.is_enabled(), 'Element is not enabled!'
                project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.1)

        # วันชำระ

                date_buy = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[2]/div[1]/div[2]/div/div/div'))
                )
                assert date_buy.is_displayed(), 'Element is not displayed!'
                assert date_buy.is_enabled(), 'Element is not enabled!'
                date_buy.click()
                time.sleep(0.1)

                date_buy = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/button[3]'))
                )
                assert date_buy.is_displayed(), 'Element is not displayed!'
                assert date_buy.is_enabled(), 'Element is not enabled!'
                date_buy.click()
                time.sleep(1)

        # ชั้น ห้อง
                floor_room = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[2]/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
                )
                assert floor_room.is_displayed(), 'Element is not displayed!'
                assert floor_room.is_enabled(), 'Element is not enabled!'
                floor_room.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(1)

        # รหัส

                password = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr/td[1]/div/div/div/div'))
                )
                assert password.is_displayed(), 'Element is not displayed!'
                assert password.is_enabled(), 'Element is not enabled!'
                password.click()
                time.sleep(0.5)

                key_text = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr/td[1]/div/div/div/div/input'))
                )
                assert key_text.is_displayed(), 'Element is not displayed!'
                assert key_text.is_enabled(), 'Element is not enabled!'
                key_text.send_keys('001' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.1)

        # เพิ่มรายการ 2 

                Add = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[4]/div[1]/button'))
                )
                assert Add.is_displayed(), 'Element is not displayed!'
                assert Add.is_enabled(), 'Element is not enabled!'
                Add.click()
                time.sleep(0.5)

                # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr[2]/td[1]/div/div/div/div/input"))  
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

        # รหัส

                key_text = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr[2]/td[1]/div/div/div/div/input'))
                )
                assert key_text.is_displayed(), 'Element is not displayed!'
                assert key_text.is_enabled(), 'Element is not enabled!'
                key_text.send_keys('002' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.1)

        # เพิ่มรายการ 3 

                Add = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[4]/div[1]/button'))
                )
                assert Add.is_displayed(), 'Element is not displayed!'
                assert Add.is_enabled(), 'Element is not enabled!'
                Add.click()
                time.sleep(0.1)

                # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr[3]/td[1]/div/div/div/div/input"))  
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

        # รหัส

                key_text = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr[3]/td[1]/div/div/div/div/input'))
                )
                assert key_text.is_displayed(), 'Element is not displayed!'
                assert key_text.is_enabled(), 'Element is not enabled!'
                key_text.send_keys('003' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.1)

        # กดลบ Delete

                # Delete = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr[2]/td[8]/button')  # ลบ 2
                # Delete.click()
                # time.sleep(0.1)

                # Delete = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr[1]/td[8]/button')  # ลบ 1
                # Delete.click()
                # time.sleep(0.1)

        # รูปแบบการชำระเงิน

                type_buy = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[5]/div[1]/div[1]/div[2]/div/label[2]/span[1]'))
                )
                assert type_buy.is_displayed(), 'Element is not displayed!'
                assert type_buy.is_enabled(), 'Element is not enabled!'
                type_buy.click()
                time.sleep(0.1)

        # หมายเหตุ

                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)

                key_text = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[5]/div[1]/div[2]/div/div/div/div/div/input'))
                )
                assert key_text.is_displayed(), 'Element is not displayed!'
                assert key_text.is_enabled(), 'Element is not enabled!'
                key_text.send_keys('Test')
                time.sleep(0.1)

                self.driver.execute_script("window.scrollTo(0, 0);")    
                time.sleep(1)

        # ยกเลิก

                cancel = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[1]/div[2]/div/button[1]'))
                )
                assert cancel.is_displayed(), 'Element is not displayed!'
                assert cancel.is_enabled(), 'Element is not enabled!'
                cancel.click()
                time.sleep(0.1)

        # บันทึก

                # button1 = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[1]/div[2]/div/button[2]')
                # self.assertTrue(button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า")
                # self.assertTrue(button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
                # button1.click()
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
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



