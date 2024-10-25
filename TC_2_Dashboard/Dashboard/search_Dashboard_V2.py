
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys 
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import pyautogui

def page_dashboard(driver):
# *** เปิดหน้า รายชื่อคนลงทะเบียน (อนุมัติ)***
        
    try:

        driver.get('https://msm-smarty-cms-staging.hr-impact.co/dashboard')
        driver.implicitly_wait(10)

        # คลิกเลือกโครงการ

        Project = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div/div/main/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div')) 
        )
        assert Project.is_displayed(), 'Element is not displayed!'
        assert Project.is_enabled(), 'Element is not enabled!'
        Project.click()

        Project = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div/div/main/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/input')) 
        )
        assert Project.is_displayed(), 'Element is not displayed!'
        assert Project.is_enabled(), 'Element is not enabled!'
        Project.send_keys('อาคาร C1' + Keys.ARROW_DOWN + Keys.ENTER + Keys.ESCAPE)

        # คลิกวันที่สร้าง 

        start_date = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div/div/main/div/div/div/div/div[1]/div/div[2]/div/div')) 
        )
        assert start_date.is_displayed(), 'Element is not displayed!'
        assert start_date.is_enabled(), 'Element is not enabled!'
        start_date.click()

        # เลือกวันที่

        time.sleep(0.5)
        pyautogui.click(x=823, y=665)
        # select_day = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, 
        # '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[1]')) 
        # )
        # assert select_day.is_displayed(), 'Element is not displayed!'
        # assert select_day.is_enabled(), 'Element is not enabled!'
        # select_day.click()

        # วันที่สินสุด

        date_end = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div[1]/div/main/div/div/div/div/div[1]/div/div[3]/div/div')) 
        )
        assert date_end.is_displayed(), 'Element is not displayed!'
        assert date_end.is_enabled(), 'Element is not enabled!'
        date_end.click()

        # เลือกวันที่

        time.sleep(0.5)
        pyautogui.click(x=820, y=699)
        # select_day = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, 
        # '//div/div[2]/div/div/div[2]/div/div[5]/button[2]')) 
        # )
        # assert select_day.is_displayed(), 'Element is not displayed!'
        # assert select_day.is_enabled(), 'Element is not enabled!'
        # select_day.click()

        # เลือกปี
        
        time.sleep(0.5)
        pyautogui.click(x=1430, y=667)
        # select_year = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, 
        # '/html/body/div/div/main/div/div/div/div/div[3]/div/div[1]/div/div[2]/div/div/div'))
        # )
        # assert select_year.is_displayed(), 'Element is not displayed!'
        # assert select_year.is_enabled(), 'Element is not enabled!'
        # select_year.click()

        # คลิก 2024
        
        select_year = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '//div[2]/div/div/div/div/div[125]/button'))
        )
        assert select_year.is_displayed(), 'Element is not displayed!'
        assert select_year.is_enabled(), 'Element is not enabled!'
        select_year.click()

        if select_year:
            print('select yaer 2024 : Pass')
        else:
            print('Not select yaer : Fail')

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
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\2.Dashboard\\Reports'))