
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


def test_page_User(driver):

        try:
                # หน้า การบริหาร - ผู้ใช้งาน
                driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/residents')
                driver.implicitly_wait(30)

                # เพิ่มลูกบ้าน

                Add = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div[1]/div[1]/div[2]/button[2]'))
                )
                assert Add.is_displayed(), 'Element is not displayed!'
                assert Add.is_enabled(), 'Element is not enabled!'
                Add.click()

                if Add:
                    print('Click Add Already :', True)
                else:
                    print('Cannot Click Add :',False)
                    

                # Upload image

                # อัพโหลดรูปภาพ Mac Os
                upload = driver.find_element(by=By.XPATH , value='//div/div/div/div/div/div/form/div/div[1]/input')
                upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')
                time.sleep(0.5)

                # คีย์ ชื่อ

                # click = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[2]/div[1]/div/div[2]/div/div')
                # click.click()
                # time.sleep(0.1)

                key_name = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[2]/div[1]/div/div[2]/div/div/input'))
                )
                assert key_name.is_displayed(), 'Element is not displayed!'
                assert key_name.is_enabled(), 'Element is not enabled!'
                key_name.send_keys('สมศรี')

                # คีย์ นามสกุล

                Key_Text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[2]/div[2]/div/div[2]/div/div/input'))
                )
                assert Key_Text.is_displayed(), 'Element is not displayed!'
                assert Key_Text.is_enabled(), 'Element is not enabled!'
                Key_Text.send_keys('พร้อมจ่าย')

                # คีย์ Email 

                key_email = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[3]/div[1]/div/div[2]/div/div/input'))
                )
                assert key_email.is_displayed(), 'Element is not displayed!'
                assert key_email.is_enabled(), 'Element is not enabled!'
                key_email.send_keys('sss@gmail.com')
                
                # เบอร์โทรศัพท์
                
                key_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[3]/div[2]/div/div[2]/div/div/input'))
                )
                assert key_number.is_displayed(), 'Element is not displayed!'
                assert key_number.is_enabled(), 'Element is not enabled!'
                key_number.send_keys('0924296825')
                
                # เลขปประจำตัวประชาชน

                key_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[4]/div/div[2]/div/div/input'))
                )
                assert key_number.is_displayed(), 'Element is not displayed!'
                assert key_number.is_enabled(), 'Element is not enabled!'
                key_number.send_keys('012345678912')
                time.sleep(2)
                # Save

                # Save = WebDriverWait(driver, 10).until(
                # EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/button'))
                # )
                # assert Save.is_displayed(), 'Element is not displayed!'
                # assert Save.is_enabled(), 'Element is not enabled!'
                # Save.click()

                # if Save:
                #     print('Click Save Already :', True)
                # else:
                #     print('Cannot Click Save :',False)

                # # ดึงตำแหน่งของ element
                # location = element.location  # dictionary ที่มี 'x' และ 'y'
                # size = element.size          # dictionary ที่มี 'width' และ 'height'
                
                # print(f'Button : Save')
                # print(f"ตำแหน่งของ element: {location}")
                # print(f"ขนาดของ element: {size}")

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



