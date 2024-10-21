
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
from selenium.common.exceptions import NoSuchElementException,TimeoutException



def test_page_search(driver):

        try:    
            # หน้า การบริหาร - ผู้ใช้งาน
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/residents')
            driver.implicitly_wait(30)

            # คีย์ ชื่อ-เบอร์
            
            search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div[1]/div[2]/div/div/div/div/input')
            search_box.send_keys('0800000000')

            # รอจนกว่า Element ที่เราต้องการโชว์

            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[3]"))  
            )
            print("Element แสดงผลถูกต้องแล้ว!")

            Check_Number = driver.find_element(By.XPATH, '//*[@class="MuiTableBody-root mui-style-1xnox0e"]//tr//td[5]')

            check_text = '0800000000'
            test_text = Check_Number.text

            if test_text == check_text:
                print("ข้อความถูกต้อง!")
            else:
                print("ข้อความไม่ถูกต้อง!")
            
            time.sleep(2)
        

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
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



