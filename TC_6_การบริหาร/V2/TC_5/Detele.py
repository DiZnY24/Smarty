
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException,TimeoutException



def test_page_delete_room(driver):
        # หน้า การบริหาร - ผู้ใช้งาน
        driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/units')
        driver.implicitly_wait(10)
        resutl = None

        try:
            # Detele

            delete = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[9]/div/button'))
            )
            assert delete.is_displayed(), 'Element is not displayed!'
            assert delete.is_enabled(), 'Element is not enabled!'
            if delete:
                delete.click()
                print('Click delete Already :', True)
            elif delete:
                print('Cannot Click delete :',False)
            else:
                print('ไม่ตรงกับเงื่อนไขใดๆ',False)

            time.sleep(0.5)

            cancel = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[1]')
            assert cancel.is_displayed(), 'Element is not displayed!'
            assert cancel.is_enabled(), 'Element is not enabled!'
            
            if cancel:
                cancel.click()
                print('Click Cancel Already :', True)
            elif cancel:
                print('Cannot Click Cancel :',False)
            else:
                print('ไม่ตรงกับเงื่อนไขใดๆ',False)
            
            # comfirm = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]')
            # assert comfirm.is_displayed(), 'Element is not displayed!'
            # assert comfirm.is_enabled(), 'Element is not enabled!'
            # comfirm.click()

            # เช็คข้อความในปุ่ม เพิ่มห้อง
            button = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[1]/div/button')
            assert button.text == 'เพิ่มห้อง', f"Expected 'Expected Button Text' but got '{button.text}'"

            # เช็คข้อความในปุ่ม ดาวโหลดข้อมูล
            button = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[2]/div/div/button')
            assert button.text == 'ดาวโหลดข้อมูล', f"Expected 'Expected Button Text' but got '{button.text}'"

            # เช็คข้อความในปุ่ม อัพโหลดข้อมูล
            button = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[2]/div/button')
            assert button.text == 'อัพโหลดข้อมูล', f"Expected 'Expected Button Text' but got '{button.text}'"

            # หาองค์ประกอบที่เราต้องการตรวจสอบ
            element = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[1]/p')
            # ใช้คำสั่ง if, elif, else เพื่อดำเนินการตามเงื่อนไข
            if element.text == 'โครงการ':
                print('ข้อความตรงกัน')
                # ทำสิ่งที่ต้องการเมื่อข้อความตรงกัน
            elif element.text == 'โครงการผิดพลาด':
                print('ข้อความเป็นอีกแบบ')
                # ทำสิ่งที่ต้องการเมื่อข้อความเป็นอีกแบบ
            else:
                print('ข้อความไม่ตรงกับเงื่อนไขใด ๆ')
                # ทำสิ่งที่ต้องการเมื่อข้อความไม่ตรงกับเงื่อนไขใด ๆ
            
            time.sleep(2)

            # คลิก

        except NoSuchElementException:
            driver.fail('Element not Found')
        except AssertionError as e:
            driver.fail(str(e))
        except Exception as n:
            driver.fail(f'An unexpected error occurred: {n}')
        except TimeoutException as m:
            driver.fail(f'การรอองค์ประกอบล้มเหลว: {m}')
        return resutl


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



