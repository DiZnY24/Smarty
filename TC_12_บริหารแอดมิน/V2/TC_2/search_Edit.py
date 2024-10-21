
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
from  selenium.common.exceptions import NoSuchElementException,TimeoutException



def test_page_serach(driver):
            
        try:
            # หน้า จัดการลูกหนี้
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/admin')
            driver.implicitly_wait(10)

    # คีย์ โครงการ

            project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/input'))
            )
            assert project.is_displayed(), 'Element is not displayed!'
            assert project.is_enabled(), 'Element is not enabled!'
            project.send_keys('0800000000')
            time.sleep(1)


    # บทบาท

            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]"))  
                            )
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)

            wait = WebDriverWait(driver, 10)  # รอสูงสุด 10 วินาที

            Role = wait.until(
                EC.presence_of_element_located((By.XPATH, '//div/div/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div'))
                                )
            assert Role.is_displayed(), 'Element is not displayed!'
            assert Role.is_enabled(), 'Element is not enabled!'
            Role.click()
            time.sleep(0.1)


            Role = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
            )
            assert Role.is_displayed(), 'Element is not displayed!'
            assert Role.is_enabled(), 'Element is not enabled!'
            Role.click()
            time.sleep(0.1)

    # Clear Filter

            Clear = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[1]/div[2]/button')
            assert Clear.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
            assert Clear.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
            Clear.click()
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



