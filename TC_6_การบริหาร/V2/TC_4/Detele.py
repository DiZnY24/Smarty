
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



def test_page_delete(driver):
        
        try:
            # หน้า การบริหาร - ผู้ใช้งาน
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/properties')
            time.sleep(1)

            # Detele
            delete = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[6]/div/button'))
            )
            assert delete.is_displayed(), 'Element is not displayed!'
            assert delete.is_enabled(), 'Element is not enabled!'
            delete.click()
            time.sleep(0.5)

            # ยกเลิก 

            cancel = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[1]'))
            )
            assert cancel.is_displayed(), 'Element is not displayed!'
            assert cancel.is_enabled(), 'Element is not enabled!'
            cancel.click()
            time.sleep(0.5)

             # ยืนยัน

            # comfirm = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]'))
            # )
            # assert comfirm.is_displayed(), 'Element is not displayed!'
            # assert comfirm.is_enabled(), 'Element is not enabled!'
            # comfirm.click()
            # time.sleep(0.5)

        except NoSuchElementException:
            driver.fail('Element not Found')
        except AssertionError as e:
            driver.fail(str(e))
        except Exception as o:
            driver.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            driver.fail('การรอองค์ประกอบล้มเหลว')



if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



