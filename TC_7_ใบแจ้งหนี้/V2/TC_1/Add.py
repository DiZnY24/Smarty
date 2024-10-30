
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
import pyautogui

def test_page_add_invoice(driver):
                
        try:
        # หน้า การบริหาร - ผู้ใช้งาน
                driver.get('https://msm-smarty-cms-staging.hr-impact.co/invoice')
                driver.implicitly_wait(30)

        # สร้างใบแจ้งหนี้ - สร้างใบแจ้งหนี้ รายบุคคล    
                Create_an_invoice = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[1]/div/button[1]'))
                )
                assert Create_an_invoice.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert Create_an_invoice.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                Create_an_invoice.click()
                time.sleep(0.1) 

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/ul/li[1]"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)
                
                Click = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]')
                Click.click()
                time.sleep(0.1)

        # โครงการ
                project = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
                )
                assert project.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert project.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.1)

        # ชั้น ห้อง
                floor = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/input'))
                )
                assert floor.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert floor.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                floor.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(3)

        # วันที่ออกเอกสาร

                date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[3]/div[1]/div/div/div'))
                )
                assert date.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                assert date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                date.click()
                time.sleep(0.1)

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[3]"))  
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1) 

                time.sleep(0.5)
                if pyautogui:
                   pyautogui.click(x=780, y=737)
                   print('Click select Day 29 :',True)
                else:
                   print('Cannot date',False)                
                time.sleep(1)
                # select_date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[3]')
                # assert select_date.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                # assert select_date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                # select_date.click()
                # time.sleep(1)

        # วันที่ครบกำหนดชำระ

                date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[3]/div[2]/div/div/div'))
                )
                assert date.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                assert date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                date.click()
                time.sleep(0.1)

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[3]"))  
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

                time.sleep(0.5)
                if pyautogui:
                   pyautogui.click(x=780, y=737)
                   print('Click select Day 29 :',True)
                else:
                   print('Cannot date',False)                
                time.sleep(0.5)
                # select = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[3]')
                # assert select.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                # assert select.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                # select.click()
                # time.sleep(0.1)

        # วันประกาศใบแจ้งหนี้

                date_start = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[3]/div[3]/div/div/div')
                assert date_start.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                assert date_start.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                date_start.click()
                time.sleep(0.1)

                time.sleep(0.5)
                if pyautogui:
                   pyautogui.click(x=780, y=737)
                   print('Click select Day 29 :',True)
                else:
                   print('Cannot date',False)                

                # time.sleep(0.5)
                # if pyautogui:
                #    pyautogui.click(x=821, y=738)
                #    print('Click select Day 30 :',True)
                # else:
                #    print('Cannot date',False)                
                # time.sleep(1)

                # select_date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[7]')
                # assert select_date.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                # assert select_date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้" 
                # select_date.click()
                # time.sleep(0.1)

        # ยกเลิก
                cancel = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[1]/div[2]/div/button[1]'))
                )
                assert cancel.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                assert cancel.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                cancel.click()
                time.sleep(0.5)

        # Save
                # Save = WebDriverWait(driver, 10).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[1]/div[2]/div/button[2]'))
                # )
                # assert Save.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                # assert Save.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                # Save.click()
                # time.sleep(0.5)

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



