
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import pyautogui
import time

def add_banner_call_to_action_v2(driver):    

        try:
            # หน้า ข่าวสาร
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/banner')
            driver.implicitly_wait(30)
            

            Add_Banner = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[1]/div/main/div/div/div/div/div[1]/div/div/button'))
            )
            assert Add_Banner.is_displayed(), 'Element is not displayed!'
            assert Add_Banner.is_enabled(), 'Element is not enabled!'
            Add_Banner.click()   

            # ชื่อแบนเนอร์

            Add_name = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/input'))
                )
            assert Add_name.is_displayed(), 'Element is not displayed!'
            assert Add_name.is_enabled(), 'Element is not enabled!'
            Add_name.send_keys('Tester_Kub')         

            # อัพโหลดรูปภาพ Mac Os

            upload = driver.find_element(by=By.XPATH , value='/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[1]/div/div/div/input')
            upload.send_keys('/Users/dizny/Downloads/Image/image Test/Logo.jpg.jpg')

            # date วันที่ วันที่เผยแพร่

            date = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[3]/div[2]/div/div'))
                )
            assert date.is_displayed(), 'Element is not displayed!'
            assert date.is_enabled(), 'Element is not enabled!'
            date.click() 

            time.sleep(0.5)
            if pyautogui:
                pyautogui.click(x=781, y=737)
                print('Click select date 29 :',True)
            else:
                print('Cannot date',False)

            # select_date = WebDriverWait(driver, 30).until(
            #         EC.element_to_be_clickable((By.XPATH, '//div/div/div[2]/div/div[5]/button[2]'))
            #     )
            # assert select_date.is_displayed(), 'Element is not displayed!'
            # assert select_date.is_enabled(), 'Element is not enabled!'
            # select_date.click()   

            # ต้องการเพิ่มปุ่ม Call to Action?

            Call_to_Action = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/form/div/div[2]/div/div/div[2]/div/label/span[1]'))
                )
            assert Call_to_Action.is_displayed(), 'Element is not displayed!'
            assert Call_to_Action.is_enabled(), 'Element is not enabled!'
            Call_to_Action.click()   

            # ------------------------------------------------------------------------------------------------------------------------------------------

            # บริการในแอปพลิเคชันที่ต้องการพาผู้ใช้งานไป (DeepLink)

            # Internal = WebDriverWait(driver, 30).until(
            #         EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div'))
            #     )
            # assert Internal.is_displayed(), 'Element is not displayed!'
            # assert Internal.is_enabled(), 'Element is not enabled!'
            # Internal.click()           

            # Internal_1 = WebDriverWait(driver, 30).until(
            #         EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[3]'))
            #     )
            # assert Internal_1.is_displayed(), 'Element is not displayed!'
            # assert Internal_1.is_enabled(), 'Element is not enabled!'
            # Internal_1.click()           
            
            # ------------------------------------------------------------------------------------------------------------------------------------------

            External = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[2]/div/div/div/div[1]/div[2]/div/div/div'))
                )
            assert External.is_displayed(), 'Element is not displayed!'
            assert External.is_enabled(), 'Element is not enabled!'
            External.click()           

            External_1 = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[2]/div[3]/ul/li[2]'))
                )
            assert External_1.is_displayed(), 'Element is not displayed!'
            assert External_1.is_enabled(), 'Element is not enabled!'
            External_1.click()           

            Url = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/input'))
                )
            assert Url.is_displayed(), 'Element is not displayed!'
            assert Url.is_enabled(), 'Element is not enabled!'
            Url.send_keys('https://msm-smarty-cms-staging.hr-impact.co/banner/51/edit')

            # ------------------------------------------------------------------------------------------------------------------------------------------

            Save = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[1]/div[2]/button[2]'))
                )
            assert Save.is_displayed(), 'Element is not displayed!'
            assert Save.is_enabled(), 'Element is not enabled!'
            Save.click()  

    # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[2]/div[1]/div/table/tbody/tr[1]/td[1]/p"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
    # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
            print('Element Show :',(True))

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
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\3.ข่าวสาร\\Reports'))
           






