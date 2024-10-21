
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
from  selenium.common.exceptions import NoSuchElementException,TimeoutException
from datetime import datetime





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



    def test_page_serach_edit(self):
        
        try:
                # หน้า จัดการลูกหนี้
                self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/receipt')
                self.driver.implicitly_wait(10)
                time.sleep(0.1)
        
        # คีย์ โครงการ

                key_project = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div[2]/div/div/input'))
                )
                assert key_project.is_displayed(), 'Element is not displayed!'
                assert key_project.is_enabled(), 'Element is not enabled!'
                key_project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.1)

        # คีย์ ชั้น / ห้อง

                floor_room = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div/input'))
                )
                assert floor_room.is_displayed(), 'Element is not displayed!'
                assert floor_room.is_enabled(), 'Element is not enabled!'
                floor_room.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.1)

        # คีย์ สถานะการชำระเงิน
                status_buy = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div'))
                )
                assert status_buy.is_displayed(), 'Element is not displayed!'
                assert status_buy.is_enabled(), 'Element is not enabled!'
                status_buy.click()
                time.sleep(0.2)

                status_buy = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
                )
                assert status_buy.is_displayed(), 'Element is not displayed!'
                assert status_buy.is_enabled(), 'Element is not enabled!'
                status_buy.click()
                time.sleep(0.1)

        # วันที่ วันชำระ (เริ่มต้น)

                Date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div'))
                )
                assert Date.is_displayed(), 'Element is not displayed!'
                assert Date.is_enabled(), 'Element is not enabled!'
                Date.click()
                time.sleep(0.1)

                Date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[3]'))
                )
                assert Date.is_displayed(), 'Element is not displayed!'
                assert Date.is_enabled(), 'Element is not enabled!'
                Date.click()
                time.sleep(0.1)

        # วันชำระ (สิ้นสุด)

                Date_buy = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div/div'))
                )
                assert Date_buy.is_displayed(), 'Element is not displayed!'
                assert Date_buy.is_enabled(), 'Element is not enabled!'
                Date_buy.click()
                time.sleep(0.1)

                Date_buy = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[7]'))
                )
                assert Date_buy.is_displayed(), 'Element is not displayed!'
                assert Date_buy.is_enabled(), 'Element is not enabled!'
                Date_buy.click()
                time.sleep(0.1)

        # วันที่สร้างเอกสาร (เริ่มต้น)

                date_create = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div/div/div'))
                )
                assert date_create.is_displayed(), 'Element is not displayed!'
                assert date_create.is_enabled(), 'Element is not enabled!'
                date_create.click()
                time.sleep(0.1)

                date_create = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[3]'))
                )
                assert date_create.is_displayed(), 'Element is not displayed!'
                assert date_create.is_enabled(), 'Element is not enabled!'
                date_create.click()
                time.sleep(0.1)

        # วันที่สร้างเอกสาร (สิ้นสุด)

                date_create = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div'))
                )
                assert date_create.is_displayed(), 'Element is not displayed!'
                assert date_create.is_enabled(), 'Element is not enabled!'
                date_create.click()
                time.sleep(0.1)

                date_create = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[7]'))
                )
                assert date_create.is_displayed(), 'Element is not displayed!'
                assert date_create.is_enabled(), 'Element is not enabled!'
                date_create.click()
                time.sleep(1)

        # ช่องทางการสร้างเอกสาร

                create = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div[2]/div/div/div'))
                )
                assert create.is_displayed(), 'Element is not displayed!'
                assert create.is_enabled(), 'Element is not enabled!'
                create.click()
                time.sleep(0.1)

                create = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[3]'))
                )
                assert create.is_displayed(), 'Element is not displayed!'
                assert create.is_enabled(), 'Element is not enabled!'
                create.click()
                time.sleep(0.1)

        # ประเภท

                type = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[4]/div[2]/div/div/div'))
                )
                assert type.is_displayed(), 'Element is not displayed!'
                assert type.is_enabled(), 'Element is not enabled!'
                type.click()
                time.sleep(0.1)

                type = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
                )
                assert type.is_displayed(), 'Element is not displayed!'
                assert type.is_enabled(), 'Element is not enabled!'
                type.click()
                time.sleep(0.1)

        # เลขที่เอกสาร

                number = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[1]/div/div[2]/div/div/input'))
                )
                assert number.is_displayed(), 'Element is not displayed!'
                assert number.is_enabled(), 'Element is not enabled!'
                number.send_keys('H2024096100045')
                time.sleep(0.1)

        # ชื่อ

                number = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[2]/div/div[2]/div/div/input'))
                )
                assert number.is_displayed(), 'Element is not displayed!'
                assert number.is_enabled(), 'Element is not enabled!'
                number.send_keys('นายบุญเลิศ ชูอนุรักษ์')
                time.sleep(0.1)

        # Refresh

                Refresh = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[3]/button')
                Refresh.click()


        # # ค้นหา element ที่ต้องการให้มองเห็น
        #         element_2 = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[10]/div/div/button")

        # # ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
        #         self.driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
        #         time.sleep(1)

        # สถานะการชำระเงิน

                status_buy = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[10]/div/div/button'))
                )
                assert status_buy.is_displayed(), 'Element is not displayed!'
                assert status_buy.is_enabled(), 'Element is not enabled!'
                status_buy.click()
                time.sleep(0.1)


        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/ul/li[1]"))  
                                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

        # พิมพ์ PDF 

                print_PDF = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
                )
                assert print_PDF.is_displayed(), 'Element is not displayed!'
                assert print_PDF.is_enabled(), 'Element is not enabled!'
                print_PDF.click()
                time.sleep(5)

                if print_PDF:
                       print("Click print pdf already :",True)
                else:
                       print("Cannot Click print pdf :",False)

        # ยกเลิกใบเสร็จ

                # cancel = WebDriverWait(self.driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]'))
                # )
                # assert cancel.is_displayed(), 'Element is not displayed!'
                # assert cancel.is_enabled(), 'Element is not enabled!'
                # cancel.click()
                # time.sleep(2)

                # if print_PDF:
                #     print("Click cancel already :",True)
                # else:
                #     print("Cannot Click cancel :",False)

                # Click = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')
                # Click.click()
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



