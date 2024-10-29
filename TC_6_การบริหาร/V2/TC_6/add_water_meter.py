
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

    
def test_page_add_water_meter(driver):

        try:
            # หน้า บริหารโครงการ
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/water-meter')
            driver.implicitly_wait(20)

        # เพิ่มมิเตอร์น้ำ

            water_meter = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[1]/div[1]/div/button'))
            )
            assert water_meter.is_displayed(), 'Element is not displayed!'
            assert water_meter.is_enabled(), 'Element is not enabled!'
            water_meter.click()
            time.sleep(0.5)   

        # โครงการ

            Project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
            )
            assert Project.is_displayed(), 'Element is not displayed!'
            assert Project.is_enabled(), 'Element is not enabled!'
            Project.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Project.send_keys('อาคาร C8' + Keys.ARROW_DOWN + Keys.ENTER)
            time.sleep(0.1) 

        # ชั้น / ห้อง

            floor = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/input'))
            )
            assert floor.is_displayed(), 'Element is not displayed!'
            assert floor.is_enabled(), 'Element is not enabled!'
            floor.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)
            time.sleep(0.1) 

        # หมายเลขมิเตอร์น้ำ 

            number_water_meter = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[3]/div[1]/div/div[2]/div/div/input'))
            )
            assert number_water_meter.is_displayed(), 'Element is not displayed!'
            assert number_water_meter.is_enabled(), 'Element is not enabled!'
            number_water_meter.send_keys('950')
            time.sleep(0.1) 

        # ค่ามาตรวัดเริ่มต้น

            number_water_meter = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[3]/div[2]/div/div[2]/div/div/input'))
            )
            assert number_water_meter.is_displayed(), 'Element is not displayed!'
            assert number_water_meter.is_enabled(), 'Element is not enabled!'
            number_water_meter.send_keys('150')       
            time.sleep(0.1) 
        # ขนาดมาตรน้ำ

            size_water_meter = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[3]/div[3]/div/div[2]/div/div/input'))
            )
            assert size_water_meter.is_displayed(), 'Element is not displayed!'
            assert size_water_meter.is_enabled(), 'Element is not enabled!'
            size_water_meter.send_keys('32')       
            time.sleep(0.1) 

        # สถานะมิเตอร์

            status_water_meter = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[3]/div[4]/div[2]/div/div/div'))
            )
            assert status_water_meter.is_displayed(), 'Element is not displayed!'
            assert status_water_meter.is_enabled(), 'Element is not enabled!'
            status_water_meter.click()       
            time.sleep(0.1) 

            status_water_meter = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]'))
            )
            assert status_water_meter.is_displayed(), 'Element is not displayed!'
            assert status_water_meter.is_enabled(), 'Element is not enabled!'
            status_water_meter.click()       
            time.sleep(0.1) 

        # วันที่ลงทะเบียน

            Registration = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[4]/div/div/div'))
            )
            assert Registration.is_displayed(), 'Element is not displayed!'
            assert Registration.is_enabled(), 'Element is not enabled!'
            Registration.click()       
            time.sleep(0.1) 

            time.sleep(0.5)
            if pyautogui:
                pyautogui.click(x=780, y=741)
                print('Click select date 29 :',True)
            else:
                print('Cannot date',False)

            # Registration = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, '//div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[2]'))
            # )
            # assert Registration.is_displayed(), 'Element is not displayed!'
            # assert Registration.is_enabled(), 'Element is not enabled!'
            # Registration.click()       
            # time.sleep(0.1) 

    # บันทึก

            # Save = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[1]/div[2]/div/button[2]'))
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click()       
            # time.sleep(0.1) 
            

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
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



