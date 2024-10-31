
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
from  selenium.common.exceptions import NoSuchElementException,TimeoutException
import pyautogui

def test_page_create_warning1(driver):

    try:
# หน้า การบริหาร - ผู้ใช้งาน
        driver.get('https://msm-smarty-cms-staging.hr-impact.co/warning')
        driver.implicitly_wait(10)

# สร้างใบเตือน - รายบุคคล  
        create = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div/div[1]/div[1]/div/button[1]'))
        )
        assert create.is_displayed(), 'Element is not displayed!'
        assert create.is_enabled(), 'Element is not enabled!'
        create.click()
        time.sleep(0.1) 

# สร้างใบเตือนรายบุคคล

        Click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
        )
        assert Click.is_displayed(), 'Element is not displayed!'
        assert Click.is_enabled(), 'Element is not enabled!'
        Click.click()
        time.sleep(0.1) 

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/form/div/div/div[2]/div[1]/div[1]/div/div/div/div/div[2]/div/div"))
        )
        print("รอคีย์โครงการ")
        time.sleep(0.1)

        # โครงการ

        project = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[2]/div[1]/div[1]/div/div/div/div/div[2]/div/div/input'))
        )
        assert project.is_displayed(), 'Element is not displayed!'
        assert project.is_enabled(), 'Element is not enabled!'
        project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(0.1)

        # ชั้น ห้อง

        floor_room = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[2]/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
        )
        assert floor_room.is_displayed(), 'Element is not displayed!'
        assert floor_room.is_enabled(), 'Element is not enabled!'
        floor_room.send_keys('01/03' + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(0.1)

        # วันครบกำหนดชำระ

        date_buy = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[2]/div[1]/div[2]/div/div/div'))
        )
        assert date_buy.is_displayed(), 'Element is not displayed!'
        assert date_buy.is_enabled(), 'Element is not enabled!'
        date_buy.click()
        time.sleep(0.1)


        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[3]"))  
        )
        print("เลือกวันที่ 23")
        time.sleep(0.1)

        time.sleep(0.3)
        if pyautogui:
            pyautogui.click(x=820, y=707)
            print('Click select Day 22 :',True)
        else:
            print('Cannot date',False)

        # date_buy = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[3]'))
        # )
        # assert date_buy.is_displayed(), 'Element is not displayed!'
        # assert date_buy.is_enabled(), 'Element is not enabled!'
        # date_buy.click()
        # time.sleep(0.1)

        # วันออกเอกสาร

        date_out = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[2]/div[1]/div[3]/div/div/div'))
        )
        assert date_out.is_displayed(), 'Element is not displayed!'
        assert date_out.is_enabled(), 'Element is not enabled!'
        date_out.click()
        time.sleep(0.1)

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[3]"))  
        )
        print("เลือกวันที่ 30")
        time.sleep(0.1)

        time.sleep(0.3)
        if pyautogui:
            pyautogui.click(x=820, y=707)
            print('Click select Day 22 :',True)
        else:
            print('Cannot date',False)

        # date_out = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[3]'))
        # )
        # assert date_out.is_displayed(), 'Element is not displayed!'
        # assert date_out.is_enabled(), 'Element is not enabled!'
        # date_out.click()
        # time.sleep(0.1)

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/form/div/div/div[2]/div[4]/table/tbody/tr[1]"))  
        )
        if element:
            print("ข้อมูลใบเตือนแจ้งหนี้แสดงปกติ",True)
        else:
            print('ข้อมูลใบเตือนแจ้งหนี้แสดงไม่ถูกต้อง',False)
            
        time.sleep(2)

        # ยกเลิก

        cancel = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[1]/div[2]/div/button[1]'))
        )
        assert cancel.is_displayed(), 'Element is not displayed!'
        assert cancel.is_enabled(), 'Element is not enabled!'
        cancel.click()
        time.sleep(0.1)

        # Save

        # text = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[1]/div[2]/div/button[2]'))
        # )
        # text.click()
        # time.sleep(0.5)

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



