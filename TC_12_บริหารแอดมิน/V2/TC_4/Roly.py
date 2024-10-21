
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from  selenium.common.exceptions import NoSuchElementException,TimeoutException



def test_page_roly(driver):
# หน้า การบริหาร - ผู้ใช้งาน
        driver.get('https://msm-smarty-cms-staging.hr-impact.co/admin')
        driver.implicitly_wait(20)

# บทบาท    
        roly = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div/div/button[2]'))
        )
        assert roly.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
        assert roly.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
        roly.click()
        time.sleep(0.1) 

# รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/button")) 
        )
# หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
        print("Element is visible. Proceeding with the next step.")
        time.sleep(0.1)


# เลือกผู้ใช้งาน

        select_user = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div/div/button[2]'))
        )
        assert select_user.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
        assert select_user.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
        select_user.click()
        time.sleep(0.5)

        select_user = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div/div/button[3]'))
        )
        assert select_user.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
        assert select_user.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
        select_user.click()
        time.sleep(0.5)

        select_user = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div/div/button[4]'))
        )
        assert select_user.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
        assert select_user.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
        select_user.click()
        time.sleep(0.5)

        select_user = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div/div/button[5]'))
        )
        assert select_user.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
        assert select_user.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
        select_user.click()
        time.sleep(0.5)

        select_user = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div/div/button[1]'))
        )
        assert select_user.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
        assert select_user.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
        select_user.click()
        time.sleep(0.5)


# จัดการเลือกโครงการ 

        # button = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[4]/div[2]/div/div/div')
        # assertTrue(button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า")
        # assertTrue(button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
        # button.click()
        # time.sleep(0.1)

        # button1 = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/ul/li[1]')
        # assertTrue(button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า")
        # assertTrue(button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
        # button1.click()
        # time.sleep(1)


# ค้นหา element ที่ต้องการให้มองเห็น
#         element_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/button")

# # ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
#         driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
#         time.sleep(1)

# Save
        # click = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr/td[1]/div/div/div/div') 
        # click.click()

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



