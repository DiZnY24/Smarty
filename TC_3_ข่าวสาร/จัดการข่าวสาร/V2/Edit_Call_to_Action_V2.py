
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

def page_edit_call_to_action_v1(driver):

# Click เข้าแก้ไข

        try:
            # หน้า ข่าวสาร
            driver.get('https://msm-smarty-cms-staging.hr-impact.co/announcement')
            driver.implicitly_wait(20)

             # Click เข้าแก้ไข 

            Edit_News = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[9]/button[1]'))
            )
            assert Edit_News.is_displayed(), 'Element is not displayed!'
            assert Edit_News.is_enabled(), 'Element is not enabled!'        
            Edit_News.click()    

            if Edit_News:
                print('Click Edit News :',(True))
            else:
                print('Cannot Click Edit News :',(False))        

            # กรอกข้อมูล
            # ชื่อข่าวสาร

            Add_name = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/input'))
            )
            assert Add_name.is_displayed(), 'Element is not displayed!'
            assert Add_name.is_enabled(), 'Element is not enabled!'        
            Add_name.send_keys(Keys.COMMAND + "a" + Keys.DELETE)
            Add_name.send_keys('Test_Nwes') 

            # คลิกลบรูป

            Delete_image = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[1]/div/div/button'))
            )
            assert Delete_image.is_displayed(), 'Element is not displayed!'
            assert Delete_image.is_enabled(), 'Element is not enabled!'        
            Delete_image.click() 

            if Delete_image:
                print('Click Delete Image :',(True))
            else:
                print('Cannot Click Delete Image :',(False)) 

            # # คลิกเพิ่มรูปใหม่

            upload = driver.find_element(by=By.XPATH , value='/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[1]/div/div/input')
            upload.send_keys('/Users/dizny/Downloads/Image/image Test/Logo.jpg.jpg')

            # วันที่เผยแพร่

            select_date = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[3]/div[2]/div/div'))
            )
            assert select_date.is_displayed(), 'Element is not displayed!'
            assert select_date.is_enabled(), 'Element is not enabled!'        
            select_date.click()  

            # # เลือกวันที่ ....                 

            time.sleep(0.5)
            if pyautogui:
                pyautogui.click(x=781, y=737)
                print('Click select date 29 :',True)
            else:
                print('Cannot date',False)

            # select_date = WebDriverWait(driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, '//div/div[2]/div/div/div[2]/div/div[5]/button[2]'))
            # )
            # assert select_date.is_displayed(), 'Element is not displayed!'
            # assert select_date.is_enabled(), 'Element is not enabled!'        
            # select_date.click()          

            # รายละเอียดข่าวสาร

            Edit_key = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/div'))
            )
            assert Edit_key.is_displayed(), 'Element is not displayed!'
            assert Edit_key.is_enabled(), 'Element is not enabled!'        
            Edit_key.click()    

            # แก้ไข รายละเอียด

            # ค้นหา element ที่ต้องการให้มองเห็น
            element_2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/div")

            # ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
            driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
            time.sleep(1)

            wait_add_text = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '//div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div'))
            )
            print('Key Text :',(True))

            Add_Text = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div'))
            )
            assert Add_Text.is_displayed(), 'Element is not displayed!'
            assert Add_Text.is_enabled(), 'Element is not enabled!'        
            Add_Text.click()

            Add_Text = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div'))
            )
            assert Add_Text.is_displayed(), 'Element is not displayed!'
            assert Add_Text.is_enabled(), 'Element is not enabled!'        
            Add_Text.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Add_Text.send_keys('Someone')

            Check_messages = driver.find_element(By.XPATH, '//div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div')
            expected_text = 'Someone'
            assert Check_messages.text == expected_text, f"ข้อความไม่ตรงกัน: คาดว่า '{expected_text}' แต่ได้ '{Check_messages.text}'"
            time.sleep(0.5)
            
    # --------------------------------------------------------------------------------------------------------------------------------

            # ตอนเทสต้องมาเปลี่ยน เปิด-ปิด ต้องการเพิ่มปุ่ม Call to Action?
            # เพิ่มปุ่ม Call to Action?

            # add_Call_to_Action = WebDriverWait(driver, 30).until(
            #         EC.element_to_be_clickable((By.XPATH, 
            #     '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[3]/label/span[1]'))
            # )
            # assert add_Call_to_Action.is_displayed(), 'Element is not displayed!'
            # assert add_Call_to_Action.is_enabled(), 'Element is not enabled!'
            # add_Call_to_Action.click()

            # if add_Call_to_Action:
            #     print('Click Open Call to Action :',(True))
            # else:
            #     print('Cannot Click pen Call to Action :',(False))

            # ชื่อปุ่ม Call to Action
            #  Key name in Call to Action?

            Key_name = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div/div/input'))
            )
            assert Key_name.is_displayed(), 'Element is not displayed!'
            assert Key_name.is_enabled(), 'Element is not enabled!'
            Key_name.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Key_name.send_keys('Some555')  

            if Key_name:
                print('Key :',(True))
            else:
                print('Cannot Key :',(False))
