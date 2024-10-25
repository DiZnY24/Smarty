
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pynput.keyboard import Key, Controller 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner
import unittest
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import pyautogui

def page_news(driver):

    try:    
        # หน้า ข่าวสาร
        driver.get('https://msm-smarty-cms-staging.hr-impact.co/announcement')
        driver.implicitly_wait(10)

#   เพิ่ทข่าวสาร

        Add_News = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div[1]/div[1]/div/button'))
        )
        assert Add_News.is_displayed(), 'Element is not displayed!'
        assert Add_News.is_enabled(), 'Element is not enabled!'
        Add_News.click()     

        if Add_News:
            print('Click Button เพิ่มข่าว : Pass')
        else:
            print('Not Click Button เพิ่มข่าว : Fail')               
        # กรอกข้อมูล

        # ชื่อข่าว
    
        Key_name = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/input'))
        )
        assert Key_name.is_displayed(), 'Element is not displayed!'
        assert Key_name.is_enabled(), 'Element is not enabled!'
        Key_name.send_keys('ข่าวใหม่เช้านี้')   
        
        # อัพโหลดรูปภาพ

        upload = driver.find_element(by=By.XPATH , value='/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[1]/div/div/input')
        upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')

        if upload:
            print('Upload image : Pass')
        else:
            print('Not Upload image : Fail')
        # คลิกวันที่
        
        date = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[3]/div[2]/div/div'))
        )
        assert date.is_displayed(), 'Element is not displayed!'
        assert date.is_enabled(), 'Element is not enabled!'
        date.click()

        if date:
            print('Click date : Pass')
        else:
            print('Not Click date : Fail')

        # # เลือกวันที่ ....

        time.sleep(0.5)
        if pyautogui:
            pyautogui.click(x=781, y=737)
            print('Click select date 29 :',True)
        else:
            print('Cannot date',False)
        
        # date = WebDriverWait(driver, 30).until(
        #     EC.visibility_of_element_located((By.XPATH, '//div/div[2]/div/div/div[2]/div/div[5]/button[2]'))
        # )
        # assert date.is_displayed(), 'Element is not displayed!'
        # assert date.is_enabled(), 'Element is not enabled!'
        # date.click()

        # if date:
        #     print('select date : Pass')
        # else:
        #     print('Not select date : Fail')

        # รายละเอียดข่าวสาร
        
        Key_email = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/div'))
        )
        assert Key_email.is_displayed(), 'Element is not displayed!'
        assert Key_email.is_enabled(), 'Element is not enabled!'
        Key_email.send_keys('Test1111111')  


        # ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
        driver.execute_script("window.scrollTo(0, 0);")  
        time.sleep(1)

        # Save

        Save = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//div/div/div/form/div/div[1]/div/div[1]/div/button[2]'))
        )
        assert Save.is_displayed(), 'Element is not displayed!'
        assert Save.is_enabled(), 'Element is not enabled!'
        Save.click()

        if Save:
            print('Click Button Save : Pass')
        else:
            print('Not Click Button Save : Fail')

# รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
        element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//div[2]/div[1]/div/table/tbody/tr[1]/td[1]/p"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
        )
# หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
        print("Wait show News New : Pass")

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
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\3.ข่าวสาร\\Reports'))




