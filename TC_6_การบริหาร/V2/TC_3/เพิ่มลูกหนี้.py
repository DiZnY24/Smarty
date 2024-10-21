
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


def test_page_add_debtor(driver):
            
        try: 
    # หน้า การบริหาร - ผู้ใช้งาน
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/debtors')
            driver.implicitly_wait(30)

    # เพิ่มลูกหนี้

            Add = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[1]/button'))
            )
            assert Add.is_displayed(), 'Element is not displayed!'
            assert Add.is_enabled(), 'Element is not enabled!'
            Add.click() 
            time.sleep(0.1) 

    # คีย์ โครงการ

            key_projet = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[1]/div/div/div/div[2]/div/div/input'))
            )
            assert key_projet.is_displayed(), 'Element is not displayed!'
            assert key_projet.is_enabled(), 'Element is not enabled!'
            key_projet.click() 
            time.sleep(0.1) 

            key_projet = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[1]/div/div/div/div[2]/div/div/input'))
            )
            assert key_projet.is_displayed(), 'Element is not displayed!'
            assert key_projet.is_enabled(), 'Element is not enabled!'
            key_projet.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
            time.sleep(0.1)

            # ชั้น / ห้อง

    # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
            floor = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[2]/div/div/div/div[2]/div/div"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
    # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)

            click_floor = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[2]/div/div/div/div[2]/div/div'))
            )
            assert click_floor.is_displayed(), 'Element is not displayed!'
            assert click_floor.is_enabled(), 'Element is not enabled!'
            click_floor.click() 
            time.sleep(0.1)

            key_floor = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[2]/div/div/div/div[2]/div/div/input'))
            )
            assert key_floor.is_displayed(), 'Element is not displayed!'
            assert key_floor.is_enabled(), 'Element is not enabled!'
            key_floor.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)

    # # สถานะ

            status = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[2]/div[2]/div/div/div"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.5)

            # element = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[2]/div[2]/div/div'))
            # )
            # assertTrue(element.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
            # assertTrue(element.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
            # element.click()

            click_status = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[2]/div[2]/div/div')
            click_status.click()

            time.sleep(1)

            click_status = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[1]'))
            )
            assert click_status.is_displayed(), 'Element is not displayed!'
            assert click_status.is_enabled(), 'Element is not enabled!'
            click_status.click() 

            time.sleep(1)

            element_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/button")
            driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
            time.sleep(1)

    # Detele

            # delete = WebDriverWait(driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[6]/table/tbody/tr[1]/td[3]/button'))
            # )
            # assert delete.is_displayed(), 'Element is not displayed!'
            # assert delete.is_enabled(), 'Element is not enabled!'
            # delete.click() 
    # Save  

            # Save = WebDriverWait(driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/button'))
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click() 
            # time.sleep(1)
            # search_box = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/button')
            
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



