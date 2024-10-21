
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


def test_page_search_edit(driver):

        try:
                # หน้า จัดการลูกหนี้
                driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/debtors')
                driver.implicitly_wait(10)
                
        # คีย์ โครงการ

                project = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/input')) 
                )
                assert project.is_displayed(), 'Element is not displayed!'
                assert project.is_enabled(), 'Element is not enabled!'
                project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)

        # คีย์ ชั้น / ห้อง

                floor = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/input'))
                )
                assert floor.is_displayed(), 'floor is not displayed!'
                assert floor.is_enabled(), 'Element is not enabled!'
                floor.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)

        # คีย์ ค้นหารายชื่อ

                key_name = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/input'))
                )
                assert key_name.is_displayed(), 'Element is not displayed!'
                assert key_name.is_enabled(), 'Element is not enabled!'
                key_name.send_keys('อาม ม่อน เสิน 23')
                
        # # Refresh

                Refresh = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button'))
                )
                assert Refresh.is_displayed(), 'Element is not displayed!'
                assert Refresh.is_enabled(), 'Element is not enabled!'
                Refresh.click()

        # -----------------------------------------------------------------------------------------------------------------------------------------------

        # คลิกการจัดการ

                management = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[8]/div/div'))
                )
                assert management.is_displayed(), 'Element is not displayed!'
                assert management.is_enabled(), 'Element is not enabled!'
                management.click()
                time.sleep(0.1)
                
        # สร้างใบปลอดหนี้แบบปกติ


                management = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
                )
                assert management.is_displayed(), 'Element is not displayed!'
                assert management.is_enabled(), 'Element is not enabled!'
                management.click()
                time.sleep(0.1)

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/form/div/div[1]/div/div/div")) 
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)

        #Click วันชำระ


                Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/form/div/div[1]/div/div/div'))
                )
                assert Date.is_displayed(), 'Element is not displayed!'
                assert Date.is_enabled(), 'Element is not enabled!'
                Date.click()
                time.sleep(0.1)      

                Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[2]'))
                )
                assert Date.is_displayed(), 'Element is not displayed!'
                assert Date.is_enabled(), 'Element is not enabled!'
                Date.click()
                time.sleep(0.1)      

        # Click Show ค่าส่วนกลาง 

                Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/form/div/div[4]/table/tbody/tr[1]/td[1]/button'))
                )
                assert Date.is_displayed(), 'Element is not displayed!'
                assert Date.is_enabled(), 'Element is not enabled!'
                Date.click()
                time.sleep(0.1)      

        # CLick Save 
        
                Save = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/form/div/div[6]/button[2]'))
                )
                assert Save.is_displayed(), 'Element is not displayed!'
                assert Save.is_enabled(), 'Element is not enabled!'
                Save.click()
                time.sleep(0.1)         

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div"))  
                )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1)



        # วันที่ กรอกฟอร์ม

                Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div'))
                )
                assert Date.is_displayed(), 'Element is not displayed!'
                assert Date.is_enabled(), 'Element is not enabled!'
                Date.click()
                time.sleep(0.1)   

                Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div/div/div/div[2]/div/div[2]/div/div/div[10]/button'))
                )
                assert Date.is_displayed(), 'Element is not displayed!'
                assert Date.is_enabled(), 'Element is not enabled!'
                Date.click()
                time.sleep(0.1)   

                Date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[3]/div/div/div/div[2]/div/div[2]/div/div/div[125]/button'))
                )
                assert Date.is_displayed(), 'Element is not displayed!'
                assert Date.is_enabled(), 'Element is not enabled!'
                Date.send_keys(Keys.ESCAPE)
                time.sleep(0.1)   

        # Input Text ข้าพเจ้าบริษัท

                Input_Text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div/div/input'))
                )
                assert Input_Text.is_displayed(), 'Element is not displayed!'
                assert Input_Text.is_enabled(), 'Element is not enabled!'
                Input_Text.send_keys('Impact')
                time.sleep(0.1)

        # Input Text ของนิติบุคคลอาคารชุดฯ โดย

                Input_Text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/div[3]/div/div/input'))
                )
                assert Input_Text.is_displayed(), 'Element is not displayed!'
                assert Input_Text.is_enabled(), 'Element is not enabled!'
                Input_Text.send_keys('อาคาร A1')
                time.sleep(0.1)

        # Input Text ของนิติบุคคลอาคารชุดฯ โดย

                Input_Text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/div[4]/div/div/div/input'))
                )
                assert Input_Text.is_displayed(), 'Element is not displayed!'
                assert Input_Text.is_enabled(), 'Element is not enabled!'
                Input_Text.send_keys('Test')
                time.sleep(0.1)

                driver.refresh()

        # Save 

                # Save = WebDriverWait(driver, 10).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div[2]/button'))
                # )
                # assert Save.is_displayed(), 'Element is not displayed!'
                # assert Save.is_enabled(), 'Element is not enabled!'
                # Save.click()
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



