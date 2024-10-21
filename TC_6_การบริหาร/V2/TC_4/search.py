
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
from selenium.common.exceptions import NoSuchElementException,TimeoutException



def test_page_search1(driver):

        try:
            # หน้า จัดการลูกหนี้
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/properties')
            driver.implicitly_wait(30)

            # คีย์ โครงการ

            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div/div/input'))
            )
            element.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
            # time.sleep(0.5)

            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)


            element = driver.find_element(By.XPATH, '//*[@title="MTTB-A1"]')
            text = 'MTTB-A1'
            check_element = element.text
            if check_element == text:
                print('ข้อความขึ้นถูกต้อง!', True)
            else:
                print('ข้อความไม่ถูกต้อง!',False) 

            time.sleep(2)

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



