from selenium.webdriver.common.by import By
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException


def check_delete(driver):

        try:            
            # หน้า ข่าวสาร
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/banner')
            driver.implicitly_wait(10)
            
            Delete_Banner = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[7]/button[2]'))
            )
            assert Delete_Banner.is_displayed(), 'Element is not displayed!'
            assert Delete_Banner.is_enabled(), 'Element is not enabled'
            Delete_Banner.click()


            Confirm = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]'))
            )
            assert Confirm.is_displayed(), 'Element is not displayed!'
            assert Confirm.is_enabled(), 'Element is not enabled'
            Confirm.click()

            wait_delete = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.ID, 'notistack-snackbar'))
            )
            print('Show delete already :',(True))

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





