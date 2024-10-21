
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



def test_page_add_receipt(driver):

        try:
                driver.get('https://msm-smarty-cms-staging.hr-impact.co/receipt')
                driver.implicitly_wait(30)

        # สร้างใบแจ้งหนี้ - สร้างใบแจ้งหนี้ รายบุคคล    
                create = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[1]/div/button[1]'))
                )
                assert create.is_displayed(), 'Element is not displayed!'
                assert create.is_enabled(), 'Element is not enabled!'
                create.click()
                time.sleep(0.1) 

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/form/div/div/div[2]/div[1]/div[1]/div/div/div/div/div[2]/div/div"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

        # โครงการ
                project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[2]/div[1]/div[1]/div/div/div/div/div[2]/div/div/input'))
                )
                assert project.is_displayed(), 'Element is not displayed!'
                assert project.is_enabled(), 'Element is not enabled!'
                project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.1)

        # วันชำระ

                date_buy = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[2]/div[1]/div[2]/div/div/div'))
                )
                assert date_buy.is_displayed(), 'Element is not displayed!'
                assert date_buy.is_enabled(), 'Element is not enabled!'
                date_buy.click()
                time.sleep(0.1)

                date_buy = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/button[3]'))
                )
                assert date_buy.is_displayed(), 'Element is not displayed!'
                assert date_buy.is_enabled(), 'Element is not enabled!'
                date_buy.click()
                time.sleep(1)

        # ชั้น ห้อง
                floor_room = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[2]/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
                )
                assert floor_room.is_displayed(), 'Element is not displayed!'
                assert floor_room.is_enabled(), 'Element is not enabled!'
                floor_room.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(1)

        # รหัส

                password = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr/td[1]/div/div/div/div'))
                )
                assert password.is_displayed(), 'Element is not displayed!'
                assert password.is_enabled(), 'Element is not enabled!'
                password.click()
                time.sleep(0.5)

                key_text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr/td[1]/div/div/div/div/input'))
                )
                assert key_text.is_displayed(), 'Element is not displayed!'
                assert key_text.is_enabled(), 'Element is not enabled!'
                key_text.send_keys('001' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.1)

        # เพิ่มรายการ 2 

                Add = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[4]/div[1]/button'))
                )
                assert Add.is_displayed(), 'Element is not displayed!'
                assert Add.is_enabled(), 'Element is not enabled!'
                Add.click()
                time.sleep(0.5)

                # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr[2]/td[1]/div/div/div/div/input"))  
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

        # รหัส

                key_text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr[2]/td[1]/div/div/div/div/input'))
                )
                assert key_text.is_displayed(), 'Element is not displayed!'
                assert key_text.is_enabled(), 'Element is not enabled!'
                key_text.send_keys('002' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.1)

        # เพิ่มรายการ 3 

                Add = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[4]/div[1]/button'))
                )
                assert Add.is_displayed(), 'Element is not displayed!'
                assert Add.is_enabled(), 'Element is not enabled!'
                Add.click()
                time.sleep(0.1)

                # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr[3]/td[1]/div/div/div/div/input"))  
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

        # รหัส

                key_text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr[3]/td[1]/div/div/div/div/input'))
                )
                assert key_text.is_displayed(), 'Element is not displayed!'
                assert key_text.is_enabled(), 'Element is not enabled!'
                key_text.send_keys('003' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.1)

        # กดลบ Delete

                # Delete = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr[2]/td[8]/button')  # ลบ 2
                # Delete.click()
                # time.sleep(0.1)

                # Delete = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[3]/table/tbody/tr[1]/td[8]/button')  # ลบ 1
                # Delete.click()
                # time.sleep(0.1)

        # รูปแบบการชำระเงิน

                type_buy = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[5]/div[1]/div[1]/div[2]/div/label[2]/span[1]'))
                )
                assert type_buy.is_displayed(), 'Element is not displayed!'
                assert type_buy.is_enabled(), 'Element is not enabled!'
                type_buy.click()
                time.sleep(0.1)

        # หมายเหตุ

                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)

                key_text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[5]/div[1]/div[2]/div/div/div/div/div/input'))
                )
                assert key_text.is_displayed(), 'Element is not displayed!'
                assert key_text.is_enabled(), 'Element is not enabled!'
                key_text.send_keys('Test')
                time.sleep(0.1)

                driver.execute_script("window.scrollTo(0, 0);")    
                time.sleep(1)

        # ยกเลิก

                cancel = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[1]/div[2]/div/button[1]'))
                )
                assert cancel.is_displayed(), 'Element is not displayed!'
                assert cancel.is_enabled(), 'Element is not enabled!'
                cancel.click()
                time.sleep(0.1)

        # บันทึก

                # button1 = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div/div[1]/div[2]/div/button[2]')
                # assertTrue(button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า")
                # assertTrue(button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
                # button1.click()
                # time.sleep(0.1) 

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



