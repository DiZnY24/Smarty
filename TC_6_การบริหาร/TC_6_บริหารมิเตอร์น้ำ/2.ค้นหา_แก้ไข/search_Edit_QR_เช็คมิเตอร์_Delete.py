
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



    def test_page_search_edit(self):
                
        try:
                # หน้า จัดการลูกหนี้
                self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/water-meter')
                self.driver.implicitly_wait(10)


                # คีย์ โครงการ

                Input_Text = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
                )
                assert Input_Text.is_displayed(), 'Element is not displayed!'
                assert Input_Text.is_enabled(), 'Element is not enabled!'
                Input_Text.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
                Input_Text.send_keys('อาคาร C8' + Keys.ARROW_DOWN + Keys.ENTER)

                # คีย์ ชั้น / ห้อง

                floor = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/input'))
                )
                assert floor.is_displayed(), 'Element is not displayed!'
                assert floor.is_enabled(), 'Element is not enabled!'
                floor.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)

                # สถานะมิเตอร์

                status = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[3]/div[1]/div[2]/div/div/div')
                assert status.is_displayed(), 'Element is not displayed!'
                assert status.is_enabled(), 'Element is not enabled!'
                status.click()
                time.sleep(0.1)

                status = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]')
                assert status.is_displayed(), 'Element is not displayed!'
                assert status.is_enabled(), 'Element is not enabled!'
                status.click()

        
                # เลือกปี (สำหรับดาวโหลดประวัติการจดหน่วยน้ำ)

                Dete = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[1]/div[3]/div[2]/div/div/div')
                assert Dete.is_displayed(), 'Element is not displayed!'
                assert Dete.is_enabled(), 'Element is not enabled!'
                Dete.click()
                time.sleep(0.1)

                Dete1 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/div[125]/button')
                assert Dete1.is_displayed(), 'Element is not displayed!'
                assert Dete1.is_enabled(), 'Element is not enabled!'
                Dete1.click()
                
                # ตั้งแต่เดือน

                Since_the_month = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[4]/div[2]/div[1]/div/div')
                assert Since_the_month.is_displayed(), 'Element is not displayed!'
                assert Since_the_month.is_enabled(), 'Element is not enabled!'
                Since_the_month.click()
                time.sleep(0.1)

                Since_the_month_1 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[10]/button')
                assert Since_the_month.is_displayed(), 'Element is not displayed!'
                assert Since_the_month.is_enabled(), 'Element is not enabled!'
                Since_the_month_1.click() 
                time.sleep(0.1)

                Since_the_month_2 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/button')
                assert Since_the_month.is_displayed(), 'Element is not displayed!'
                assert Since_the_month.is_enabled(), 'Element is not enabled!'
                Since_the_month_2.send_keys(Keys.ESCAPE) 

                # ถึงเดือน
                To_the_month =self.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[1]/div[4]/div[2]/div[2]/div/div')
                assert Since_the_month.is_displayed(), 'Element is not displayed!'
                assert Since_the_month.is_enabled(), 'Element is not enabled!'
                To_the_month.click()
                time.sleep(0.1)
                
                To_the_month_1 =self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[10]/button')
                assert Since_the_month.is_displayed(), 'Element is not displayed!'
                assert Since_the_month.is_enabled(), 'Element is not enabled!'
                To_the_month_1.click()
                time.sleep(0.1)

                To_the_month = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/button')
                To_the_month.send_keys(Keys.ESCAPE)

                # เลขมิเตอร์

                number = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[4]/div[2]/div[3]/div/div[2]/div/div/input')
                number.send_keys('00000000')

        # Refresh
                # self.management =self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[4]/div[2]/div[4]/button')
                # self.management.click()
                # time.sleep(0.5)

        # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                                                                # ส่วนของแก้ไข
        # การจัดการ - แก้ไข 

                Edit = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/div/table/tbody/tr/td[8]/div/button[1]')
                assert Edit.is_displayed(), 'Element is not displayed!'
                assert Edit.is_enabled(), 'Element is not enabled!'
                Edit.click()
        
                time.sleep(1)  

        # คีย์ โครงการ

                # project = WebDriverWait(self.driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
                # )
                # assert project.is_displayed(), 'Element is not displayed!'
                # assert project.is_enabled(), 'Element is not enabled!'
                # time.sleep(2)

                Key_text = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
                )
                assert Key_text.is_displayed(), 'Element is not displayed!'
                assert Key_text.is_enabled(), 'Element is not enabled!'
                Key_text.send_keys(Keys.COMMAND + 'a' + Keys.DELETE) 
                Key_text.send_keys('อาคาร C8' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(1)

                # ชั้น / ห้อง

                floor_room = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/input'))
                )
                assert floor_room.is_displayed(), 'Element is not displayed!'
                assert floor_room.is_enabled(), 'Element is not enabled!'
                floor_room.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)

                # หมายเลขมิเตอร์น้ำ

                number = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[3]/div[1]/div/div[2]/div/div/input')
                assert number.is_displayed(), 'Element is not displayed!'
                assert number.is_enabled(), 'Element is not enabled!'
                number.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
                number.send_keys('950')

                # ขนาดมาตรน้ำ

                siez = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[3]/div[2]/div/div[2]/div/div/input')
                siez.send_keys('32') 

                # สถานะมิเตอร์

                status = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[3]/div[3]/div[2]/div/div/div')
                status.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                status.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                status.click()
                time.sleep(0.1) 

                status = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')
                status.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                status.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                status.click()  

                # วันที่ลงทะเบียน

                button = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[4]/div/div/div')
                assert button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                assert button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                button.click()
                time.sleep(0.1)

                button1 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[4]')
                assert button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                assert button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                button1.click()

                element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[1]/div[2]/div/button[1]')) 
                )
                assert element.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert element.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                element.click()         
                time.sleep(0.1)


        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                                                                        # ส่วนของ QR Cord
        # รอให้ Element คลิกได้  # คลิก QR Cord
                click_QR_Code = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/div/table/tbody/tr/td[8]/div/button[2]')) # คลิกขอ เข้าสู่ระบบ
                )
                assert click_QR_Code.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert click_QR_Code.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                click_QR_Code.click()
                time.sleep(0.1)

                element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button')) 
                )
                element.send_keys(Keys.ESCAPE)
                time.sleep(0.1)

                
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                                                                        # ส่วนของ 

        # รอให้ Element คลิกได้  # คลิก QR Cord

                QR_Code = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/div/table/tbody/tr/td[8]/div/button[3]')) # คลิกขอ เข้าสู่ระบบ
                )
                assert QR_Code.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert QR_Code.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                QR_Code.click()
                time.sleep(0.1)

        # เลือกปี
                select = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[3]/div[1]/div/div/div')) 
                )
                assert select.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert select.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                select.click()
                time.sleep(0.1)

                select = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/div[125]/button')) 
                )
                assert select.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert select.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                select.click()
                time.sleep(0.1)

                back = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/div[125]/button')
                back.send_keys(Keys.ESCAPE)
                time.sleep(0.1)

                back = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/button')) 
                )
                assert back.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert back.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                back.click()
                time.sleep(0.1)



        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                                                                        # ส่วน Button Delete
                button_delete = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/div/table/tbody/tr/td[8]/div/button[4]')) 
                )
                assert button_delete.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert button_delete.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                button_delete.click()
                time.sleep(0.1)

                # delete = WebDriverWait(self.driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]')) 
                # )
                # assert delete.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                # assert delete.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                # delete.click()
                # time.sleep(0.1)

                cancel = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[1]')) 
                )
                assert cancel.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert cancel.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                cancel.click()
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