# --------------------------------------------------------------------------------------------------------------------------------

            # ต้องการพาผู้ใช้งานไปยัง
            # Internal (Deeplink) เปลี่ยนเป็น External (URL)

            Internal = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div/div/div'))
            )
            assert Internal.is_displayed(), 'Element is not displayed!'
            assert Internal.is_enabled(), 'Element is not enabled!'
            Internal.click()

            wait_element = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "//div[3]/div[3]/ul/li[2]"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
            print("Wait select show : Pass ")

            Select_Internal = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, 
            '//div[3]/div[3]/ul/li[1]'))
            )
            assert Select_Internal.is_displayed(), 'Element is not displayed!'
            assert Select_Internal.is_enabled(), 'Element is not enabled!'
            Select_Internal.click()

            Internal = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div'))
            )
            assert Internal.is_displayed(), 'Element is not displayed!'
            assert Internal.is_enabled(), 'Element is not enabled!'
            Internal.click()

            # บริการในแอปพลิเคชันที่ต้องการพาผู้ใช้งานไป (DeepLink)

            Click_Internal = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[3]/div[3]/ul/li[1]'))
            )
            assert Click_Internal.is_displayed(), 'Element is not displayed!'
            assert Click_Internal.is_enabled(), 'Element is not enabled!'
            Click_Internal.click()

            # เลื่อนจอขึ้น
            driver.execute_script("window.scrollTo(0, -900)")

            # รูปแบบการเผยแพร่ 

            Click_Chack = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[3]/div[3]/div[2]/div/div/div'))
            )
            assert Click_Chack.is_displayed(), 'Element is not displayed!'
            assert Click_Chack.is_enabled(), 'Element is not enabled!'
            Click_Chack.click()

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
            element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[3]/ul/li[2]"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
            print("Wait Element Show : Pass")

            # กดเลือก ตามโครงการ

            Click_Select_Chack = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, 
            '//div[3]/ul/li[2]'))
            )
            assert Click_Select_Chack.is_displayed(), 'Element is not displayed!'
            assert Click_Select_Chack.is_enabled(), 'Element is not enabled!'
            Click_Select_Chack.click()

            # เลือกตึก หลังกด ตามโครงการ

            select_building = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[4]/div/div/div/div/input')) # คลิกขอ เข้าสู่ระบบ
            )
            assert select_building.is_displayed(), 'Element is not displayed!'
            assert select_building.is_enabled(), 'Element is not enabled!'
            select_building.click()  

            # พิมพ์ ตึกลง 
                
            Key_building = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div[4]/div/div/div/div/input')) 
            )
            assert Key_building.is_displayed(), 'Element is not displayed!'
            assert Key_building.is_enabled(), 'Element is not enabled!'
            Key_building.send_keys('C')
            Key_building.send_keys(Keys.ARROW_DOWN + Keys.ENTER + Keys.ESCAPE)  

            # Save

            Save = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '//div/div/div/form/div/div[1]/div/div[1]/div/button[2]'))
            )
            assert Save.is_displayed(), 'Element is not displayed!'
            assert Save.is_enabled(), 'Element is not enabled!'
            Save.click()

            if Save:
                print('Click Button Save :',(True))
            else:
                print('Not Click Button Save :',(False))

            wait_element = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, 
            '/html/body/div/div/main/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[1]'))
            )
            if wait_element:
                print('Edit Already :',(True))
            else:
                print('Cannot Edit :',(False))

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
        
        







