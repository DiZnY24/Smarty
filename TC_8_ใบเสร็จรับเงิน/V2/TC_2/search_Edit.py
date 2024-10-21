
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



def test_page_serach_edit(driver):
        
        try:
                # หน้า จัดการลูกหนี้
                driver.get('https://msm-smarty-cms-staging.hr-impact.co/receipt')
                driver.implicitly_wait(10)
                time.sleep(0.1)
        
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

        # คีย์ สถานะการชำระเงิน
                status_buy = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div'))
                )
                assert status_buy.is_displayed(), 'Element is not displayed!'
                assert status_buy.is_enabled(), 'Element is not enabled!'
                status_buy.click()
                time.sleep(0.2)

                status_buy = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
                )
                assert status_buy.is_displayed(), 'Element is not displayed!'
                assert status_buy.is_enabled(), 'Element is not enabled!'
                status_buy.click()
                time.sleep(0.1)

        # วันที่ วันชำระ (เริ่มต้น)

                Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div'))
                )
                assert Date.is_displayed(), 'Element is not displayed!'
                assert Date.is_enabled(), 'Element is not enabled!'
                Date.click()
                time.sleep(0.1)

                Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[3]'))
                )
                assert Date.is_displayed(), 'Element is not displayed!'
                assert Date.is_enabled(), 'Element is not enabled!'
                Date.click()
                time.sleep(0.1)

        # วันชำระ (สิ้นสุด)

                Date_buy = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div/div'))
                )
                assert Date_buy.is_displayed(), 'Element is not displayed!'
                assert Date_buy.is_enabled(), 'Element is not enabled!'
                Date_buy.click()
                time.sleep(0.1)

                Date_buy = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[7]'))
                )
                assert Date_buy.is_displayed(), 'Element is not displayed!'
                assert Date_buy.is_enabled(), 'Element is not enabled!'
                Date_buy.click()
                time.sleep(0.1)

        # วันที่สร้างเอกสาร (เริ่มต้น)

                date_create = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div/div/div'))
                )
                assert date_create.is_displayed(), 'Element is not displayed!'
                assert date_create.is_enabled(), 'Element is not enabled!'
                date_create.click()
                time.sleep(0.1)

                date_create = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[3]'))
                )
                assert date_create.is_displayed(), 'Element is not displayed!'
                assert date_create.is_enabled(), 'Element is not enabled!'
                date_create.click()
                time.sleep(0.1)

        # วันที่สร้างเอกสาร (สิ้นสุด)

                date_create = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div'))
                )
                assert date_create.is_displayed(), 'Element is not displayed!'
                assert date_create.is_enabled(), 'Element is not enabled!'
                date_create.click()
                time.sleep(0.1)

                date_create = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[7]'))
                )
                assert date_create.is_displayed(), 'Element is not displayed!'
                assert date_create.is_enabled(), 'Element is not enabled!'
                date_create.click()
                time.sleep(1)

        # ช่องทางการสร้างเอกสาร

                create = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div[2]/div/div/div'))
                )
                assert create.is_displayed(), 'Element is not displayed!'
                assert create.is_enabled(), 'Element is not enabled!'
                create.click()
                time.sleep(0.1)

                create = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[3]'))
                )
                assert create.is_displayed(), 'Element is not displayed!'
                assert create.is_enabled(), 'Element is not enabled!'
                create.click()
                time.sleep(0.1)

        # ประเภท

                type = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[4]/div[2]/div/div/div'))
                )
                assert type.is_displayed(), 'Element is not displayed!'
                assert type.is_enabled(), 'Element is not enabled!'
                type.click()
                time.sleep(0.1)

                type = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
                )
                assert type.is_displayed(), 'Element is not displayed!'
                assert type.is_enabled(), 'Element is not enabled!'
                type.click()
                time.sleep(0.1)

        # เลขที่เอกสาร

                number = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[1]/div/div[2]/div/div/input'))
                )
                assert number.is_displayed(), 'Element is not displayed!'
                assert number.is_enabled(), 'Element is not enabled!'
                number.send_keys('H2024096100045')
                time.sleep(0.1)

        # ชื่อ

                number = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[2]/div/div[2]/div/div/input'))
                )
                assert number.is_displayed(), 'Element is not displayed!'
                assert number.is_enabled(), 'Element is not enabled!'
                number.send_keys('นายบุญเลิศ ชูอนุรักษ์')
                time.sleep(0.1)

        # Refresh

                Refresh = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[3]/button')
                Refresh.click()


        # # ค้นหา element ที่ต้องการให้มองเห็น
        #         element_2 = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[10]/div/div/button")

        # # ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
        #         driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
        #         time.sleep(1)

        # สถานะการชำระเงิน

                status_buy = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[10]/div/div/button'))
                )
                assert status_buy.is_displayed(), 'Element is not displayed!'
                assert status_buy.is_enabled(), 'Element is not enabled!'
                status_buy.click()
                time.sleep(0.1)


        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/ul/li[1]"))  
                                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

        # พิมพ์ PDF 

                print_PDF = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
                )
                assert print_PDF.is_displayed(), 'Element is not displayed!'
                assert print_PDF.is_enabled(), 'Element is not enabled!'
                print_PDF.click()
                time.sleep(5)

                if print_PDF:
                       print("Click print pdf already :",True)
                else:
                       print("Cannot Click print pdf :",False)

        # ยกเลิกใบเสร็จ

                # cancel = WebDriverWait(driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]'))
                # )
                # assert cancel.is_displayed(), 'Element is not displayed!'
                # assert cancel.is_enabled(), 'Element is not enabled!'
                # cancel.click()
                # time.sleep(2)

                # if print_PDF:
                #     print("Click cancel already :",True)
                # else:
                #     print("Cannot Click cancel :",False)

                # Click = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')
                # Click.click()
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



