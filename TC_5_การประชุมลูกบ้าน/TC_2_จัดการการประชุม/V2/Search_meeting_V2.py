
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys 
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException,TimeoutException


def page_search(driver):
        try:
                # เปิดหน้า จัดการประชุม
                driver.get('https://msm-smarty-cms-staging.hr-impact.co/agm/meetings')
                driver.implicitly_wait(30)


                project = WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div'))
                )
                assert project.is_displayed(), 'Element is not displayed!'
                assert project.is_enabled(), 'Element is not enabled!'
                project.click()


                Key_text = WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/input'))
                )
                assert Key_text.is_displayed(), 'Element is not displayed!'
                assert Key_text.is_enabled(), 'Element is not enabled!'
                Key_text.send_keys('อาคาร C6' + Keys.ARROW_DOWN + Keys.ENTER)

                # คลิกปีที่ปีประชุม 2567

                click_date = WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div'))
                )
                print('Show Element date', True)


                click_date = WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div'))
                )
                assert click_date.is_displayed(), 'Element is not displayed!'
                assert click_date.is_enabled(), 'Element is not enabled!'
                click_date.click()

                click_date = WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[5]'))
                )
                assert click_date.is_displayed(), 'Element is not displayed!'
                assert click_date.is_enabled(), 'Element is not enabled!'
                click_date.click()

                # คลิกค้นหา      

                click_search = WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div/div[2]/div/div'))
                )
                assert click_search.is_displayed(), 'Element is not displayed!'
                assert click_search.is_enabled(), 'Element is not enabled!'
                click_search.click()

                # กรอกชื่อการประชุม ประชุมใหญ่สามัญเจ้าของร่วมประจำปี

                Key_text = WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[3]/div/div[2]/div/div/input'))
                )
                assert Key_text.is_displayed(), 'Element is not displayed!'
                assert Key_text.is_enabled(), 'Element is not enabled!'
                Key_text.send_keys('ประชุมใหญ่สามัญเจ้าของร่วมประจำปี')


                # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[2]/div/div/div/table/tbody/tr[1]/td[1]/p"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
                )
                # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
                print("Element is visible. Proceeding with the next step.")

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
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\5.การประชุมลูกบ้าน\\Reports'))