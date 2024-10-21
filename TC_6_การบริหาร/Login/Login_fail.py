
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


def Login_Smarty(driver):
        result = None
        time.sleep(1)

        try:
        # ป้อนรหัสผ่าน
            element = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div/div[1]/div/div[1]/p')
            expected_text = 'เบอร์โทรศัพท์ / รหัสพนักงาน'
            assert element.text == expected_text, f"ข้อความไม่ตรงกัน: คาดว่า '{expected_text}' แต่ได้ '{element.text}'"
            time.sleep(0.1)

            Key_Passwprd = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input')
            Key_Passwprd.send_keys('00000')

        # ตรวจสอบค่าที่ป้อนในกล่องข้อความ
            textbox_element = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input")  
            textbox_value = textbox_element.get_attribute("value")
            text_to_check = "00000"
            assert text_to_check in textbox_value, f"ไม่พบ '{text_to_check}' ในกล่องข้อความ"
            
            Click = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/button')  # ขอ OTP
            assert Click.is_displayed(), 'Element is not displayed!'
            assert Click.is_enabled(), 'Element is not enabled!'
            Click.click()  # คลิกขอ OTP

        # รอให้ Element คลิกได้  # คลิกขอ เข้าสู่ระบบ
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/button')) # คลิกขอ เข้าสู่ระบบ
            )
            assert element.is_displayed(), 'Element is not displayed!'
            assert element.is_enabled(), 'Element is not enabled!'
            element.click()
        # จับข้อผิดพลาดนี้เมื่อไม่พบองค์ประกอบ และเรียกใช้ self.fail() เพื่อบอกว่าการทดสอบล้มเหลว
        except NoSuchElementException:
            driver.fail('Element not Found')
        # จับข้อผิดพลาดเมื่อการตรวจสอบไม่สำเร็จ
        except AssertionError as e:
            driver.fail(str(e))
        # จับข้อผิดพลาดทั่วไปที่ไม่อยู่ในเงื่อนไขอื่น ๆ
        except Exception as o:
            driver.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว')
        
        try:
        # ทดสอบการคลิก Element
            result_elemet = driver.find_element(By.XPATH, '/html/body/div/div/main/nav/div/div/div/ul/div[3]/li/div/div[2]')    
            driver.assertIsNotNone(result_elemet)
        except NoSuchElementException as e:
            driver.fail('Element not Found')
        # การคืนค่าจากฟังก์ชันช่วยให้เราสามารถรู้สถานะของการล็อกอินได้ โดยในที่นี้คืนค่าที่แสดงว่าล็อกอินสำเร็จหรือไม่
        return result
  

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\1.Register\\Reports'))