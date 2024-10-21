
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




    def test_page_edit(self):
        # หน้า การบริหาร - ผู้ใช้งาน
        self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/properties')
        self.driver.implicitly_wait(30)

        try:
            # แก้ไข

            click_edit = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/button'))
            )
            assert click_edit.is_displayed(), 'Element is not displayed!'
            assert click_edit.is_enabled(), 'Element is not enabled!'
            click_edit.click()
            time.sleep(0.3)
            
            # รหัสอาคาร

            key_number = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)  
            key_number.send_keys('DBL1')
            time.sleep(0.3)
            
            # ชื่อโครงการ (เต็ม)        

            key_project = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_project.is_displayed(), 'Element is not displayed!'
            assert key_project.is_enabled(), 'Element is not enabled!'
            key_project.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)  
            key_project.send_keys('นิติบุคคลอาคารชุด ดับเบิ้ลเลค DBL1')
            time.sleep(0.1)

            # ชื่อโครงการ (ย่อ)

            key_name_project = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/div[3]/div/div[2]/div/div/input'))
            )
            assert key_name_project.is_displayed(), 'Element is not displayed!'
            assert key_name_project.is_enabled(), 'Element is not enabled!'
            key_name_project.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)  
            key_name_project.send_keys('MTTD-DBL1')
            time.sleep(0.1)

            # เลขที่โครงการ

            key_name_project = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_name_project.is_displayed(), 'Element is not displayed!'
            assert key_name_project.is_enabled(), 'Element is not enabled!'
            key_name_project.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)  
            key_name_project.send_keys('3')
            time.sleep(0.1)

            # ขนาดพื้นที่ (ไร่)

            key_number = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)  
            key_number.send_keys('5')
            time.sleep(0.1)

            # เบอร์ติดต่อ

            key_phone_number = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[3]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_phone_number.is_displayed(), 'Element is not displayed!'
            assert key_phone_number.is_enabled(), 'Element is not enabled!'
            key_phone_number.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)  
            key_phone_number.send_keys('0659373999')
            time.sleep(0.1)
            
            # เลขประจำตัวผู้เสียภาษี
            
            key_number = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[3]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)  
            key_number.send_keys('0994001106111')
            time.sleep(0.1)

            # อีเมล

            key_gmail = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[3]/div[3]/div/div[2]/div/div/input'))
                )
            assert key_gmail.is_displayed(), 'Element is not displayed!'
            assert key_gmail.is_enabled(), 'Element is not enabled!'
            key_gmail.send_keys(Keys.COMMAND + 'a' + Keys.DELETE) 
            key_gmail.send_keys('doe@msm-muangthong.com')
            time.sleep(0.1)

            # เลขที่อยู่

            Address_number = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[4]/div[1]/div/div[2]/div/div/input'))
                )
            assert Address_number.is_displayed(), 'Element is not displayed!'
            assert Address_number.is_enabled(), 'Element is not enabled!'
            Address_number.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Address_number.send_keys('100 หมู่6')
            time.sleep(0.1)

            # อาคาร

            building = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div/div/input'))
                )
            assert building.is_displayed(), 'Element is not displayed!'
            assert building.is_enabled(), 'Element is not enabled!'
            building.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            building.send_keys('-')
            time.sleep(0.1)

            # ถนน

            road = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[4]/div[3]/div/div[2]/div/div/input'))
                )
            assert road.is_displayed(), 'Element is not displayed!'
            assert road.is_enabled(), 'Element is not enabled!'
            road.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            road.send_keys('-')
            time.sleep(0.1)

            # อยู่ที่

            Address_number = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[5]/div/div/div/div[2]/div/div/input'))
                )
            assert Address_number.is_displayed(), 'Element is not displayed!'
            assert Address_number.is_enabled(), 'Element is not enabled!'
            Address_number.send_keys('บางตะไนย์ / ปากเกร็ด / นนทบุรี / 11120' + Keys.ARROW_DOWN )
            time.sleep(0.1)

            ESC = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[5]/div/div/div/div[2]/div/div/input')
            ESC.send_keys(Keys.ESCAPE)
            time.sleep(0.1)

            # Save

            # Save = WebDriverWait(self.driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/button'))
            #     )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click()
            # time.sleep(0.1)
            

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            

            # บัญชีธนาคาร

            bank = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[1]/div[2]/div/button[2]'))
            )
            assert bank.is_displayed(), 'Element is not displayed!'
            assert bank.is_enabled(), 'Element is not enabled!'  
            bank.click()
            time.sleep(0.5)

            # ชื่อบัญชี

            key_name = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_name.is_displayed(), 'Element is not displayed!'
            assert key_name.is_enabled(), 'Element is not enabled!'  
            key_name.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            key_name.send_keys('นิติบุคคลอาคารชุด ดับเบิ้ลเลค คอนโดมิเนียม เฟส 2')
            time.sleep(0.5)
            
            # ชนิดบัญชี
            
            key_bank = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_bank.is_displayed(), 'Element is not displayed!'
            assert key_bank.is_enabled(), 'Element is not enabled!'  
            key_bank.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            key_bank.send_keys('ออมทรัพย์')
            time.sleep(0.5)


            # ธนาคาร

            self.search_box = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div/input')
            self.search_box.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            self.search_box.send_keys('กสิกรไทย')
            time.sleep(0.1)

            # สาขา
            self.search_box = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/input')
            self.search_box.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            self.search_box.send_keys('สำนักแจ้งวัฒนะเมืองทองธานี')
            time.sleep(0.1)

            # เลขที่บัญชี
            self.search_box = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[3]/div/div/div[2]/div/div/input')
            self.search_box.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            self.search_box.send_keys('0053987656')
            time.sleep(0.1)

            # เลขประจำตัวผู้เสียภาษี
            # self.search_box = self.driver.find_element(By.XPATH, '')
            # self.search_box.send_keys('0994001106649')
            # time.sleep(0.1)
            
            # Suffix-code   
            self.search_box = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div/div/input')
            self.search_box.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            self.search_box.send_keys('72')
            time.sleep(0.1)

            # QR CODE

            # Add_image = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[4]/div/div/div')
            # Add_image.click()
            # time.sleep(1)

            # อัพโหลดรูปภาพ
            # อัพโหลดรูปภาพ Mac Os
            upload = self.driver.find_element(by=By.XPATH , value='/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[4]/div/input')
            upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')
            time.sleep(0.1)

            # ใช้งาน Cross Bank
            Click = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[2]/label/span[1]')
            Click.click()

            # บันทึก
            # Save = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[2]/button').click()

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            # ตั้งค่าการเรียกเก็บ
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[1]/div[2]/div/button[3]'))
            )
            element.click()
            time.sleep(1)

            # เพิ่มโครงการ
            Add_ = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[4]/div/div/button')
            Add_.click()
            time.sleep(1)

            # รหัส
            self.Key_Text = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[1]/div[1]/div/div[2]/div/div/input')
            # self.Key_Text.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            self.Key_Text.send_keys('123')
            time.sleep(0.3)
            
            # ชื่อรายการ
            self.Key_Text = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[1]/div[2]/div/div[2]/div/div/input')
            # self.Key_Text.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            self.Key_Text.send_keys('test')
            time.sleep(0.3)

            # จำนวนหน่วย
            self.Key_Text = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[1]/div[3]/div/div[2]/div/div/input')
            # self.Key_Text.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            self.Key_Text.send_keys('20')
            time.sleep(0.3)

            # ส่วนลด
            self.Key_Text = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[1]/div[4]/div/div[2]/div/div/input')
            # self.Key_Text.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
            self.Key_Text.send_keys('5')
            time.sleep(0.3)

            # ราคาต่อหน่วย - ห้องอยู่อาศัย
            self.Key_Text = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/div[1]/div/div[2]/div/div/input')
            # self.Key_Text.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
            self.Key_Text.send_keys('1')
            time.sleep(0.3)

            # ราคาต่อหน่วย - ห้องร้านค้า
            self.Key_Text = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/div[2]/div/div[2]/div/div/input')
            # self.Key_Text.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
            self.Key_Text.send_keys('1')
            time.sleep(0.3)

            # ราคาต่อหน่วย - ห้องพิเศษ
            self.Key_Text = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/div[3]/div/div[2]/div/div/input')
            # self.Key_Text.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
            self.Key_Text.send_keys('1')
            time.sleep(0.3)

            # เรียกเก็บรายเดือน
            Add_ = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/label/span[1]')
            Add_.click()
            time.sleep(0.3)

            # ยกเลิก
            # cancel = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[3]/button[1]')
            # cancel.click()
            # time.sleep(0.3)

            # # ยืนยัน
            # confirm = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[3]/button[2]')
            # confirm.click()
            # time.sleep(0.3)

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
        print('___Test Pass__')
        cls.driver.quit()   

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



