
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import pyautogui

def page_edit_banner_call_to_action_v1(driver):

        try:
            # หน้า ข่าวสาร
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/banner')
            assert driver.current_url == ('https://msm-smarty-cms-staging.hr-impact.co/banner')
            driver.implicitly_wait(10)

            Edit_Banner = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[7]/button[1]'))
            )
            assert Edit_Banner.is_displayed(), 'Element is not displayed!'
            assert Edit_Banner.is_enabled(), 'Element is not enabled!'
            Edit_Banner.click()

            if Edit_Banner:
                print('Click Edit Banner Already :',(True))
            else:
                print('Cannot Click Edit Banner :',(False))
                
            # กรอกข้อมูล
            # ชื่อแบนเนอร์

            Edit_name = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/input'))
            )
            assert Edit_name.is_displayed(), 'Element is not displayed!'
            assert Edit_name.is_enabled(), 'Element is not enabled!'
            Edit_name.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Edit_name.send_keys('Kub_New')     

            # เลือก รูปภาพ

            Delete_image = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[1]/div/div/div/button'))
            )
            assert Delete_image.is_displayed(), 'Element is not displayed!'
            assert Delete_image.is_enabled(), 'Element is not enabled!'
            Delete_image.click()

            if Delete_image:
                print('Click Delete image Already :',(True))
            else:
                print('Cannot Click Delete image :',(False))

            # อัพโหลดรูปภาพ Mac Os

            upload = driver.find_element(by=By.XPATH , value='/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[1]/div/div/div/input')
            upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')

            if upload:
                print('Upload image Already :',(True))
            else:
                print('Cannot Upload image :',(False))

            # date วันที่ วันที่เผยแพร่

            Data = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[3]/div[2]/div/div'))
            )
            assert Data.is_displayed(), 'Element is not displayed!'
            assert Data.is_enabled(), 'Element is not enabled!'
            Data.click()

            if Data:
                print('Click Date Already :',(True))
            else:
                print('Cannot Click date :',(False))

            time.sleep(0.5)
            if pyautogui:
                pyautogui.click(x=781, y=737)
                print('Click select date 29 :',True)
            else:
                print('Cannot date',False)

            # Select_Date = WebDriverWait(driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '//div/div/div[2]/div/div[5]/button[2]'))
            # )
            # assert Select_Date.is_displayed(), 'Element is not displayed!'
            # assert Select_Date.is_enabled(), 'Element is not enabled!'
            # Select_Date.click()

            # if Select_Date:
            #     print('Click Select date Already :',(True))
            # else:
            #     print('Cannot Click select date :',(False))


            # ต้องการเพิ่มปุ่ม Call to Action?
            
            # Call_to_Action = WebDriverWait(driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '//div/div/div/form/div/div[2]/div/div/div[2]/div/label/span[1]'))
            # )
            # assert Call_to_Action.is_displayed(), 'Element is not displayed!'
            # assert Call_to_Action.is_enabled(), 'Element is not enabled!'
            # Call_to_Action.click()

            # ------------------------------------------------------------------------------------------------------------------------------------------
            # บริการในแอปพลิเคชันที่ต้องการพาผู้ใช้งานไป (DeepLink)

            # การเลือกแบบ Internal 

            External = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[2]/div/div/div/div[1]/div[2]/div/div/div'))
                )
            assert External.is_displayed(), 'Element is not displayed!'
            assert External.is_enabled(), 'Element is not enabled!'
            External.click() 

            if External:
                print('Click External Already :',(True))
            else:
                print('Cannot Click External :',(False))

            # Internal = WebDriverWait(driver, 30).until(
            #         EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div'))
            #     )
            # assert Internal.is_displayed(), 'Element is not displayed!'
            # assert Internal.is_enabled(), 'Element is not enabled!'
            # Internal.click()           

            # if Internal:
            #     print('Click Internal Already :',(True))
            # else:
            #     print('Cannot Click Internal :',(False))

            select_Internal = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
                )
            assert select_Internal.is_displayed(), 'Element is not displayed!'
            assert select_Internal.is_enabled(), 'Element is not enabled!'
            select_Internal.click()

            Internal_deeplink = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div'))
                )
            assert Internal_deeplink.is_displayed(), 'Element is not displayed!'
            assert Internal_deeplink.is_enabled(), 'Element is not enabled!'
            Internal_deeplink.click()
            
            Internal_3 = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[2]/div[3]/ul/li[1]'))
                )
            assert Internal_3.is_displayed(), 'Element is not displayed!'
            assert Internal_3.is_enabled(), 'Element is not enabled!'
            Internal_3.click()

            # ------------------------------------------------------------------------------------------------------------------------------------------

            # External = WebDriverWait(driver, 30).until(
            #         EC.element_to_be_clickable((By.XPATH, '//div[2]/div/div/div/div[1]/div[2]/div/div/div'))
            #     )
            # assert External.is_displayed(), 'Element is not displayed!'
            # assert External.is_enabled(), 'Element is not enabled!'
            # External.click()           

            # External_1 = WebDriverWait(driver, 30).until(
            #         EC.element_to_be_clickable((By.XPATH, '//div[2]/div[3]/ul/li[2]'))
            #     )
            # assert External_1.is_displayed(), 'Element is not displayed!'
            # assert External_1.is_enabled(), 'Element is not enabled!'
            # External_1.click()           

            # Url = WebDriverWait(driver, 30).until(
            #         EC.element_to_be_clickable((By.XPATH, 
            # '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/input'))
            #     )
            # assert Url.is_displayed(), 'Element is not displayed!'
            # assert Url.is_enabled(), 'Element is not enabled!'
            # Url.send_keys('https://msm-smarty-cms-staging.hr-impact.co/banner/51/edit')

            # ------------------------------------------------------------------------------------------------------------------------------------------

            Save = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[1]/div[2]/button[2]'))
                )
            assert Save.is_displayed(), 'Element is not displayed!'
            assert Save.is_enabled(), 'Element is not enabled!'
            Save.click()  

            if Save:
                print('Click Save Already :',(True))
            else:
                print('Cannot Click Save :',(False))

    # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[2]/div[1]/div/table/tbody/tr[1]/td[1]/p"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
    # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
            print('Element Show :',(True))

            time.sleep(5)

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
           
        






