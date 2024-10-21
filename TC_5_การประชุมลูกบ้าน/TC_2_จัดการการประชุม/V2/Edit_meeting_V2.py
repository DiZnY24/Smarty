
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys 
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException,TimeoutException


def page_edit_meeting(driver):
        
        try:
            # เปิดหน้า จัดการประชุม
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/agm/meetings')
            driver.implicitly_wait(30)

            # คลิกปุ่ม Edit

            click_edit = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div/table/tbody/tr/td[8]/div/button[1]'))
            )
            assert click_edit.is_displayed(), 'Element is not displayed!'
            assert click_edit.is_enabled(), 'Element is not enabled!'
            click_edit.click()

            # โครงการ

            project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div'))
            )
            assert project.is_displayed(), 'Element is not displayed!'
            assert project.is_enabled(), 'Element is not enabled!'
            project.click()


            key_text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/input'))
            )
            assert key_text.is_displayed(), 'Element is not displayed!'
            assert key_text.is_enabled(), 'Element is not enabled!'
            key_text.send_keys(Keys.COMMAND + 'a')
            key_text.send_keys(Keys.DELETE)
            key_text.send_keys('อาคาร C6' + Keys.ARROW_DOWN + Keys.ENTER)

            # # ปีที่ประชุม 

            click_year = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div'))
            )
            assert click_year.is_displayed(), 'Element is not displayed!'
            assert click_year.is_enabled(), 'Element is not enabled!'
            click_year.click()

            key_text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/input'))
            )
            assert key_text.is_displayed(), 'Element is not displayed!'
            assert key_text.is_enabled(), 'Element is not enabled!'
            key_text.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            key_text.send_keys('2572' + Keys.ARROW_DOWN + Keys.ENTER) 

            # # ชื่อการประชุม

            click_year = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[3]/div/div/div/div[2]/div/div'))
            )
            assert click_year.is_displayed(), 'Element is not displayed!'
            assert click_year.is_enabled(), 'Element is not enabled!'
            click_year.click()

            key_text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[3]/div/div/div/div[2]/div/div/input'))
            )
            assert key_text.is_displayed(), 'Element is not displayed!'
            assert key_text.is_enabled(), 'Element is not enabled!'
            key_text.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            key_text.send_keys('ประชุมใหญ่สามัญเจ้าของร่วมประจำปี' + Keys.ARROW_DOWN + Keys.ENTER) 

            # # ครั้งที่

            click = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[3]/div[1]/div/div[2]/div/div'))
            )
            assert click.is_displayed(), 'Element is not displayed!'
            assert click.is_enabled(), 'Element is not enabled!'
            click.click()

            key_num = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div/form/div/div[1]/div[3]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_num.is_displayed(), 'Element is not displayed!'
            assert key_num.is_enabled(), 'Element is not enabled!'
            key_num.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            key_num.send_keys('2') 



    # วันและเวลาที่จัดประชุม

            Click_Date = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[3]/div[2]/div/div/div/button'))
            )
            assert Click_Date.is_displayed(), 'Element is not displayed!'
            assert Click_Date.is_enabled(), 'Element is not enabled!'
            Click_Date.click()

            select_Date = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div[5]/button[4]'))
            )
            assert select_Date.is_displayed(), 'Element is not displayed!'
            assert select_Date.is_enabled(), 'Element is not enabled!'
            select_Date.click()        
    
            # เลื่อนหน้าจอไปยังองค์ประกอบ

            select_Time = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[2]/ul[1]'))
            )
            assert select_Time.is_displayed(), 'Element is not displayed!'
            assert select_Time.is_enabled(), 'Element is not enabled!'
            actions = ActionChains(driver)
            actions.move_to_element(select_Time).click().perform()        

            select_Time = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[2]/ul[1]/li[5]'))
            )
            assert select_Time.is_displayed(), 'Element is not displayed!'
            assert select_Time.is_enabled(), 'Element is not enabled!'
            actions = ActionChains(driver)
            actions.move_to_element(select_Time).click().perform()        

            time.sleep(0.5)

            select_Time = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[2]/ul[2]'))
            )
            assert select_Time.is_displayed(), 'Element is not displayed!'
            assert select_Time.is_enabled(), 'Element is not enabled!'
            actions = ActionChains(driver)
            actions.move_to_element(select_Time).click().perform()        


            select_Time = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[2]/ul[2]/li[3]'))
            )
            assert select_Time.is_displayed(), 'Element is not displayed!'
            assert select_Time.is_enabled(), 'Element is not enabled!'
            actions = ActionChains(driver)
            actions.move_to_element(select_Time).click().perform()        

            # สถานที่ประชุม 

            send_key = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[3]/div[3]/div/div[2]/div/div/input'))
            )
            assert send_key.is_displayed(), 'Element is not displayed!'
            assert send_key.is_enabled(), 'Element is not enabled!'
            send_key.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            send_key.send_keys('MSM Smarty')


    # วาระที่ / ระเบียบวาระการประชุม / รูปแบบวาระ

        # แก้ไข วาระ 1

            # ครั้งที่ 10 

            send_key = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr/td[1]/div/div/div/div/div/input'))
            )
            assert send_key.is_displayed(), 'Element is not displayed!'
            assert send_key.is_enabled(), 'Element is not enabled!'
            send_key.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            send_key.send_keys('10')

            # กรอก ระเบียบวาระการประชุม

            send_key = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[1]/td[2]/div/div[1]/div/div/div/div/input'))
            )
            assert send_key.is_displayed(), 'Element is not displayed!'
            assert send_key.is_enabled(), 'Element is not enabled!'
            send_key.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            send_key.send_keys('Test')

            # คลิกรูปแบบวาระ

            click = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[1]/td[3]/div/div/div/div/div/div'))
            )
            assert click.is_displayed(), 'Element is not displayed!'
            assert click.is_enabled(), 'Element is not enabled!'
            click.click()

            # รูปแบบวาระ

            click = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]'))
            )
            assert click.is_displayed(), 'Element is not displayed!'
            assert click.is_enabled(), 'Element is not enabled!'
            click.click()

        # แก้ไข วาระ 2

            send_key = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/div/div/div/input'))
            )
            assert send_key.is_displayed(), 'Element is not displayed!'
            assert send_key.is_enabled(), 'Element is not enabled!'
            send_key.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            send_key.send_keys('11')

            # กรอก ระเบียบวาระการประชุม

            send_key = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[2]/td[2]/div/div[1]/div/div/div/div/input'))
            )
            assert send_key.is_displayed(), 'Element is not displayed!'
            assert send_key.is_enabled(), 'Element is not enabled!'
            send_key.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            send_key.send_keys('Test2')

            # คลิกรูปแบบวาระ

            click = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[2]/td[3]/div/div/div/div/div'))
            )
            assert click.is_displayed(), 'Element is not displayed!'
            assert click.is_enabled(), 'Element is not enabled!'
            click.click()

            # รูปแบบวาระ

            click = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[6]'))
            )
            assert click.is_displayed(), 'Element is not displayed!'
            assert click.is_enabled(), 'Element is not enabled!'
            click.click()


            key_num = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[2]/td[2]/div/div[2]/div/div/div/div/div/div/div/input'))
            )
            assert key_num.is_displayed(), 'Element is not displayed!'
            assert key_num.is_enabled(), 'Element is not enabled!'
            key_num.send_keys('5')

    # Save 
            # Click_Add = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[1]/button')
            # Click_Add.click()  # รูปแบบวาระ


    # ลบวาระทั้งหมด

            Click_Detele = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div/div/table/tbody/tr[7]/td[3]/div/button'))
            )
            assert Click_Detele.is_displayed(), 'Element is not displayed!'
            assert Click_Detele.is_enabled(), 'Element is not enabled!'
            Click_Detele.click()

            if Click_Detele:
                print('Click Delete Already :', True)
            else:
                print('Cannot Click Delete :', False)

            Click_Detele = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div/div/table/tbody/tr[4]/td[3]/div/button'))
            )
            assert Click_Detele.is_displayed(), 'Element is not displayed!'
            assert Click_Detele.is_enabled(), 'Element is not enabled!'
            Click_Detele.click()

            if Click_Detele:
                print('Click Delete Already :', True)
            else:
                print('Cannot Click Delete :', False)

            Click_Detele = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div/table/tbody/tr[6]/td[3]/div/button'))
            )
            assert Click_Detele.is_displayed(), 'Element is not displayed!'
            assert Click_Detele.is_enabled(), 'Element is not enabled!'
            Click_Detele.click()
            
            if Click_Detele:
                print('Click Delete Already :', True)
            else:
                print('Cannot Click Delete :', False)


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