
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException

 
def page_dalete(driver):
            
            # หน้า ข่าวสาร
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/parcels/express')
            driver.implicitly_wait(30)

            # search Home Page

            delete = WebDriverWait(driver, 30).until(
                 EC.element_to_be_clickable((By.XPATH, '//div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/button'))
            )
            assert delete.is_displayed(), 'Element is not displayed!'
            assert delete.is_enabled(), 'Element is not enabled!'
            delete.click() 

            if delete:
                print('Click Delete Already :',True)
            else:
                print('Cannot Click Delete :s',False)


            confirm = WebDriverWait(driver, 30).until(
                 EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]'))
            )
            # time.sleep(0.5)
            assert confirm.is_displayed(), 'Element is not displayed!'
            assert confirm.is_enabled(), 'Element is not enabled!'
            confirm.click() 

            if confirm:
                print('Click Confirm Already :',True)
            else:
                print('Cannot Click Confirm :s',False)

            time.sleep(2)

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\4.พัสดุ\\Reports'))





