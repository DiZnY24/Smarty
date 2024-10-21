
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
from selenium.common.exceptions import NoSuchElementException ,TimeoutException


def test_page_edit_room(driver):
        # หน้า การบริหาร - ผู้ใช้งาน
        driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/units')
        driver.implicitly_wait(10)

        try:
            # แก้ไข 

            edit = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[8]/div/button'))
            )
            assert edit.is_displayed(), 'Element is not displayed!'
            assert edit.is_enabled(), 'Element is not enabled!'
            edit.click()
            time.sleep(1)
            
            # บ้านเลขที่

            home_number = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[1]/div[1]/div/div[2]/div/div/input'))
            )
            assert home_number.is_displayed(), 'Element is not displayed!'
            assert home_number.is_enabled(), 'Element is not enabled!'
            home_number.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            home_number.send_keys('99/1') 
            time.sleep(0.1)

            # ชั้น

            floor = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[1]/div[2]/div/div[2]/div/div/input'))
            )
            assert floor.is_displayed(), 'Element is not displayed!'
            assert floor.is_enabled(), 'Element is not enabled!'
            floor.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            floor.send_keys('01/02') 
            time.sleep(0.1)

            # เลขที่ห้อง

            number_home = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[1]/div[3]/div/div[2]/div/div/input'))
            )
            assert number_home.is_displayed(), 'Element is not displayed!'
            assert number_home.is_enabled(), 'Element is not enabled!'
            number_home.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            number_home.send_keys('134/06') 
            time.sleep(0.1)

            # ประเภท

            type = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[1]/div[4]/div[2]/div/div/div'))
            )
            assert type.is_displayed(), 'Element is not displayed!'
            assert type.is_enabled(), 'Element is not enabled!'
            type.click() 
            time.sleep(0.1)

            type = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[3]'))
            )
            assert type.is_displayed(), 'Element is not displayed!'
            assert type.is_enabled(), 'Element is not enabled!'
            type.click() 
            time.sleep(0.1)
            
            # ขนาดห้อง (ตร.ม.)

            Room_size = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[2]/div[1]/div/div[2]/div/div/input'))
            )
            assert Room_size.is_displayed(), 'Element is not displayed!'
            assert Room_size.is_enabled(), 'Element is not enabled!'
            Room_size.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Room_size.send_keys('35.ม') 
            time.sleep(0.1)
            
            # อัตราส่วนแห่งกรรมสิทธิ์ในทรัพย์สินส่วนกลาง

            Buy = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[2]/div[2]/div/div[2]/div/div/input'))
            )
            assert Buy.is_displayed(), 'Element is not displayed!'
            assert Buy.is_enabled(), 'Element is not enabled!'
            Buy.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Buy.send_keys('0.700000') 
            time.sleep(0.1)

            # Ref1

            Ref1 = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[2]/div[3]/div/div[2]/div/div/input'))
            )
            assert Ref1.is_displayed(), 'Element is not displayed!'
            assert Ref1.is_enabled(), 'Element is not enabled!'
            Ref1.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Ref1.send_keys('500002') 
            time.sleep(0.1)

            # Ref2

            Ref1 = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[2]/div[4]/div/div[2]/div/div/input'))
            )
            assert Ref1.is_displayed(), 'Element is not displayed!'
            assert Ref1.is_enabled(), 'Element is not enabled!'
            Ref1.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Ref1.send_keys('0102') 
            time.sleep(0.1)


        # Save

            # Save = WebDriverWait(driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/form/div/div[3]/button'))
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click() 


        except NoSuchElementException:
            driver.fail('Element not Found')
        except AssertionError as e :
            driver.fail(str(e))
        except Exception as n:
            driver.fail(f'An unexpected error occurred:: {n}')
        
        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        try:
            # ที่อยู่จัดส่ง 

            address = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div[2]/div/button[2]'))
            )
            assert address.is_displayed(), 'Element is not displayed!'
            assert address.is_enabled(), 'Element is not enabled!'
            address.click() 
            time.sleep(0.5)

            # ประเภทที่อยู่จัดส่ง

            type_address = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[1]/div[2]/div/div/div'))
            )
            assert type_address.is_displayed(), 'Element is not displayed!'
            assert type_address.is_enabled(), 'Element is not enabled!'
            type_address.click() 
            time.sleep(0.1)

            type_address = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[2]'))
            )
            assert type_address.is_displayed(), 'Element is not displayed!'
            assert type_address.is_enabled(), 'Element is not enabled!'
            type_address.click() 
            time.sleep(0.1)
            
            # รายละเอียดที่อยู่

            Address_details = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[2]/div/div/input'))
                )
            assert Address_details.is_displayed(), 'Element is not displayed!'
            assert Address_details.is_enabled(), 'Element is not enabled!'
            Address_details.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Address_details.send_keys('5/0012')
            time.sleep(0.1)

            # ซอย

            road = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[3]/div[1]/div/div[2]/div/div/input'))
                )
            assert road.is_displayed(), 'Element is not displayed!'
            assert road.is_enabled(), 'Element is not enabled!'
            road.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            road.send_keys('-')
            time.sleep(0.1)

            # เลขที่ห้อง

            number_room = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[3]/div[2]/div/div[2]/div/div/input'))
                )
            assert number_room.is_displayed(), 'Element is not displayed!'
            assert number_room.is_enabled(), 'Element is not enabled!'
            number_room.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            number_room.send_keys('ถนนป๊อปปูล่า')
            time.sleep(0.1)
            
            # ตำบล

            district = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[4]/div[1]/div/div[2]/div/div/input'))
                )
            assert district.is_displayed(), 'Element is not displayed!'
            assert district.is_enabled(), 'Element is not enabled!'
            district.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            district.send_keys('บ้านใหม่')
            time.sleep(0.1)
            
            # อำเภอ

            district = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[4]/div[2]/div/div[2]/div/div/input'))
                )
            assert district.is_displayed(), 'Element is not displayed!'
            assert district.is_enabled(), 'Element is not enabled!'
            district.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            district.send_keys('ปากเกร็ด')
            time.sleep(0.1)

            # จังหวัด

            province = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[5]/div[1]/div/div[2]/div/div/input'))
                )
            assert province.is_displayed(), 'Element is not displayed!'
            assert province.is_enabled(), 'Element is not enabled!'
            province.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            province.send_keys('นนทบุรี')
            time.sleep(0.1)

            # รหัสไปรษณีย์

            province = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/div[5]/div[2]/div/div[2]/div/div/input'))
                )
            assert province.is_displayed(), 'Element is not displayed!'
            assert province.is_enabled(), 'Element is not enabled!'
            province.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            province.send_keys('11120')
            time.sleep(0.1)

            # Save

            # Save = WebDriverWait(driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/form/div/button'))
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click() 

    
        except NoSuchElementException:
            driver.fail('Element not Found')
        except AssertionError as e:
            driver.fail(str(e))
        except Exception as o:
            driver.fail(f'An unexpected error occurred: {o}')

    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        try:
            # ชื่อออกเอกสาร 
            Name_of_document = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div[2]/div/button[3]'))
            )
            assert Name_of_document.is_displayed(), 'Element is not displayed!'
            assert Name_of_document.is_enabled(), 'Element is not enabled!'
            Name_of_document.click()
            time.sleep(0.5)
            
            # ชื่อ

            province = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[3]/div/form/div/div/div/div/div[1]/div/div/div/div/input'))
                )
            assert province.is_displayed(), 'Element is not displayed!'
            assert province.is_enabled(), 'Element is not enabled!'
            province.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            province.send_keys('นางสาวศิริพร,นางสุณี-')
            time.sleep(0.1)

            # Save
            
            # Save = WebDriverWait(driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[3]/div/form/div/div/div/div/div[2]/button'))
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click() 



        except NoSuchElementException:
            driver.fail('Element not Found')
        except AssertionError as e:
            driver.fail(str(e))
        except Exception as o:
            driver.fail(f'An unexpected error occurred: {o}')   
          

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



