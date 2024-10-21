
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
from selenium.common.exceptions import NoSuchElementException, TimeoutException



def test_page_search_room(driver):
        # หน้า จัดการลูกหนี้
        driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/units')
        driver.implicitly_wait(20)

        try:
            try:
                # คีย์ โครงการ
                Project = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
                )
                assert Project.is_displayed(), 'element is not dispalyed!'
                assert Project.is_enabled(), 'Element is not selected!'
                Project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.5)            
            except AssertionError as e:
                driver.fail('เงื่อนไขไม่ตรง'+ str(e))
                
            
            try:
            # คีย์ ชั้น / ห้อง
                floor = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/input'))
                )
                assert floor.is_displayed(), 'element is not dispalyed!'
                assert floor.is_enabled(), 'Element is not selected!'
                floor.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.5)
            except AssertionError as e:
                driver.fail('Element not Found'+ str(e))
                 
            try:
            # ประเภท

                type = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[1]/div[2]/div/div/div'))
                )
                assert type.is_displayed(), 'element is not dispalyed!'
                assert type.is_enabled(), 'Element is not selected!'
                type.click()
                time.sleep(0.5)

                type = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
                )
                assert type.is_displayed(), 'element is not dispalyed!'
                assert type.is_enabled(), 'Element is not selected!'
                type.click()
                time.sleep(0.5)

            except AssertionError as e:
                driver.fail('Element not Found: '+ str(e))


            try:
            # ค้นหาชื่อ

                search_name = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[2]/div/div[2]/div/div/input'))
                )
                assert search_name.is_displayed(), 'element is not dispalyed!'
                assert search_name.is_enabled(), 'Element is not selected!'
                search_name.send_keys('นางอำไพ นิมานะ')
                time.sleep(0.3)

            except AssertionError as e:
                driver.fail('Element not Found: '+ str(e))
            time.sleep(0.1)


            # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
            # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)
            

            try:
            # Refresh

                wait_element = WebDriverWait(driver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@title="อาคาร A1"]'))
                )
                if wait_element:
                    print('ข้อความถูกต้อง!',True)
                else:
                    print('ข้อมความไม่ถูกต้อง!',False)

                Refresh = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/button'))
                )
                assert Refresh.is_displayed(), 'element is not dispalyed!'
                assert Refresh.is_enabled(), 'Element is not selected!'
                Refresh.click()
                time.sleep(0.5)

            except AssertionError as e:
                driver.fail('Element not Found: '+ str(e))
                
        except TimeoutException as e : 
            driver.fail(f"เกิดข้อผิดพลาดในการโหลดหน้า : {e}")

            

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



