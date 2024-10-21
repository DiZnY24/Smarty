
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



def test_page_add_bank1(driver):
        
        try:
            # หน้า บริหารโครงการ
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/properties')
            driver.implicitly_wait(20)

            # เพิ่มโครงการ
            Project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[1]/div[1]/div/button'))
            )
            assert Project.is_displayed(), 'Element is not displayed!'
            assert Project.is_enabled(), 'Element is not enabled!'
            Project.click()
            time.sleep(0.1)

            # รหัสอาคาร
        
            key_password = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_password.is_displayed(), 'Element is not displayed!'
            assert key_password.is_enabled(), 'Element is not enabled!'
            key_password.send_keys('DBL2')
            time.sleep(0.1)

            # ชื่อโครงการ (เต็ม)

            key_project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_project.is_displayed(), 'Element is not displayed!'
            assert key_project.is_enabled(), 'Element is not enabled!'
            key_project.send_keys('นิติบุคคลอาคารชุด ดับเบิ้ลเลค คอนโดมิเนียม DBL2')
            time.sleep(0.1)
        

            # ชื่อโครงการ (ย่อ)

            key_project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/div[3]/div/div[2]/div/div/input'))
            )
            assert key_project.is_displayed(), 'Element is not displayed!'
            assert key_project.is_enabled(), 'Element is not enabled!'
            key_project.send_keys('MTTD-DBL2')
            time.sleep(0.1)

            # เลขที่โครงการ

            key_project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_project.is_displayed(), 'Element is not displayed!'
            assert key_project.is_enabled(), 'Element is not enabled!'
            key_project.send_keys('1')
            time.sleep(0.1)

            # ขนาดพื้นที่ (ไร่)

            key_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys('2')
            time.sleep(0.1)

            # เบอร์ติดต่อ

            Phone_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[3]/div[1]/div/div[2]/div/div/input'))
            )
            assert Phone_number.is_displayed(), 'Element is not displayed!'
            assert Phone_number.is_enabled(), 'Element is not enabled!'
            Phone_number.send_keys('0659373995')
            time.sleep(0.1)

            # เลขประจำตัวผู้เสียภาษี

            key_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[3]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys('0994001106649')
            time.sleep(0.1)

            # อีเมล

            key_gmail = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[3]/div[3]/div/div[2]/div/div/input'))
            )
            assert key_gmail.is_displayed(), 'Element is not displayed!'
            assert key_gmail.is_enabled(), 'Element is not enabled!'
            key_gmail.send_keys('doublelake@msm-muangthong.com')
            time.sleep(0.1)

            # เลขที่อยู่

            Address_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[4]/div[1]/div/div[2]/div/div/input'))
            )
            assert Address_number.is_displayed(), 'Element is not displayed!'
            assert Address_number.is_enabled(), 'Element is not enabled!'
            Address_number.send_keys('84 หมู่5')
            time.sleep(0.1)

            # อาคาร

            building = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div/div/input'))
            )
            assert building.is_displayed(), 'Element is not displayed!'
            assert building.is_enabled(), 'Element is not enabled!'
            building.send_keys('-')
            time.sleep(0.1)

            # ถนน

            road = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[4]/div[3]/div/div[2]/div/div/input'))
            )
            assert road.is_displayed(), 'Element is not displayed!'
            assert road.is_enabled(), 'Element is not enabled!'
            road.send_keys('-')
            time.sleep(0.1)

            # อยู่ที่

            road = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[5]/div/div/div/div[2]/div/div/input'))
            )
            assert road.is_displayed(), 'Element is not displayed!'
            assert road.is_enabled(), 'Element is not enabled!'
            road.send_keys('บ้านใหม่ / ปากเกร็ด / นนทบุรี / 11120' + Keys.ARROW_DOWN + Keys.ENTER)
            time.sleep(0.1)

            # บันทึก

            # Save = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[2]/button'))
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click()
            # time.sleep(0.1)

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



