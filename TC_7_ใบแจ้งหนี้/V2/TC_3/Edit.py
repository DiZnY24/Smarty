
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from pynput.keyboard import Key, Controller 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import pyautogui


def test_page_staus_edit(driver):

        try:     
                # หน้า จัดการลูกหนี้
                driver.get('https://msm-smarty-cms-staging.hr-impact.co/invoice')
                driver.implicitly_wait(10)
                time.sleep(1)

        # คีย์ รายการใหม่

                new_items = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[10]/div/div/button")) 
                )
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

                new_items = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[10]/div/div/button'))
                )
                assert new_items.is_displayed(), 'Element is not displayed!'
                assert new_items.is_enabled(), 'Element is not enabled!'
                new_items.click()

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/ul/li[1]")) 
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

        # แจ้งชำระ

                Buy = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
                )
                assert Buy.is_displayed(), 'Element is not displayed!'
                assert Buy.is_enabled(), 'Element is not enabled!'
                Buy.click()

        # วันชำระ

                # Date = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div/div[2]/div[1]/div[2]/div/div/div')
                # assertTrue(Date.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
                # assertTrue(Date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
                # Date.click()
                # time.sleep(0.1)

                # Date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/button[7]')
                # assertTrue(Date.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
                # assertTrue(Date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
                # Date.click()
                # time.sleep(0.1)

        # คีย์ ที่อยู่

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div/form/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/input")) 
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)


                key_text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/input'))
                )
                assert key_text.is_displayed(), 'Element is not displayed!'
                assert key_text.is_enabled(), 'Element is not enabled!'
                key_text.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
                key_text.send_keys('162/0001 โครงการเมืองทองบางนา A3 หมู่ 7 อาคาร 1 ถนน 1 ซอย 1 ตำบล/แขวง คลองท่อมเหนือ ')
                time.sleep(0.1)

        # คีย์ ชื่อ

                key_name = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div/div[2]/div[3]/div[1]/div/div[2]/div/div/input'))
                )
                assert key_name.is_displayed(), 'Element is not displayed!'
                assert key_name.is_enabled(), 'Element is not enabled!'
                key_name.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
                key_name.send_keys('คุณอมรกิจ')
                time.sleep(0.1)

        # เบอร์โทรศัพท์

                phone_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div/div[2]/div[3]/div[2]/div/div[2]/div/div/input'))
                )
                assert phone_number.is_displayed(), 'Element is not displayed!'
                assert phone_number.is_enabled(), 'Element is not enabled!'
                phone_number.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
                phone_number.send_keys('0000000000')
                time.sleep(1)


        # ค้นหา element ที่ต้องการให้มองเห็น
                element_2 = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div/form/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/label[1]/span[1]")

        # ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
                driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
                time.sleep(1)

        # รูปแบบการชำระเงิน

                Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/label[1]/span[1]'))
                )
                assert Date.is_displayed(), 'Element is not displayed!'
                assert Date.is_enabled(), 'Element is not enabled!'
                Date.click()
                time.sleep(0.1)

        # หมายเหตุ

                note = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div/div[3]/div[2]/div[1]/div[2]/div/div/div/div/div/input'))
                )
                assert note.is_displayed(), 'Element is not displayed!'
                assert note.is_enabled(), 'Element is not enabled!'
                # element.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
                note.send_keys('Test')
                time.sleep(0.1)

        # รับเงินทั้งหมด

                money = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div/div[3]/div[2]/div[2]/div/div[7]/div/div/div/div/div/input'))
                )
                assert money.is_displayed(), 'Element is not displayed!'
                assert money.is_enabled(), 'Element is not enabled!'
                money.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
                money.send_keys('100')
                time.sleep(1.5)


        # เลื่อนจอขึ้นสุด
                driver.execute_script("window.scrollTo(0, 0);")         
                time.sleep(0.5)

        # # ยกเลิก 

                cancel = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div/div[1]/div[2]/div/button[1]'))
                )
                assert cancel.is_displayed(), 'Element is not displayed!'
                assert cancel.is_enabled(), 'Element is not enabled!'
                cancel.click()
                time.sleep(0.1)

        # # บันทึก

        #         S = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div/div[1]/div[2]/div/button[2]')
        #         assertTrue(S.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
        #         assertTrue(S.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
        #         S.click()
        #         time.sleep(0.1)


        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # คีย์ รายการใหม่ - สร้างใบลดหนี้

                element = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[10]/div/div/button")) 
                )
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

                new_items = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[10]/div/div/button'))
                )
                assert new_items.is_displayed(), 'Element is not displayed!'
                assert new_items.is_enabled(), 'Element is not enabled!'
                new_items.click()

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/ul/li[2]")) 
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

        # สร้างใบลดหนี้

                create = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]'))
                )
                assert create.is_displayed(), 'Element is not displayed!'
                assert create.is_enabled(), 'Element is not enabled!'
                create.click()
                time.sleep(0.1)


        # # ยกเลิก 

                # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/form/div/div/div[1]/div[2]/div/button[1]")) 
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

                cancel = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div/div[1]/div[2]/div/button[1]'))
                )
                assert cancel.is_displayed(), 'Element is not displayed!'
                assert cancel.is_enabled(), 'Element is not enabled!'
                cancel.click()
                time.sleep(0.1)

        # # บันทึก

        #         S = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div/div[1]/div[2]/div/button[2]')
        #         assertTrue(S.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
        #         assertTrue(S.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
        #         S.click()
        #         time.sleep(0.1)


        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # คีย์ รายการใหม่ - เปลี่ยนวันประกาศใบแจ้งหนี้

                element = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[10]/div/div/button")) 
                )
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

                new = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[10]/div/div/button'))
                )
                assert new.is_displayed(), 'Element is not displayed!'
                assert new.is_enabled(), 'Element is not enabled!'
                new.click()

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/ul/li[3]")) 
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

        # เปลี่ยนวันประกาศใบแจ้งหนี้

                new = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[3]'))
                )
                assert new.is_displayed(), 'Element is not displayed!'
                assert new.is_enabled(), 'Element is not enabled!'
                new.click()
                time.sleep(0.1)


        # เปลี่ยนวันประกาศใบแจ้งหนี้

                Date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div')
                assert Date.is_displayed(), 'Element is not displayed!'
                assert Date.is_enabled(), 'Element is not enabled!'
                Date.click()
                time.sleep(0.1)

                # time.sleep(0.5)
                # if pyautogui:
                #    pyautogui.click(x=782, y=738)
                #    print('Click select day 29 :',True)
                # else:
                #    print('Cannot date',False)

                time.sleep(0.5)
                if pyautogui:
                   pyautogui.click(x=823, y=737)
                   print('Click select day 29 :',True)
                else:
                   print('Cannot date',False)

                # Date = driver.find_element(By.XPATH, '//div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[3]')
                # Date.click()
                # time.sleep(0.1)

        # บันทึก

        #         S = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/button')
        #         assertTrue(S.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
        #         assertTrue(S.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
        #         S.click()
        #         time.sleep(0.1)
        
        # ยกเยิก

                cancel = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/h2/div/button')
                assert cancel.is_displayed(), 'Element is not displayed!'
                assert cancel.is_enabled(), 'Element is not enabled!'
                cancel.click()
                time.sleep(0.1)


        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # คีย์ รายการใหม่ - Print PDF

                element = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[10]/div/div/button")) 
                )
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

                element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[10]/div/div/button'))
                )
                element.click()

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/ul/li[4]")) 
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

        # พิมพ์ PDF
                click = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[4]').click()
                time.sleep(0.1)


        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # คีย์ รายการใหม่ - ยกเลิกใบแจ้งหนี้

                element = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[10]/div/div/button")) 
                )
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

                element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[10]/div/div/button'))
                )
                assert element.is_displayed(), 'Element is not displayed!'
                assert element.is_enabled(), 'Element is not enabled!'
                element.click()

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/ul/li[3]")) 
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

        # ยกเลิกใบแจ้งหนี้
                click = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[5]').click()
                time.sleep(0.1)


        # ยกเลิกใบแจ้งหนี้

                key_input_text = WebDriverWait(driver, 10).until(
                     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div/div/div/div/input'))
                )
                key_input_text.send_keys('ชำระเรียบร้อย')
                time.sleep(0.5)

                cancel = WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[1]')) 
                )
                assert cancel.is_displayed(), 'Element is not displayed!'
                assert cancel.is_enabled(), 'Element is not enabled!'

                if cancel:
                     cancel.click()
                     print("Click Cancel Alrady :",True)
                else:
                     print("Cannot Click Cancel :",False)
                time.sleep(0.1)

                # Date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]')
                # assertTrue(Date.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
                # assertTrue(Date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
                # Date.click()
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



