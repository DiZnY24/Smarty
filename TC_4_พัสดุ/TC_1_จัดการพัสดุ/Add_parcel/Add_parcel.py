
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import pyautogui

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


    def test_page_parcel(self):
         
        try: 
            # หน้า ข่าวสาร
            self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/parcels')
            self.driver.implicitly_wait(30)

                    
            # กดปุ่มเพิ่มพัสดุ

            Add_parcel = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div/div[1]/button'))
            )
            assert Add_parcel.is_displayed(), 'Element is not displayed!'
            assert Add_parcel.is_enabled(), 'Element is not enabeld!'
            Add_parcel.click()

            # กรอกข้อมูล
            # อัพโหลดรูปภาพ Mac Os

            upload = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div[3]/div/div/div'))
            )
            print('Wait Show Element Upload Image :', True)

            upload = self.driver.find_element(by=By.XPATH , value='/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div[3]/div/div/input')
            upload.send_keys('/Users/dizny/Downloads/Image/image Test/Logo.jpg.jpg')

            # คลิกโครงการ

            Add_project = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div[4]/div[1]/div/div/div/div/div[2]/div/div/input'))
            )
            assert Add_project.is_displayed(), 'Element is not displayed!'
            assert Add_project.is_enabled(), 'Element is not enabeld!'
            Add_project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)     

            # คลิกชั้น / ห้อง

            room_floor = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div[4]/div[2]/div/div/div/div/div[2]/div/div')) 
            )
            assert room_floor.is_displayed(), 'Element is not displayed!'
            assert room_floor.is_enabled(), 'Element is not enabeld!'
            room_floor.click()    

            # พิมพ์ ชั้น / ห้อง

            room_floor = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div[4]/div[2]/div/div/div/div/div[2]/div/div/input')) 
            )
            assert room_floor.is_displayed(), 'Element is not displayed!'
            assert room_floor.is_enabled(), 'Element is not enabeld!'
            room_floor.send_keys('01/02' + Keys.ARROW_DOWN + Keys.ENTER)     

        
            # เลือก_ชื่อลูกบ้านที่ต้องการแจ้งเตือน

            time.sleep(2.5)
            # pyautogui.click(x=612, y=925)

            select = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div/div/div/form/div[2]/div[1]/div[1]/div/div[2]/div/div')) 
            )
            assert select.is_displayed(), 'Element is not displayed!'
            assert select.is_enabled(), 'Element is not enabeld!'
            select.click()   

            time.sleep(0.5)
            select = self.driver.find_element(by=By.XPATH, value='/html/body/div/div/main/div/div/div/div/form/div[2]/div[1]/div[1]/div/div[2]/div/div/div')
            
            select = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li')) 
            )
            assert select.is_displayed(), 'Element is not displayed!'
            assert select.is_enabled(), 'Element is not enabeld!'
            select.click()    
            select.send_keys(Keys.ESCAPE)

            # Key หมายเลขพัสดุ

            Key_number = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[2]/div[1]/div[2]/div/div/div[2]/div/div/input')) 
            )
            assert Key_number.is_displayed(), 'Element is not displayed!'
            assert Key_number.is_enabled(), 'Element is not enabeld!'
            Key_number.send_keys('16161616')     
        
            # # บริษัทขนส่ง

            Key_date = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[2]/div[1]/div[3]/div/div[2]/div/div/div')) 
            )
            assert Key_date.is_displayed(), 'Element is not displayed!'
            assert Key_date.is_enabled(), 'Element is not enabeld!'
            Key_date.click()    

            Key_date = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')) 
            )
            assert Key_date.is_displayed(), 'Element is not displayed!'
            assert Key_date.is_enabled(), 'Element is not enabeld!'
            Key_date.click()    

            # สถานะ

            status = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[2]/div[1]/div[4]/div/div[2]/div/div/div')) 
            )
            assert status.is_displayed(), 'Element is not displayed!'
            assert status.is_enabled(), 'Element is not enabeld!'
            status.click()    

            status = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[3]')) 
            )
            assert status.is_displayed(), 'Element is not displayed!'
            assert status.is_enabled(), 'Element is not enabeld!'
            status.click()    

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            
            # Save = WebDriverWait(self.driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[2]/div[2]/button')) 
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabeld!'

            # if Save:
            #     Save.click()    
            #     print('Save Already',True)
            # else:
            #     print('Cannot Save Already', False)
            
            # Show_Save = WebDriverWait(self.driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]')) 
            # )
            # print('Element Show Save Already :',True)


        except NoSuchElementException:
            self.fail('Element not Found',False)
        except AssertionError as e:
            self.fail(str(e))
        except Exception as o:
            self.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว',False)


    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit() 
        

if __name__ == '__main__':
    unittest.main()


# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\4.พัสดุ\\Reports'))