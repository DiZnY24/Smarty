
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
from selenium.common.exceptions import NoSuchElementException ,TimeoutException


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



    def test_page_edit(self):
        # หน้า การบริหาร - ผู้ใช้งาน
        self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/units')
        self.driver.implicitly_wait(10)

        try:
            # แก้ไข 

            edit = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[8]/div/button'))
            )
            assert edit.is_displayed(), 'Element is not displayed!'
            assert edit.is_enabled(), 'Element is not enabled!'
            edit.click()
            time.sleep(1)
            
            # บ้านเลขที่

            home_number = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[1]/div[1]/div/div[2]/div/div/input'))
            )
            assert home_number.is_displayed(), 'Element is not displayed!'
            assert home_number.is_enabled(), 'Element is not enabled!'
            home_number.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            home_number.send_keys('99/1') 
            time.sleep(0.1)

            # ชั้น

            floor = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[1]/div[2]/div/div[2]/div/div/input'))
            )
            assert floor.is_displayed(), 'Element is not displayed!'
            assert floor.is_enabled(), 'Element is not enabled!'
            floor.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            floor.send_keys('01/02') 
            time.sleep(0.1)

            # เลขที่ห้อง

            number_home = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[1]/div[3]/div/div[2]/div/div/input'))
            )
            assert number_home.is_displayed(), 'Element is not displayed!'
            assert number_home.is_enabled(), 'Element is not enabled!'
            number_home.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            number_home.send_keys('134/06') 
            time.sleep(0.1)

            # ประเภท

            type = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[1]/div[4]/div[2]/div/div/div'))
            )
            assert type.is_displayed(), 'Element is not displayed!'
            assert type.is_enabled(), 'Element is not enabled!'
            type.click() 
            time.sleep(0.1)

            type = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[3]'))
            )
            assert type.is_displayed(), 'Element is not displayed!'
            assert type.is_enabled(), 'Element is not enabled!'
            type.click() 
            time.sleep(0.1)
            
            # ขนาดห้อง (ตร.ม.)

            Room_size = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[2]/div[1]/div/div[2]/div/div/input'))
            )
            assert Room_size.is_displayed(), 'Element is not displayed!'
            assert Room_size.is_enabled(), 'Element is not enabled!'
            Room_size.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Room_size.send_keys('35.ม') 
            time.sleep(0.1)
            
            # อัตราส่วนแห่งกรรมสิทธิ์ในทรัพย์สินส่วนกลาง

            Buy = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[2]/div[2]/div/div[2]/div/div/input'))
            )
            assert Buy.is_displayed(), 'Element is not displayed!'
            assert Buy.is_enabled(), 'Element is not enabled!'
            Buy.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Buy.send_keys('0.700000') 
            time.sleep(0.1)

            # Ref1

            Ref1 = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[2]/div[3]/div/div[2]/div/div/input'))
            )
            assert Ref1.is_displayed(), 'Element is not displayed!'
            assert Ref1.is_enabled(), 'Element is not enabled!'
            Ref1.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Ref1.send_keys('500002') 
            time.sleep(0.1)

            # Ref2

            Ref1 = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[2]/div[4]/div/div[2]/div/div/input'))
            )
            assert Ref1.is_displayed(), 'Element is not displayed!'
            assert Ref1.is_enabled(), 'Element is not enabled!'
            Ref1.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Ref1.send_keys('0102') 
            time.sleep(0.1)


        # Save

            # Save = WebDriverWait(self.driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[3]/button'))
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click() 


        except NoSuchElementException:
            self.fail('Element not Found')
        except AssertionError as e :
            self.fail(str(e))
        except Exception as n:
            self.fail(f'An unexpected error occurred:: {n}')
        
        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        try:
            # ที่อยู่จัดส่ง 

            address = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div[2]/div/button[2]'))
            )
            assert address.is_displayed(), 'Element is not displayed!'
            assert address.is_enabled(), 'Element is not enabled!'
            address.click() 
            time.sleep(0.5)

            # ประเภทที่อยู่จัดส่ง

            type_address = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[1]/div[2]/div/div/div'))
            )
            assert type_address.is_displayed(), 'Element is not displayed!'
            assert type_address.is_enabled(), 'Element is not enabled!'
            type_address.click() 
            time.sleep(0.1)

            type_address = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[2]'))
            )
            assert type_address.is_displayed(), 'Element is not displayed!'
            assert type_address.is_enabled(), 'Element is not enabled!'
            type_address.click() 
            time.sleep(0.1)
            
            # รายละเอียดที่อยู่

            Address_details = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[2]/div/div/input'))
                )
            assert Address_details.is_displayed(), 'Element is not displayed!'
            assert Address_details.is_enabled(), 'Element is not enabled!'
            Address_details.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Address_details.send_keys('5/0012')
            time.sleep(0.1)

            # ซอย

            road = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[3]/div[1]/div/div[2]/div/div/input'))
                )
            assert road.is_displayed(), 'Element is not displayed!'
            assert road.is_enabled(), 'Element is not enabled!'
            road.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            road.send_keys('-')
            time.sleep(0.1)

            # เลขที่ห้อง

            number_room = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[3]/div[2]/div/div[2]/div/div/input'))
                )
            assert number_room.is_displayed(), 'Element is not displayed!'
            assert number_room.is_enabled(), 'Element is not enabled!'
            number_room.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            number_room.send_keys('ถนนป๊อปปูล่า')
            time.sleep(0.1)
            
            # ตำบล

            district = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[4]/div[1]/div/div[2]/div/div/input'))
                )
            assert district.is_displayed(), 'Element is not displayed!'
            assert district.is_enabled(), 'Element is not enabled!'
            district.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            district.send_keys('บ้านใหม่')
            time.sleep(0.1)
            
            # อำเภอ

            district = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[4]/div[2]/div/div[2]/div/div/input'))
                )
            assert district.is_displayed(), 'Element is not displayed!'
            assert district.is_enabled(), 'Element is not enabled!'
            district.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            district.send_keys('ปากเกร็ด')
            time.sleep(0.1)

            # จังหวัด

            province = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[5]/div[1]/div/div[2]/div/div/input'))
                )
            assert province.is_displayed(), 'Element is not displayed!'
            assert province.is_enabled(), 'Element is not enabled!'
            province.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            province.send_keys('นนทบุรี')
            time.sleep(0.1)

            # รหัสไปรษณีย์

            province = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[5]/div[2]/div/div[2]/div/div/input'))
                )
            assert province.is_displayed(), 'Element is not displayed!'
            assert province.is_enabled(), 'Element is not enabled!'
            province.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            province.send_keys('11120')
            time.sleep(0.1)

            # Save

            # Save = WebDriverWait(self.driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/button'))
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click() 

    
        except NoSuchElementException:
            self.fail('Element not Found')
        except AssertionError as e:
            self.fail(str(e))
        except Exception as o:
            self.fail(f'An unexpected error occurred: {o}')

    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        try:
            # ชื่อออกเอกสาร 
            Name_of_document = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div[2]/div/button[3]'))
            )
            assert Name_of_document.is_displayed(), 'Element is not displayed!'
            assert Name_of_document.is_enabled(), 'Element is not enabled!'
            Name_of_document.click()
            time.sleep(0.5)
            
            # ชื่อ

            province = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[3]/div/form/div/div/div/div/div[1]/div/div/div/div/input'))
                )
            assert province.is_displayed(), 'Element is not displayed!'
            assert province.is_enabled(), 'Element is not enabled!'
            province.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            province.send_keys('นางสาวศิริพร,นางสุณี-')
            time.sleep(0.1)

            # Save
            
            # Save = WebDriverWait(self.driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[3]/div/form/div/div/div/div/div[2]/button'))
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click() 



        except NoSuchElementException:
            self.fail('Element not Found')
        except AssertionError as e:
            self.fail(str(e))
        except Exception as o:
            self.fail(f'An unexpected error occurred: {o}')   
          

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()   

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



