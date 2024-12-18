
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller 
from selenium.webdriver.support.ui import Select
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner
import unittest
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import pyautogui


def page_edit_news(driver):

        try:
            # หน้า ข่าวสาร
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/announcement')
            driver.implicitly_wait(20)

             # Click เข้าแก้ไข 

            Edit_News = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[9]/button[1]'))
            )
            assert Edit_News.is_displayed(), 'Element is not displayed!'
            assert Edit_News.is_enabled(), 'Element is not enabled!'        
            Edit_News.click()    

            if Edit_News:
                print('Click Edit News :',(True))
            else:
                print('Cannot Click Edit News :',(False))        

            # กรอกข้อมูล

            #ชื่อข่าวสาร

            Add_name = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/input'))
            )
            assert Add_name.is_displayed(), 'Element is not displayed!'
            assert Add_name.is_enabled(), 'Element is not enabled!'        
            Add_name.send_keys(Keys.COMMAND + "a" + Keys.DELETE)
            Add_name.send_keys('New_Kub') 

            # คลิกลบรูป

            Delete_image = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[1]/div/div/button'))
            )
            assert Delete_image.is_displayed(), 'Element is not displayed!'
            assert Delete_image.is_enabled(), 'Element is not enabled!'        
            Delete_image.click() 

            if Delete_image:
                print('Click Delete Image :',(True))
            else:
                print('Cannot Click Delete Image :',(False)) 

            # # คลิกเพิ่มรูปใหม่

            upload = driver.find_element(by=By.XPATH , value='/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[1]/div/div/input')
            upload.send_keys('/Users/dizny/Downloads/Image/image Test/Logo.jpg.jpg')

            # วันที่เผยแพร่

            select_date = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[3]/div[2]/div/div'))
            )
            assert select_date.is_displayed(), 'Element is not displayed!'
            assert select_date.is_enabled(), 'Element is not enabled!'        
            select_date.click()  

            # # เลือกวันที่ ....                 

            # time.sleep(0.5)
            # if pyautogui:
            #     pyautogui.click(x=821, y=660)
            #     print('Click select date 16 :',True)
            # else:
            #     print('Cannot date',False)

            time.sleep(0.5)
            if pyautogui:
                pyautogui.click(x=781, y=737)
                print('Click select date 29 :',True)
            else:
                print('Cannot date',False)
                
            # select_date = WebDriverWait(driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '//div/div[2]/div/div/div[2]/div/div[5]/button[2]'))
            # )
            # assert select_date.is_displayed(), 'Element is not displayed!'
            # assert select_date.is_enabled(), 'Element is not enabled!'        
            # select_date.click()          

            # รายละเอียดข่าวสาร

            Edit_key = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/div'))
            )
            assert Edit_key.is_displayed(), 'Element is not displayed!'
            assert Edit_key.is_enabled(), 'Element is not enabled!'        
            Edit_key.click()    

            # แก้ไข รายละเอียด

            # ค้นหา element ที่ต้องการให้มองเห็น
            element_2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/div")

            # ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
            driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
            time.sleep(1)

            wait_add_text = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '//div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div'))
            )
            print('Key Text :',(True))

            Add_Text = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div'))
            )
            assert Add_Text.is_displayed(), 'Element is not displayed!'
            assert Add_Text.is_enabled(), 'Element is not enabled!'        
            Add_Text.click()

            Add_Text = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div'))
            )
            assert Add_Text.is_displayed(), 'Element is not displayed!'
            assert Add_Text.is_enabled(), 'Element is not enabled!'        
            Add_Text.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Add_Text.send_keys('TestNew')

            time.sleep(1)

            Check_messages = driver.find_element(By.XPATH, '//div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div')
            expected_text = 'TestNew'
            assert Check_messages.text == expected_text, f"ข้อความไม่ตรงกัน: คาดว่า '{expected_text}' แต่ได้ '{Check_messages.text}'"
            time.sleep(0.1)

            # เลื่อนจอขึ้น
            driver.execute_script("window.scrollTo(0, -900)")

            # กด บันทึก

            save = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[1]/div/button[2]'))
            )
            assert save.is_displayed(), 'Element is not displayed!'
            assert save.is_enabled(), 'Element is not enabled!'        
            save.click()

            if save:
                print('Click Save :',(True))
            else:
                print('Cannot Click Save :',(False))
            
            time.sleep(3)

            while True:

                Check_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[3]/p')))

                if Check_element.text == 'New_Kub':
                    print('ข้อความขึ้นถูกต้อง!',True)
                    break
                elif Check_element.text == 'New_Kub ข้อความขึ้นเป็นอีกแบบ':
                    print('ข้อมความขึ้นไม่ถูกต้อง!!! :',False)
                else:
                    print('ไม่ตรงเงื่อนไขที่ตั้งไว้',False)
                    break
           
                time.sleep(0.5)

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
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\3.ข่าวสาร\\Reports'))
       
        
                







