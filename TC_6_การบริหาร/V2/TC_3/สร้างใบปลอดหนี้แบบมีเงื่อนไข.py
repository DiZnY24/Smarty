
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


def test_page_create(driver):

        try:
            # หน้า จัดการลูกหนี้
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/debtors')
            driver.implicitly_wait(10)
            time.sleep(1)

    # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[8]/div/div"))  
            )
    # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)


            # สร้างใบปลอดหนี้แบบมีเงื่อนไข

            management = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[8]/div/div')) 
            )
            assert management.is_displayed(), 'Element is not displayed!'
            assert management.is_enabled(), 'Element is not enabled!'
            management.click()
            time.sleep(0.5)

            management = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')) 
            )
            assert management.is_displayed(), 'Element is not displayed!'
            assert management.is_enabled(), 'Element is not enabled!'
            management.click()
            time.sleep(0.1)


    # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[1]/div/div/div")) 
            )
    # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)
            

            # วันที่ กรอกฟอร์ม

            Date = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[1]/div/div/div')) 
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            Date = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//div/div/div/div[2]/div/div[2]/div/div/div[10]/button')) 
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            Date = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[125]/button')) 
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.send_keys(Keys.ESCAPE)
            time.sleep(0.1)


            # Input Text ข้าพเจ้าบริษัท

            Input_Text = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[2]/div/div/input')) 
            )
            assert Input_Text.is_displayed(), 'Element is not displayed!'
            assert Input_Text.is_enabled(), 'Element is not enabled!'
            Input_Text.send_keys('Impact')
            time.sleep(0.1)

            # Input Text  โดย

            Input_Text = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[3]/div/div/input')) 
            )
            assert Input_Text.is_displayed(), 'Element is not displayed!'
            assert Input_Text.is_enabled(), 'Element is not enabled!'
            Input_Text.send_keys(Keys.CONTROL + 'a' + Keys.DELETE) 
            Input_Text.send_keys('อาม ม่อน เสิน 23')
            time.sleep(0.1)

            # Input Text มีภาระหนี้สินจำนวน

            Input_Text = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[5]/div[3]/div/input')) 
            )
            assert Input_Text.is_displayed(), 'Element is not displayed!'
            assert Input_Text.is_enabled(), 'Element is not enabled!'
            Input_Text.send_keys('1500')
            time.sleep(0.1)

            # Input Text ลงชื่อ ผู้จัดการนิติบุคคลอาคารชุด

            Input_Text = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[7]/div/div/div/input')) 
            )
            assert Input_Text.is_displayed(), 'Element is not displayed!'
            assert Input_Text.is_enabled(), 'Element is not enabled!'
            Input_Text.send_keys('Test')
            time.sleep(0.1)


            # วันที่ 1. นับตั้งจดทะเบียนนิติบุคคลอาคารชุด - วันที่

            Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[4]/div/div/div'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/button[4]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)
        
            Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[4]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.send_keys(Keys.ESCAPE)
            time.sleep(0.1)       

            # วันที่ 2. ระหว่างวันที่

            Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[5]/div[1]/div/div'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/button[5]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)
        
            Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/button[5]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.send_keys(Keys.ESCAPE)
            time.sleep(0.1)       

            # วันที่ - วันที่

            Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[5]/div[2]/div/div'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/button[6]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)
        
            Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/button[6]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.send_keys(Keys.ESCAPE)
            time.sleep(0.1)       

    # วันที่ 3. ระหว่างวันที่


            Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[1]/div[6]/div/div/div'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/button[7]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)
        
            Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/button[7]'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.send_keys(Keys.ESCAPE)
            time.sleep(0.1)       

    # เช็คข้อความในปุ่ม Back - บันทึก 
            button = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[2]/button[1]')
            assert button.text == 'ยกเลิก', f"Expected 'Expected Button Text' but got '{button.text}'"
            time.sleep(0.1)

            button = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[2]/button[2]')
            assert button.text == 'บันทึก', f"Expected 'Expected Button Text' but got '{button.text}'"
            time.sleep(0.1)

    # Button Save 

            # Save = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[2]/button[2]'))
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click()
            # time.sleep(0.1)   

    # Button ยกเลิก

            cancel = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div/div[2]/button[1]'))
            )
            assert cancel.is_displayed(), 'Element is not displayed!'
            assert cancel.is_enabled(), 'Element is not enabled!'
            cancel.click()
            time.sleep(0.1)   
        
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
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



