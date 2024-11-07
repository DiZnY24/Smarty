
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
        
    try:

        driver.get('https://msm-smarty-cms-staging.hr-impact.co/dashboard')
        driver.implicitly_wait(10)

        # คลิกเลือกโครงการ

        Project = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, 
        '//*[@class="MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-adornedEnd MuiAutocomplete-inputRoot mui-style-s2ujxz"]')) 
        )
        assert Project.is_displayed(), 'Element is not displayed!'
        assert Project.is_enabled(), 'Element is not enabled!'
        Project.click()

        time.sleep(0.5)

        Project = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div/div/main/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/input')) 
        )
        assert Project.is_displayed(), 'Element is not displayed!'
        assert Project.is_enabled(), 'Element is not enabled!'
        Project.send_keys('อาคาร C1' + Keys.ARROW_DOWN + Keys.ENTER + Keys.ESCAPE)

        # คลิกเดือนล่าสุด 

        click_month = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div/div/main/div/div/div/div/div[1]/div/div[2]/div[2]/div/div')) 
        )
        assert click_month.is_displayed(), 'Element is not displayed!'
        assert click_month.is_enabled(), 'Element is not enabled!'
        click_month.click()

        # เลือกเลือกเดือน

        # time.sleep(0.5)
        # pyautogui.click(x=823, y=665)

        select_month = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div[2]/div[3]/ul/li[2]')) 
        )
        assert select_month.is_displayed(), 'Element is not displayed!'
        assert select_month.is_enabled(), 'Element is not enabled!'
        select_month.click()

        # เลือกปี

        select_year = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '//*/div[3]/div[2]/div/div/div')) 
        )
        assert select_year.is_displayed(), 'Element is not displayed!'
        assert select_year.is_enabled(), 'Element is not enabled!'
        select_year.click()

        # เลือกวันที่

        # time.sleep(0.5)
        # pyautogui.click(x=820, y=699)
        
        select_day = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '//*[@class="MuiList-root MuiList-padding MuiMenu-list mui-style-r8u8y9"]//li[4]')) 
        )
        assert select_day.is_displayed(), 'Element is not displayed!'
        assert select_day.is_enabled(), 'Element is not enabled!'
        select_day.click()

        # check_element = WebDriverWait(driver, 30).until(
        #     EC.visibility_of_element_located((By.XPATH, '//*[@class="MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiCard-root mui-style-kkge07"]'))
        # )
        # if check_element:
        #     print('Element Show Already',True)
        # else:
        #     print('Element not Found',False)

        while True:
            try:
                # ตรวจสอบว่า element ที่เราต้องการมีการแสดงผลหรือไม่
                check_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@class="MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiCard-root mui-style-kkge07"]')))
                print("Element found! :",True)
                break  # ออกจาก while loop เมื่อพบ element
            except:
                print("Element not found, retrying...")
                time.sleep(1)  # รอ 1 วินาทีแล้วลองใหม่


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