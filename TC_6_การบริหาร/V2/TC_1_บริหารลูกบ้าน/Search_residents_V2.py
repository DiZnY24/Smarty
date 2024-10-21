
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



def test_page_Resident(driver):

        try:
                # หน้า การบริหาร - ผู้ใช้งาน

                driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/users')
                driver.implicitly_wait(30)

                # คีย์ หมายเลขบัตรประชาชน

                Key_Text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div/input')) #คีย์ เลขประชาชน
                )
                assert Key_Text.is_displayed(), 'Element is not displayed!'
                assert Key_Text.is_enabled(), 'Element is not enabled!'
                Key_Text.send_keys('0000000000000')

                # คีย์ ชื่อ

                key_name = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/input')) #คีย์ ชื่อ
                )
                assert key_name.is_displayed(), 'Element is not displayed!'
                assert key_name.is_enabled(), 'Element is not enabled!'
                key_name.send_keys('kanapok')

                # เลือก สถานะ

                status = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div')) # เลือก ห้องมี
                )
                assert status.is_displayed(), 'Element is not displayed!'
                assert status.is_enabled(), 'Element is not enabled!'
                status.click()

                

                # เลือก สถานะ มีห้อง

                room = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]')) # เลือกห้องที่มี
                )
                assert room.is_displayed(), 'Element is not displayed!'
                assert room.is_enabled(), 'Element is not enabled!'
                room.click()

                # ค้นหา

                search = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/button[2]')) # ค้นหา
                )
                assert search.is_displayed(), 'Element is not displayed!'
                assert search.is_enabled(), 'Element is not enabled!'
                search.click()
        
                time.sleep(0.1)

                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, 
                "/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
                )
                print("Wait Show Element :",True )
                
                button = driver.find_element(By.XPATH, '//div/div/div[2]/div[2]/div/div/div/div/div[2]/div')
                assert button.text == 'kanapok', f"Expected 'Expected Button Text' but got '{button.text}'"
                time.sleep(2)

                # ล้างข้อมความทั้งหมด

                element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/button[1]')) # ล้างข้อมความทั้งหมด
                )
                element.click()
                time.sleep(0.1)

        except ArithmeticError as e:
            print(f'ตรวจสอบไม่สำเร็จ: {e}')
        except NoSuchElementException as b:
            print(f'ไม่พบองค์ประกอบของ Elenemt: {b}')
        except Exception as n:
            print(f'เงื่อนไขไม่ตรงตามที่คาดหวัง: {n}')
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว')


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



