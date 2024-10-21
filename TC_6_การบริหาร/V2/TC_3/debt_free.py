
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
from selenium.common.exceptions import NoSuchElementException,TimeoutException


def test_page_debt_free(driver):
        
        try:
            # หน้า จัดการลูกหนี้
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/debtors')
            driver.implicitly_wait(10)

            # คลิก ใบปลอดหนี้

            click = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div/div/button[2]'))
            )
            assert click.is_displayed(), 'Element is not displayed!'
            assert click.is_enabled(), 'Element is not enabled!'
            click.click()
            time.sleep(0.1)

    # เช็คข้อความในปุ่ม - ดาวน์โหลด 
            button = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[1]/button')
            assert button.text == 'ดาวน์โหลด', f"Expected 'Expected Button Text' but got '{button.text}'"
            time.sleep(0.1)


            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)

            # โครงการ

            Project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/input'))
            )
            assert Project.is_displayed(), 'Element is not displayed!'
            assert Project.is_enabled(), 'Element is not enabled!'
            Project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
            time.sleep(0.1)

            # คีย์ ชั้น / ห้อง

            floor_room = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div'))
            )
            assert floor_room.is_displayed(), 'Element is not displayed!'
            assert floor_room.is_enabled(), 'Element is not enabled!'
            floor_room.click()
            time.sleep(0.1)

            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/input"))  
            )

            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)

            floor_room = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/input'))
            )
            assert floor_room.is_displayed(), 'Element is not displayed!'
            assert floor_room.is_enabled(), 'Element is not enabled!'
            floor_room.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)
            time.sleep(0.1)

            # ค้นหารายชื่อ

            Key_name = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/input'))
            )
            assert Key_name.is_displayed(), 'Element is not displayed!'
            assert Key_name.is_enabled(), 'Element is not enabled!'
            Key_name.send_keys('นายนิธิศ สมทรัพย์เสถียร')
            time.sleep(0.1)

    # สถานะ

            status = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div'))
            )
            assert status.is_displayed(), 'Element is not displayed!'
            assert status.is_enabled(), 'Element is not enabled!'
            status.click()
            time.sleep(0.1)

            status = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]'))
            )
            assert status.is_displayed(), 'Element is not displayed!'
            assert status.is_enabled(), 'Element is not enabled!'
            status.click()
            time.sleep(0.1)
            
    # เลขที่เอกสาร

            Document_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/div[2]/div/div/input'))
            )
            assert Document_number.is_displayed(), 'Element is not displayed!'
            assert Document_number.is_enabled(), 'Element is not enabled!'
            Document_number.send_keys('2024085400001')
            time.sleep(0.1)        


            # check_text = driver.find_element(By.XPATH, '//div/div/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[4]/p')

            # check_name = 'นายนิธิศ สมทรัพย์เสถียร'
            # test_text = check_text.text

            # if test_text == check_text:
            #     print("ข้อความถูกต้อง!")
            # else:
            #     print("ข้อความไม่ถูกต้อง!")
            
    # Refresh

            Refresh = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/button'))
            )
            assert Refresh.is_displayed(), 'Element is not displayed!'
            assert Refresh.is_enabled(), 'Element is not enabled!'
            Refresh.click()
            time.sleep(0.1)  



            
                 
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



