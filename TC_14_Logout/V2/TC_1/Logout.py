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
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui



def test_page_logout(driver):

        try:    
        # หน้า การบริหาร - ผู้ใช้งาน
            # self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/warning')
            driver.implicitly_wait(20)

        # สร้างใบเตือน - รายบุคคล  

            wait = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/nav/div/div/div/div[5]/ul/li/div'))
            )
            print('พร้อมแล้ว')

            # time.sleep(2)

            # element = driver.find_element(By.XPATH, '/html/body/div/div/main/nav/div/div/div/div[5]/ul/li/div')
            # actions = ActionChains(driver)
            # actions.move_to_element(element).click().perform()

            time.sleep(2) 
            driver.refresh()

            Click_logout = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/nav/div/div/div/div[5]/ul/li/div'))
                )
            assert Click_logout.is_displayed(), 'Element is not displayed!'
            assert Click_logout.is_enabled(), 'Element is not enabled!'
            Click_logout.click() 

            time.sleep(0.1) 

            Click_logout = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]'))
                )
            assert Click_logout.is_displayed(), 'Element is not displayed!'
            assert Click_logout.is_enabled(), 'Element is not enabled!'
            Click_logout.click() 
            time.sleep(0.1) 

        except NoSuchElementException:
            driver.fail('Element not Found')
        except AssertionError as e:
            driver.fail(str(e))
        except Exception as o:
            driver.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว')


if __name__ == "__main__":
    unittest.main()




