
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
from selenium.common.exceptions import NoSuchElementException 
from  selenium.common.exceptions import NoSuchElementException,TimeoutException



def test_page_add_user(driver):
                
        try:
        # หน้า การบริหาร - ผู้ใช้งาน
                driver.get('https://msm-smarty-cms-staging.hr-impact.co/admin')
                driver.implicitly_wait(20)


        #เพิ่มผู้ใช้งาน    
                click_add = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div[2]/div[1]/div[1]/button'))
                )
                assert click_add.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert click_add.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                click_add.click()
                time.sleep(1) 

                element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[3]/div/div[1]/div/div[2]/div[1]/h6")) 
                )
                print("Element is visible. Proceeding with the next step.")
                time.sleep(1)

        # เลือกผู้ใช้งาน

                select_username = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div/div')
                select_username.click()
                time.sleep(0.1)

                wait = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div/div/input'))
                )
                print(True)

                input('รอจนกว่ารายชื่อจะปรากฏ ENTER')

                key_name = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div/div/input'))
                )
                key_name.send_keys("Karis Matchaparn (อิม)" + Keys.ARROW_DOWN)
                key_name.send_keys(Keys.ENTER)
                time.sleep(1)

                # บทบาท 

                Role = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[2]/div/div/div'))
                )
                assert Role.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert Role.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                Role.click()
                time.sleep(1.5) 

                # element = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[2]/div/div/div')
                # actions = ActionChains(driver)
                # assertTrue(element.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า")
                # assertTrue(element.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
                # actions.move_to_element(element).click().perform()
                # time.sleep(0.1)

                # button = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[2]/div/div/div')
                # assertTrue(button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า")
                # assertTrue(button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
                # button.click()
                # time.sleep(0.1)

                Role = driver.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[1]')
                assert Role.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                assert Role.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                Role.click()
                time.sleep(0.5)

        # จัดการเลือกโครงการ 

                button = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[4]/div[2]/div/div/div')
                assert button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                assert button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                button.click()
                time.sleep(1.5)

                button1 = driver.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[1]')
                assert button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                assert button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                button1.click()
                time.sleep(0.5)


                element_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/button")

                driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
                time.sleep(1)

        # Save

                # Save = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/button') 
                # Save.click()

        # Refresh

                # try:
                #         element = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div/div[3]/button")
                #         assert element.is_displayed(), "Element is not visible"  
                #         assertTrue(element.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
                #         assertTrue(element.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
                #         element.click()
                # except NoSuchElementException:
                #         print("Element not found")
                #         time.sleep(0.1)


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



