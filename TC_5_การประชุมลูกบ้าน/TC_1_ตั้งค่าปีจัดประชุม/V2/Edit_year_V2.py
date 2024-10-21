
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller 
import traceback
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException,TimeoutException


def page_edit_year(driver):
        
# หน้า แก้ไขตั้งค่าปีจัดประชุม
        try:
        
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/agm/years')
            driver.implicitly_wait(30)

            Click_Add_year = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[3]/div[3]/div/button'))
            )
            assert Click_Add_year.is_displayed(), 'Element is not displayed!'
            assert Click_Add_year.is_enabled(), 'Element is not enabled!'
            
            if Click_Add_year:
                Click_Add_year.click()
                print('Click Edit year Already :', True)
            else:
                driver.fail('Cannot Edit year :', False)


            Edit_name = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div/div/div/div[2]/div/div/input'))
            )
            assert Edit_name.is_displayed(), 'Element is not displayed!'
            assert Edit_name.is_enabled(), 'Element is not enabled!'
            
            if Edit_name:
                Edit_name.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
                Edit_name.send_keys('2569' + Keys.ENTER)
                print('Click Edit year 2569 Already :', True)
            else:
                driver.fail('Cannot Edit year :', False)

            time.sleep(2)

        except ArithmeticError as e:
            driver.fail(f'ตรวจสอบไม่สำเร็จ: {e}')
        except NoSuchElementException as b:
            driver.fail(f'ไม่พบองค์ประกอบของ Elenemt: {b}')
        except Exception as n:
            driver.fail(f'เงื่อนไขไม่ตรงตามที่คาดหวัง: {n}')
        except TimeoutException:
            driver.fail('การรอองค์ประกอบล้มเหลว')


if __name__ == '__main__':
    unittest.main()


# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\5.การประชุมลูกบ้าน\\Reports'))