
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException  




def page_delete(driver):
# หน้า ข่าวสาร
        driver.get('https://msm-smarty-cms-staging.hr-impact.co/announcement')
        driver.implicitly_wait(30)

        try:

        # Detele News
            Click_delete = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[9]/button[2]'))
            )
            assert Click_delete.is_displayed(), 'Element is not displayed!'
            assert Click_delete.is_enabled(), 'Element is not enabled!'
            Click_delete.click()

            if Click_delete:
                print(f'CLick Dalete Alraedy :',(True))
            else:
                print(f'Cannot Click Dalete :',(False))

            delete = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]'))
            )
            assert delete.is_displayed(), 'Element is not displayed!'
            assert delete.is_enabled(), 'Element is not enabled!'
            delete.click()
            
            if Click_delete:
                print(f'Dalete Alraedy :',(True))
            else:
                print(f'Cannot Dalete :',(False))

            wait_element = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.ID, 'notistack-snackbar'))
            )
            print(f'Show Dalete Alraedy :',(True))


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
        
        







