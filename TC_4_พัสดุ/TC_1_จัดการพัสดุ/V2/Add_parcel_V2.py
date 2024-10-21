
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import pyautogui


def page_parcel(driver):

        try: 
            # หน้า ข่าวสาร
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/parcels')
            driver.implicitly_wait(30)

            # กดปุ่มเพิ่มพัสดุ

            Add_parcel = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div/div[1]/button'))
            )
            assert Add_parcel.is_displayed(), 'Element is not displayed!'
            assert Add_parcel.is_enabled(), 'Element is not enabeld!'
            Add_parcel.click()

            # กรอกข้อมูล
            # อัพโหลดรูปภาพ Mac Os

            upload = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div[3]/div/div/div'))
            )
            print('Wait Show Element Upload Image :', True)

            upload = driver.find_element(by=By.XPATH , value='/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div[3]/div/div/input')
            upload.send_keys('/Users/dizny/Downloads/Image/image Test/Logo.jpg.jpg')

            # คลิกโครงการ

            Add_project = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div[4]/div[1]/div/div/div/div/div[2]/div/div/input'))
            )
            assert Add_project.is_displayed(), 'Element is not displayed!'
            assert Add_project.is_enabled(), 'Element is not enabeld!'
            Add_project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)     

            # คลิกชั้น / ห้อง

            room_floor = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div[4]/div[2]/div/div/div/div/div[2]/div/div')) 
            )
            assert room_floor.is_displayed(), 'Element is not displayed!'
            assert room_floor.is_enabled(), 'Element is not enabeld!'
            room_floor.click()    

            # พิมพ์ ชั้น / ห้อง

            room_floor = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div[4]/div[2]/div/div/div/div/div[2]/div/div/input')) 
            )
            assert room_floor.is_displayed(), 'Element is not displayed!'
            assert room_floor.is_enabled(), 'Element is not enabeld!'
            room_floor.send_keys('01/02' + Keys.ARROW_DOWN + Keys.ENTER)     

        
            # เลือก_ชื่อลูกบ้านที่ต้องการแจ้งเตือน

            time.sleep(3)
            # pyautogui.click(x=612, y=925)

            select = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div/div/div/form/div[2]/div[1]/div[1]/div/div[2]/div/div')) 
            )
            assert select.is_displayed(), 'Element is not displayed!'
            assert select.is_enabled(), 'Element is not enabeld!'
            select.click()   

            time.sleep(0.5)
            select = driver.find_element(by=By.XPATH, value='/html/body/div/div/main/div/div/div/div/form/div[2]/div[1]/div[1]/div/div[2]/div/div/div')
            
            select = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li')) 
            )
            assert select.is_displayed(), 'Element is not displayed!'
            assert select.is_enabled(), 'Element is not enabeld!'
            select.click()    
            select.send_keys(Keys.ESCAPE)

            # Key หมายเลขพัสดุ

            Key_number = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[2]/div[1]/div[2]/div/div/div[2]/div/div/input')) 
            )
            assert Key_number.is_displayed(), 'Element is not displayed!'
            assert Key_number.is_enabled(), 'Element is not enabeld!'
            Key_number.send_keys('16161616')     
        
            # # บริษัทขนส่ง

            Key_date = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[2]/div[1]/div[3]/div/div[2]/div/div/div')) 
            )
            assert Key_date.is_displayed(), 'Element is not displayed!'
            assert Key_date.is_enabled(), 'Element is not enabeld!'
            Key_date.click()    

            Key_date = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')) 
            )
            assert Key_date.is_displayed(), 'Element is not displayed!'
            assert Key_date.is_enabled(), 'Element is not enabeld!'
            Key_date.click()    

            # สถานะ

            status = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[2]/div[1]/div[4]/div/div[2]/div/div/div')) 
            )
            assert status.is_displayed(), 'Element is not displayed!'
            assert status.is_enabled(), 'Element is not enabeld!'
            status.click()    

            status = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[3]')) 
            )
            assert status.is_displayed(), 'Element is not displayed!'
            assert status.is_enabled(), 'Element is not enabeld!'
            status.click()    

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            
            # Save = WebDriverWait(driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[2]/div[2]/button')) 
            # )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabeld!'

            # if Save:
            #     Save.click()    
            #     print('Save Already',True)
            # else:
            #     print('Cannot Save Already', False)
            
            # Show_Save = WebDriverWait(driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]')) 
            # )
            # print('Element Show Save Already :',True)


        except NoSuchElementException:
            driver.fail('Element not Found',False)
        except AssertionError as e:
            driver.fail(str(e))
        except Exception as o:
            driver.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            driver.fail('การรอองค์ประกอบล้มเหลว',False)


if __name__ == '__main__':
    unittest.main()


# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\4.พัสดุ\\Reports'))