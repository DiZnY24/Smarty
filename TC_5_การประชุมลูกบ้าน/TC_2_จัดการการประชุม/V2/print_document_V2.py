
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException,TimeoutException


def page_print(driver):

        try:
            # เปิดหน้า จัดการประชุม
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/agm/meetings')
            driver.implicitly_wait(30)

            # รอหน้าเว็ปเสร็จที่จะเริ่มคลิก พิมพ์เออกสาร
            print_1 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[8]/div/div/button'))
            )
            assert print_1.is_displayed(),'Element is not displayed!'
            assert print_1.is_enabled(), 'Element is not enabled!'

            if print_1:
                print_1.click()
                print('Click print Already :', True)
            else:
                print('Cannot Click print :',False)

            time.sleep(3)

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
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\5.การประชุมลูกบ้าน\\Reports'))