
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
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def test_page_add_room(driver):
        # หน้า บริหารโครงการ
        driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/units')
        driver.implicitly_wait(30)

        try:
        # เพิ่มโครงการ

            add_project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[1]/div/button'))
            )
            assert add_project.is_displayed(), 'Element is not displayed!'
            assert add_project.is_enabled(), 'Element is not enabled!'
            add_project.click()
            time.sleep(1)
           
        # โครงการ

            project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/div/div[2]/div/div/input'))
            )
            assert project.is_displayed(), 'Element is not displayed!'
            assert project.is_enabled(), 'Element is not enabled!'
            project.send_keys('อาคาร C1' + Keys.ARROW_DOWN + Keys.ENTER)
            time.sleep(0.5)
        
        # บ้านเลขที่

            key_text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[3]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_text.is_displayed(), 'Element is not displayed!'
            assert key_text.is_enabled(), 'Element is not enabled!'
            key_text.send_keys('92/1')
            time.sleep(0.1)
        
        # ชั้น

            floor = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[3]/div[2]/div/div[2]/div/div/input'))
            )
            assert floor.is_displayed(), 'Element is not displayed!'
            assert floor.is_enabled(), 'Element is not enabled!'
            floor.send_keys('01/01')
            time.sleep(0.1)

        # เลขที่ห้อง

            key_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[3]/div[3]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys('143/01')
            time.sleep(0.1)
        
        # ประเภท

            type = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[3]/div[4]/div[2]/div/div'))
            )
            assert type.is_displayed(), 'Element is not displayed!'
            assert type.is_enabled(), 'Element is not enabled!'
            type.click()
            time.sleep(0.1)

            type = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
            )
            assert type.is_displayed(), 'Element is not displayed!'
            assert type.is_enabled(), 'Element is not enabled!'
            type.click()
            time.sleep(0.1)
        
        # ขนาดห้อง (ตร.ม.)

            key_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[4]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys('32.ม')
            time.sleep(0.1)
        
        # อัตราส่วนแห่งกรรมสิทธิ์ในทรัพย์สินส่วนกลาง

            key_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[4]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys('0.500000')
            time.sleep(0.1)
        
        # Ref1

            key_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[4]/div[3]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys('500001')
            time.sleep(0.1)
       
        # Ref2

            key_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[4]/div[4]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys('0101')
            time.sleep(0.1)
            # Cancel

            Cancel = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/button[1]').click()
# Save

        # Save = WebDriverWait(driver, 30).until(
        #         EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/button[2]'))
        # )
        # assert Save.is_displayed(), 'Element is not displayed!'
        # assert Save.is_enabled(), 'Element is not enabled!'
        # Save.click() 


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

# if __name__ == '__msain__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



