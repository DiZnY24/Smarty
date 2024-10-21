
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


def test_page_report(driver):

        try:            
            # หน้า จัดการลูกหนี้
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/report/daily')
            driver.implicitly_wait(10)
            time.sleep(1)


    # วันเริ่มต้น

    #         Date = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div/div[1]/div/div')
    #         assertTrue(Date.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
    #         assertTrue(Date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
    #         Date.click()
    #         time.sleep(0.1)

    #         Date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/button[1]')
    #         assertTrue(Date.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
    #         assertTrue(Date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
    #         Date.click()
    #         time.sleep(0.1)

    #         ESC = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/button[1]')
    #         ESC.send_keys(Keys.ESCAPE)

    # # # วันสิ้นสุด

    #         Date = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div/div[2]/div/div')
    #         assertTrue(Date.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
    #         assertTrue(Date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
    #         Date.click()
    #         time.sleep(0.1)

    #         Date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/button[7]')
    #         assertTrue(Date.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
    #         assertTrue(Date.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
    #         Date.click()
    #         time.sleep(0.1)

    #         ESC = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/button[7]')
    #         ESC.send_keys(Keys.ESCAPE)


            Download = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[1]/div/button').click()
            time.sleep(2.5)
            print('ดาวโหลด นิติบุคคลอาคารชุด ดับเบิ้ลเลค คอนโดมิเนียม เฟส 2 เรียบร้อย')
            
            Download = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[2]/div/button').click()
            time.sleep(2.5)
            print('ดาวโหลด testhi เรียบร้อย')

            Download = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div[3]/div/button').click()
            time.sleep(2.5)
            print('ดาวโหลด นิติบุคคลอาคารชุด เมืองทอง เรียบร้อย')



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



