
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



def test_page_edit(driver):
            
        try:
            # หน้า การบริหาร - ผู้ใช้งาน
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/admin')
            driver.implicitly_wait(10)

            # Edit 
            edit = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[6]/div/button'))
            )
            assert edit.is_displayed(), 'Element is not displayed!'
            assert edit.is_enabled(), 'Element is not enabled!'
            edit.click()
        
            time.sleep(0.1)

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[2]/div/div/div"))  
                            )
    # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)
            
            input("รอจนกว่ารายชื่อปรากฏขึ้น ENTER")

            # บทบาท

            Role = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[2]/div/div/div'))
            )
            assert Role.is_displayed(), 'Element is not displayed!'
            assert Role.is_enabled(), 'Element is not enabled!'
            Role.click()
            time.sleep(0.1)

            # เบือก บทบาท      

            select = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[1]'))
            )
            assert select.is_displayed(), 'Element is not displayed!'
            assert select.is_enabled(), 'Element is not enabled!'
            select.click()
            time.sleep(0.1)

            # จัดการเลือกโครงการ

            select_project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[4]/div[2]/div/div/div'))
            )
            assert select_project.is_displayed(), 'Element is not displayed!'
            assert select_project.is_enabled(), 'Element is not enabled!'
            select_project.click()
            time.sleep(0.1)

            # ทั้งหมด

            All = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[1]'))
            )
            assert All.is_displayed(), 'Element is not displayed!'
            assert All.is_enabled(), 'Element is not enabled!'
            All.click()
            time.sleep(0.1)

            # บันทึก
            # Save = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/button').click()

    # ค้นหา element ที่ต้องการให้มองเห็น
            element_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/button")

    # ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
            driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
            time.sleep(1)


    # กดออก ยกเลิก 

            Click = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/h2/div/button').click()
            time.sleep(0.5)


    # Delete 

            click_delete = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[7]/div/button').click()
            time.sleep(1)

            cancel = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[1]').click()
            time.sleep(1)
            # delete = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]').click()

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



