
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



def page_participants(driver):
        
        try:
            # เปิดหน้า จัดการประชุม

            driver.get('https://msm-smarty-cms-staging.hr-impact.co/agm/meetings')
            driver.implicitly_wait(30)
            

            Click_icon = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[8]/div/button[3]'))
            )
            assert Click_icon.is_displayed(), 'Element is not displayed!'
            assert Click_icon.is_enabled(), 'Element is not enabled!'
            Click_icon.click()


            Click_Edit = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div/div[1]/table/tbody/tr[1]/td[10]/button[1]'))
            )
            assert Click_Edit.is_displayed(), 'Element is not displayed!'
            assert Click_Edit.is_enabled(), 'Element is not enabled!'
            Click_Edit.click()

            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 

    # ข้อมูลห้องชุด
            
            Click_room = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/div/input'))
            )
            assert Click_room.is_displayed(), 'Element is not displayed!'
            assert Click_room.is_enabled(), 'Element is not enabled!'
            Click_room.send_keys('01/03' + Keys.ARROW_DOWN + Keys.ENTER)


            Click_room = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div/div[2]/div/div/input'))
            )
            assert Click_room.is_displayed(), 'Element is not displayed!'
            assert Click_room.is_enabled(), 'Element is not enabled!'
            Click_room.send_keys('01/04' + Keys.ARROW_DOWN + Keys.ENTER)



    # ลบห้อง

            time.sleep(2)

            delete = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/button'))
            )
            assert delete.is_displayed(), 'Element is not displayed!'
            assert delete.is_enabled(), 'Element is not enabled!'
            delete.click()

            delete = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/button'))
            )
            assert delete.is_displayed(), 'Element is not displayed!'
            assert delete.is_enabled(), 'Element is not enabled!'
            delete.click()
            
            delete = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/button'))
            )
            assert delete.is_displayed(), 'Element is not displayed!'
            assert delete.is_enabled(), 'Element is not enabled!'
            delete.click()

    # ลงทะเบียน 
        
            # Save = WebDriverWait(driver, 30).until(
            #         EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div[2]/button'))
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click()
        
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