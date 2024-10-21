
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException,TimeoutException


def page_transport(driver):

        try:
            # หน้า จัดการขนส่งพัสดุ
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/parcels/express')
            driver.implicitly_wait(30)

            # คลิก แอดเพิ่มขนส่ง

            Click_Button = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[1]/button')
            time.sleep(0.5)
            assert Click_Button.is_displayed(), 'Element is not displayed!'
            assert Click_Button.is_enabled(), 'Element is not enabled!'
            Click_Button.click() 

            # พิมชื่อขนส่งที่ต้องการ
            
            Key_name = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div/div/div/div[2]/div/div/input')
            time.sleep(0.5)
            assert Key_name.is_displayed(), 'Element is not displayed!'
            assert Key_name.is_enabled(), 'Element is not enabled!'
            Key_name.send_keys('Test_Kub' + Keys.ENTER)

            WaitElement = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[4]/div[2]/div'))
            )                
            print('Show Element Already :', True)

            element = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[4]/div[2]/div")  
            expected_text = "Test_Kub"
            actual_text = element.text

            if actual_text == expected_text:
                print("ข้อความถูกต้อง!")
            else:
                print("ข้อความไม่ถูกต้อง!")

        except NoSuchElementException:
            driver.fail('Element not Found')
        except AssertionError as e:
            driver.fail(str(e))
        except Exception as o:
            driver.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว')  
                    

if __name__ == '__main__':
    unittest.main()

          

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\4.พัสดุ\\Reports'))

   







