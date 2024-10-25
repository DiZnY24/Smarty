
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
import pyautogui

def page_pending(driver):
        
# *** เปิดหน้า รายชื่อคนลงทะเบียน (รออนุมัติ) ***
        driver.get('https://msm-smarty-cms-staging.hr-impact.co/pre-register/pending')
        driver.implicitly_wait(10)
        time.sleep(0.3)

        try: 
            # คลิกเลือกตึก
            select_building = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div[1]/div[1]/div/div/div/div/input')) 
            )
            assert select_building.is_displayed(), 'Element is not displayed!'
            select_building.send_keys('อาคาร C1' + Keys.ARROW_DOWN + Keys.ENTER + Keys.ESCAPE)
            
            input_key = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[1]/div/div/div/div/input')
            input_value = input_key.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}')     

            # พิมพ์ ชั้น / ห้อง

            floor_room = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div/div')) 
            )
            assert floor_room.is_displayed(), 'Element is not displayed!'
            assert floor_room.is_enabled(), 'Element is not enabled!'
            floor_room.click()

            floor_room = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div/div/input')) 
            )
            assert floor_room.is_displayed(), 'Element is not displayed!'
            floor_room.send_keys('04/02' + Keys.ARROW_DOWN + Keys.ENTER)
            
    
            input_key = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div/div/input')
            input_value = input_key.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}')  

            # ค้นหาจาก ชื่อ / นามสกุล / เลขบัตรประชาชน
            Search_by_name = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/input')) 
            )
            assert Search_by_name.is_displayed(), 'Element is not displayed!'
            Search_by_name.send_keys('0935909660' + Keys.ARROW_DOWN + Keys.ENTER)
        
            input_key = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/input')
            input_value = input_key.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}')  

            # คลิกวันที่สร้าง 
            date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[3]/div[1]/div/div')) 
            )
            assert date.is_displayed(), 'Element is not displayed!'
            assert date.is_enabled(), 'Element is not enabled!'
            date.click()

            # เลือกวันที่

            time.sleep(0.5)
            pyautogui.click(x=781, y=627)
            # time.sleep(5)  # ปรับเวลาตามความต้องการ        
            # current_position = pyautogui.position()
            # print(f"The current mouse position is: {current_position}")

            # date = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, 
            # '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[2]')) 
            # )
            # assert date.is_displayed(), 'Element is not displayed!'
            # assert date.is_enabled(), 'Element is not enabled!'
            # date.click()      

            # วันที่สิ้นสุด
            date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div')) 
            )
            assert date.is_displayed(), 'Element is not displayed!'
            assert date.is_enabled(), 'Element is not enabled!'
            date.click()

            # เลือกวันที่

            time.sleep(0.5)
            pyautogui.click(x=781, y=700)
            # element = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, 
            # '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[2]')) 
            # )
            # assert element.is_displayed(), 'Element is not displayed!'
            # assert element.is_enabled(), 'Element is not enabled!'
            # element.click()
            
            # บทบาท
            Role = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div/div/div')) 
            )
            assert Role.is_displayed(), 'Element is not displayed!'
            assert Role.is_enabled(), 'Element is not enabled!'
            Role.click()
            
            # เลือกบทบาท
            Role = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '//div[2]/div[3]/ul/li[1]')) 
            )
            assert Role.is_displayed(), 'Element is not displayed!'
            assert Role.is_enabled(), 'Element is not enabled!'
            Role.click()

            wait_element = WebDriverWait(driver, 10).until(
                 EC.visibility_of_element_located((By.XPATH, 
            '//div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]'))
            )
            print('Wait Element Show : Pass')


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


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\1.Register\\Reports'))