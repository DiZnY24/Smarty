
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
import pyautogui


def test_page_search_edit(driver):
        
        try:
            # หน้า จัดการลูกหนี้
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/invoice')
            driver.implicitly_wait(10)

            # คีย์ โครงการ

            project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div[2]/div/div/input'))
            )
            assert project.is_displayed(), 'Element is not displayed!'
            assert project.is_enabled(), 'Element is not enabled!'
            project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)

            # คีย์ ชั้น / ห้อง

            floor_room = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div/input'))
            )
            assert floor_room.is_displayed(), 'Element is not displayed!'
            assert floor_room.is_enabled(), 'Element is not enabled!'
            floor_room.send_keys('01/04' + Keys.ARROW_DOWN + Keys.ENTER)
            time.sleep(0.1)

    # คีย์ ค้นหารายชื่อ
            search_name = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div/div/div/div'))
            )
            assert search_name.is_displayed(), 'Element is not displayed!'
            assert search_name.is_enabled(), 'Element is not enabled!'
            search_name.click()
            time.sleep(0.5)

            click = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[4]/button[1]').click()

            key_name = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/input'))
            )
            assert key_name.is_displayed(), 'Element is not displayed!'
            assert key_name.is_enabled(), 'Element is not enabled!'
            key_name.send_keys('รายการใหม่' + Keys.ARROW_DOWN + Keys.ENTER)

            time.sleep(1)

    # วันที่ วันที่ออกเอกสาร

            Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div/div/div'))
            )
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            time.sleep(0.5)
            if pyautogui:
                pyautogui.click(x=743 ,y=737)
                print('Click select Day 28 :',True)
            else:
                print('Cannot date',False)
                time.sleep(0.1)

        #     Date = WebDriverWait(driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[3]'))
        #     )
        #     assert Date.is_displayed(), 'Element is not displayed!'
        #     assert Date.is_enabled(), 'Element is not enabled!'
        #     Date.click()
        #     time.sleep(0.1)

    # วันที่ วันที่ครบกำหนดชำระ (เริ่มต้น)

            Date = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div')
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()

            time.sleep(0.5)
            if pyautogui:
                pyautogui.click(x=743 ,y=737)
                print('Click select Day 28 :',True)
            else:
                print('Cannot date',False)
                time.sleep(0.1)

        #     Date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/button[3]')
        #     assert Date.is_displayed(), 'Element is not displayed!'
        #     assert Date.is_enabled(), 'Element is not enabled!'
        #     Date.click()
        #     time.sleep(0.1)

    # วันที่ วันที่ครบกำหนดชำระ (สิ้นสุด)

            Date = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div/div')
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            time.sleep(0.5)
            if pyautogui:
                pyautogui.click(x=743 ,y=737)
                print('Click select Day 28 :',True)
            else:
                print('Cannot date',False)
                time.sleep(0.1)

        #     Date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/button[7]')
        #     assert Date.is_displayed(), 'Element is not displayed!'
        #     assert Date.is_enabled(), 'Element is not enabled!'
        #     Date.click()
        #     time.sleep(0.1)

    # วันที่สร้างเอกสาร (เริ่มต้น)

            Date = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[4]/div/div/div')
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            time.sleep(0.5)
            if pyautogui:
                pyautogui.click(x=743 ,y=737)
                print('Click select Day 28 :',True)
            else:
                print('Cannot date',False)
                time.sleep(0.1)

        #     Date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[1]')
        #     assert Date.is_displayed(), 'Element is not displayed!'
        #     assert Date.is_enabled(), 'Element is not enabled!'
        #     Date.click()
        #     time.sleep(0.1)

    # วันที่สร้างเอกสาร (สิ้นสุด)

            Date = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[5]/div/div/div')
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            time.sleep(0.5)
            if pyautogui:
                pyautogui.click(x=821 ,y=737)
                print('Click select Day 30 :',True)
            else:
                print('Cannot date',False)
                time.sleep(0.1)

        #     Date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[2]')
        #     assert Date.is_displayed(), 'Element is not displayed!'
        #     assert Date.is_enabled(), 'Element is not enabled!'
        #     Date.click()
        #     time.sleep(0.1)

    # วันประกาศใบแจ้งหนี้

            Date = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[6]/div/div/div')
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            time.sleep(0.5)  
            if pyautogui:
                pyautogui.click(x=743 ,y=737)
                print('Click select Day 28 :',True)
            else:
                print('Cannot date',False)
                time.sleep(0.1)

        #     Date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[3]')
        #     assert Date.is_displayed(), 'Element is not displayed!'
        #     assert Date.is_enabled(), 'Element is not enabled!'
        #     Date.click()
        #     time.sleep(0.1)

    # ที่อยู่จัดส่งเอกสาร

            Date = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[7]/div[2]/div/div/div')
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

            Date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.click()
            time.sleep(0.1)

    # ค้นหา เลขที่เอกสาร

        #     Date = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[1]/div/div[2]/div/div/input')
        #     Date.send_keys('IW2024092200001')
        #     time.sleep(0.1)

    # ค้นหา ชื่อ

            Date = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[2]/div/div[2]/div/div/input')
            assert Date.is_displayed(), 'Element is not displayed!'
            assert Date.is_enabled(), 'Element is not enabled!'
            Date.send_keys('นายพรสวรรค์ วรรณพานิช')
            time.sleep(0.1)

    # Refresh

            Refresh = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/button')
            assert Refresh.is_displayed(), 'Element is not displayed!'
            assert Refresh.is_enabled(), 'Element is not enabled!'
            Refresh.click()
            time.sleep(0.1)

            
    # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]")) 
            )
    # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
            print("Element is visible. Proceeding with the next step.")
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



