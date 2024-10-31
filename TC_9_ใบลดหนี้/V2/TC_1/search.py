
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
import pyautogui


def test_page_search_edit(driver):

        try:
                # หน้า จัดการลูกหนี้
                driver.get('https://msm-smarty-cms-staging.hr-impact.co/credit-note')
                driver.implicitly_wait(10)

        # คีย์ โครงการ

                key_project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div[2]/div/div/input'))
                )
                assert key_project.is_displayed(), 'Element is not displayed!'
                assert key_project.is_enabled(), 'Element is not enabled!'
                key_project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.1)

        # คีย์ ชั้น / ห้อง

                floor_room = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div/input'))
                )
                assert floor_room.is_displayed(), 'Element is not displayed!'
                assert floor_room.is_enabled(), 'Element is not enabled!'
                floor_room.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.1)

        # วันที่ วันที่ออกเอกสาร

                Date = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div'))
                )
                assert Date.is_displayed(), 'Element is not displayed!'
                assert Date.is_enabled(), 'Element is not enabled!'
                Date.click()         
                # time.sleep(0.1)

                time.sleep(0.5)
                if pyautogui:
                   pyautogui.click(x=782, y=736)
                   print('Click select Day 29 :',True)
                else:
                   print('Cannot date',False) 

                # Date = WebDriverWait(driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '//div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[3]'))
                # )
                # assert Date.is_displayed(), 'Element is not displayed!'
                # assert Date.is_enabled(), 'Element is not enabled!'
                # Date.click()         
                time.sleep(0.1)

        # สถานะ

                status = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div'))
                )
                assert status.is_displayed(), 'Element is not displayed!'
                assert status.is_enabled(), 'Element is not enabled!'
                status.click()         
                time.sleep(0.1)

                status = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
                )
                assert status.is_displayed(), 'Element is not displayed!'
                assert status.is_enabled(), 'Element is not enabled!'
                status.click()         
                time.sleep(0.1)

        # ค้นหา เลขที่เอกสาร

                key_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div/input'))
                )
                assert key_number.is_displayed(), 'Element is not displayed!'
                assert key_number.is_enabled(), 'Element is not enabled!'
                key_number.send_keys('CN2024096100005')
                time.sleep(0.1)

        # ค้นหา ชื่อ

                key_name = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[1]/div/div[2]/div/div/input'))
                )
                assert key_name.is_displayed(), 'Element is not displayed!'
                assert key_name.is_enabled(), 'Element is not enabled!'
                key_name.send_keys('นางสาวสุธิมา  สุขสมบูรณ์')
                time.sleep(0.1)
        

        # Refresh

                Refresh = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[2]/button'))
                )
                assert Refresh.is_displayed(), 'Element is not displayed!'
                assert Refresh.is_enabled(), 'Element is not enabled!'
                Refresh.click()         
                time.sleep(0.1)
                
        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div")) 
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("รอจนกว่าปุ่มสถานะจะปรากฏขึ้น.")
                time.sleep(0.1) 

        # สถานะ 

                # status = WebDriverWait(driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[8]/div/div/button'))
                # )
                # assert status.is_displayed(), 'Element is not displayed!'
                # assert status.is_enabled(), 'Element is not enabled!'
                # status.click()         
                # time.sleep(0.1)

                # element = WebDriverWait(driver, 10).until(
                # EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/ul/li[1]")) 
                # )
                # print("Element is visible. Proceeding with the next step.")
                # time.sleep(0.1) 


        # พิมพ์ PDF

                # print_pdf = WebDriverWait(driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
                # )
                # assert print_pdf.is_displayed(), 'Element is not displayed!'
                # assert print_pdf.is_enabled(), 'Element is not enabled!'

                # if print_pdf: 
                #     print_pdf.click()         
                #     print("Click print PDF Already :",True)
                # else:
                #      print("Cannot Click print PDF :",False)
                # time.sleep(0.1)


        # คลิกสร้างสำเร็จ

                click = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[8]/div/div/button'))
                )
                assert click.is_displayed(), 'Element is not displayed!'
                assert click.is_enabled(), 'Element is not enabled!'
                click.click()

                click = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]'))
                )
                assert click.is_displayed(), 'Element is not displayed!'
                assert click.is_enabled(), 'Element is not enabled!'
                click.click()

        # ยกเเลิก

                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div[3]/button[1]")) 
                )
                print("รอจนกว่าจะโชว์เมนูปรากฏขึ้น.")
                time.sleep(0.1) 

                key_input_text = WebDriverWait(driver, 10).until(
                     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div/div/div/div/input'))
                )
                key_input_text.send_keys("ชำระเรียบร้อย")
                time.sleep(0.5)

                cancel = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[1]'))
                )
                assert cancel.is_displayed(), 'Element is not displayed!'
                assert cancel.is_enabled(), 'Element is not enabled!'
                
                if cancel: 
                    cancel.click()
                    print("Click Cancel Already :",True)
                else:
                     print("Cannot Click Cancel :",False)

        # ยืนยัน

                # confirm = WebDriverWait(driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]'))
                # )
                # assert confirm.is_displayed(), 'Element is not displayed!'
                # assert confirm.is_enabled(), 'Element is not enabled!'
                
                # if confirm: 
                #     confirm.click()
                #     print("Click Comfirm Already :",True)
                # else:
                #      print("Cannot Click Comfirm :",False)



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



