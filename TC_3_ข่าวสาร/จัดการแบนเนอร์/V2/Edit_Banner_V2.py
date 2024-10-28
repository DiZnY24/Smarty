
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller 
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import pyautogui

def page_edit_banner(driver):

        try:
            # หน้า ข่าวสาร
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/banner')
            driver.implicitly_wait(10)

            Edit_Banner = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[7]/button[1]'))
            )
            assert Edit_Banner.is_displayed(), 'Element is not displayed!'
            assert Edit_Banner.is_enabled(), 'Element is not enabled!'    
            Edit_Banner.click()
            
            # กรอกข้อมูล
            # ชื่อแบนเนอร์

            Edit_name = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/input'))
            )
            assert Edit_name.is_displayed(), 'Element is not displayed!'
            assert Edit_name.is_enabled(), 'Element is not enabled!'    
            time.sleep(0.3)
            Edit_name.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Edit_name.send_keys('Kub')     

            # เลือก รูปภาพ

            Delete_image = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[1]/div/div/div/button'))
            )
            assert Delete_image.is_displayed(), 'Element is not displayed!'
            assert Delete_image.is_enabled(), 'Element is not enabled!'    
            Delete_image.click()

            # อัพโหลดรูปภาพ Mac Os

            upload = driver.find_element(by=By.XPATH , value='/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[1]/div/div/div/input')
            upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')
            time.sleep(1)

            # date วันที่ วันที่เผยแพร่

            Click_date = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[3]/div[2]/div/div'))
            )
            assert Click_date.is_displayed(), 'Element is not displayed!'
            assert Click_date.is_enabled(), 'Element is not enabled!'    
            Click_date.click()

            time.sleep(0.5)
            if pyautogui:
                pyautogui.click(x=781, y=737)
                print('Click select date 29 :',True)
            else:
                print('Cannot date',False)

            # select_date = WebDriverWait(driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/button[4]'))
            # )
            # assert select_date.is_displayed(), 'Element is not displayed!'
            # assert select_date.is_enabled(), 'Element is not enabled!'    
            # select_date.click()


            Save = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[1]/div[2]/button[2]'))
            )
            assert Save.is_displayed(), 'Element is not displayed!'
            assert Save.is_enabled(), 'Element is not enabled!'    
            Save.click()

            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[2]/div[1]/div/table/tbody/tr[1]/td[1]/p"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
            print('Element Show :',(True))

            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[3]/p"))  
            )
            if element.text == 'Kub':
                    print('ข้อความตรงกัน')
            elif element.text == 'Kubผิดพลาด':
                    print('ข้อความเป็นอีกแบบ')
            else:
                    print('ข้อความไม่ตรงกับเงื่อนไขใด ๆ')

            time.sleep(1)

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
                        
        




