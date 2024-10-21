
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



def add_banner(driver):

        try:
            # หน้า จัดการแบนเนอร์
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/banner')
            driver.implicitly_wait(30)
            
            Add_Banner = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div[1]/div/div/button'))
            )
            assert Add_Banner.is_displayed(), 'Element is not displayed!'
            assert Add_Banner.is_enabled(), 'Element is not enabled!'
            Add_Banner.click()               

            # ชื่อแบนเนอร์

            Add_name = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/input'))
            )
            assert Add_name.is_displayed(), 'Element is not displayed!'
            assert Add_name.is_enabled(), 'Element is not enabled!'
            Add_name.send_keys('News_Kub') 

            # อัพโหลดรูปภาพ Mac Os

            upload = driver.find_element(by=By.XPATH , value='/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[1]/div/div/div/input')
            upload.send_keys('/Users/dizny/Downloads/Image/image Test/Logo.jpg.jpg')

            # date วันที่ วันที่เผยแพร่

            date = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[3]/div[2]/div/div'))
            )
            assert date.is_displayed(), 'Element is not displayed!'
            assert date.is_enabled(), 'Element is not enabled!'
            date.click()   

            select_date = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[1]'))
            )
            assert select_date.is_displayed(), 'Element is not displayed!'
            assert select_date.is_enabled(), 'Element is not enabled!'
            select_date.click()   

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

            time.sleep(3)

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
                        







