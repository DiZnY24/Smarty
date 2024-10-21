
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


def page_search(driver):

        try:

            driver.get('https://msm-smarty-cms-staging.hr-impact.co/parcels')
            driver.implicitly_wait(30)

            # search Home Page

            Click_search = WebDriverWait(driver, 30).until(
                 EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div/div/input'))
            )
            assert Click_search.is_displayed(), 'Element is not displayed!'
            assert Click_search.is_enabled(), 'Element is not enabeld!'
            Click_search.send_keys('อาคาร A3'+ Keys.ARROW_DOWN + Keys.ENTER + Keys.ESCAPE) 

            # คลิกโครงการ

            # Click_search = WebDriverWait(driver, 30).until(
            #      EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div/div/input'))
            # )
            # assert Click_search.is_displayed(), 'Element is not displayed!'
            # assert Click_search.is_enabled(), 'Element is not enabeld!'
            # Click_search.send_keys('อาคาร A3'+ Keys.ARROW_DOWN + Keys.ENTER + Keys.ESCAPE) 

            # Add_project = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div[4]/div[1]/div/div/div/div/div[2]/div/div/input')
            # Add_project.send_keys('อาคาร C1' + Keys.ARROW_DOWN + Keys.ENTER)     


            # คลิกชั้น/ห้อง

            Click_room = WebDriverWait(driver, 30).until(
                 EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div/div[3]/div[1]/div/div/div/div[2]/div/div'))
            )
            assert Click_room.is_displayed(), 'Element is not displayed!'
            assert Click_room.is_enabled(), 'Element is not enabeld!'
            Click_room.click()
            
            Key_room = WebDriverWait(driver, 30).until(
                 EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div/div[3]/div[1]/div/div/div/div[2]/div/div/input'))
            )
            assert Key_room.is_displayed(), 'Element is not displayed!'
            assert Key_room.is_enabled(), 'Element is not enabeld!'
            Key_room.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)

            # เลือก_ชื่อลูกบ้านที่ต้องการแจ้งเตือน

            # สถานะ

            status = WebDriverWait(driver, 30).until(
                 EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div/div'))
            )
            assert status.is_displayed(), 'Element is not displayed!'
            assert status.is_enabled(), 'Element is not enabeld!'
            status.click()

            status = WebDriverWait(driver, 30).until(
                 EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[3]'))
            )
            assert status.is_displayed(), 'Element is not displayed!'
            assert status.is_enabled(), 'Element is not enabeld!'
            status.click()

            # Key หมายเลขพัสดุ

            Key_number = WebDriverWait(driver, 30).until(
                 EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div/div[3]/div[3]/div/div[2]/div/div/input'))
            )
            assert Key_number.is_displayed(), 'Element is not displayed!'
            assert Key_number.is_enabled(), 'Element is not enabeld!'
            Key_number.send_keys('1121212')   


            Check_Element = WebDriverWait(driver, 30).until(
                 EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]'))
            )
            print('Show Element :', True)
            time.sleep(2)

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





