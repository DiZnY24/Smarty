
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
import pyautogui

def page_meeting(driver):

    try:
# เปิดหน้า จัดการประชุม
        driver.get('https://msm-smarty-cms-staging.hr-impact.co/agm/meetings')
        driver.implicitly_wait(30)

        # คลิกเพิ่มการประชุม

        Click = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/button'))
        )
        assert Click.is_displayed(), 'Element is not displayed!'
        assert Click.is_enabled(), 'Element is not enabled!'
        Click.click()

        if Click:
            print('Click Add Already :', True)
        else:
            print('Cannot Add Delete :', False)

        # คลิกโครงการเพื่อพิม

        Click = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/input'))
        )
        assert Click.is_displayed(), 'Element is not displayed!'
        assert Click.is_enabled(), 'Element is not enabled!'
        Click.click()

        # กรอกชื่อโครงการ อาคาร C1

        Key_Text = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/input'))
        )
        assert Key_Text.is_displayed(), 'Element is not displayed!'
        assert Key_Text.is_enabled(), 'Element is not enabled!'
        Key_Text.send_keys('อาคาร C1' + Keys.ARROW_DOWN + Keys.ENTER)

        if Key_Text:
            print('Key Already :', True)
        else:
            print('Cannot Key Delete :', False)


        # คลิกประจำปี

        Click_year = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div'))
        )
        assert Click_year.is_displayed(), 'Element is not displayed!'
        assert Click_year.is_enabled(), 'Element is not enabled!'
        Click_year.click()

        if Click_year:
            print('Click Year Already :', True)
        else:
            print('Cannot Year Delete :', False)


        # กรอกประจำปี 2567

        Key_year = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/input'))
        )
        assert Key_year.is_displayed(), 'Element is not displayed!'
        assert Key_year.is_enabled(), 'Element is not enabled!'
        Key_year.send_keys('2024' + Keys.ARROW_DOWN + Keys.ENTER)

        if Key_year:
            print('Key year Already :', True)
        else:
            print('Cannot Key year :', False)

        # คลิกชื่อประชุม

        Click_Name = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[3]/div/div/div/div[2]/div/div'))
        )
        assert Click_Name.is_displayed(), 'Element is not displayed!'
        assert Click_Name.is_enabled(), 'Element is not enabled!'
        Click_Name.click()

        # กรอกชื่อการประชุม Test_Kub

        Key_Name = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[3]/div/div/div/div[2]/div/div/input'))
        )
        assert Key_Name.is_displayed(), 'Element is not displayed!'
        assert Key_Name.is_enabled(), 'Element is not enabled!'
        Key_Name.send_keys('Test_Kub')

        # กรอก ครั้งที่ 1 

        Key_num = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[3]/div[1]/div/div[2]/div/div/input'))
        )
        assert Key_num.is_displayed(), 'Element is not displayed!'
        assert Key_num.is_enabled(), 'Element is not enabled!'
        Key_num.send_keys('1') 

        # คลิก วันและเวลาที่จัดประชุม

        Click_Date = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div/form/div/div[1]/div[3]/div[2]/div/div/div/button'))
        )
        assert Click_Date.is_displayed(), 'Element is not displayed!'
        assert Click_Date.is_enabled(), 'Element is not enabled!'
        Click_Date.click()

        time.sleep(0.5)
        if pyautogui:
            pyautogui.click(x=641, y=926)
            print('Click select date 29 :',True)
        else:
            print('Cannot date',False)

        # select_Date = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div[2]/button[6]'))
        # )
        # assert select_Date.is_displayed(), 'Element is not displayed!'
        # assert select_Date.is_enabled(), 'Element is not enabled!'
        # select_Date.click()        

        # คลิกกรอบเวลา

        # Click_select_Date = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[2]/ul[1]/li[7]'))
        # )
        # assert Click_select_Date.is_displayed(), 'Element is not displayed!'
        # assert Click_select_Date.is_enabled(), 'Element is not enabled!'
        # Click_select_Date.click()        

        # เลื่อนหน้าจอไปยังองค์ประกอบ

        select_Time = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[2]/ul[1]'))
        )
        assert select_Time.is_displayed(), 'Element is not displayed!'
        assert select_Time.is_enabled(), 'Element is not enabled!'
        actions = ActionChains(driver)
        actions.move_to_element(select_Time).click().perform()        

        # element = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[2]/ul[1]')
        # actions = ActionChains(driver)
        # actions.move_to_element(element).click().perform()

        select_Time = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[2]/ul[1]'))
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
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[2]/ul[2]/li[9]'))
        )
        assert select_Time.is_displayed(), 'Element is not displayed!'
        assert select_Time.is_enabled(), 'Element is not enabled!'
        actions = ActionChains(driver)
        actions.move_to_element(select_Time).click().perform()        


        send_key = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[3]/div[3]/div/div[2]/div/div/input'))
        )
        assert send_key.is_displayed(), 'Element is not displayed!'
        assert send_key.is_enabled(), 'Element is not enabled!'
        send_key.send_keys('MSM Smarty')


        # วาระที่ / ระเบียบวาระการประชุม / รูปแบบวาระ

    # เพิ่มวาระ 1

        Click_Add_meeting = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//div/div/div/div/div/form/div/div[2]/div/button'))
        )
        assert Click_Add_meeting.is_displayed(), 'Element is not displayed!'
        assert Click_Add_meeting.is_enabled(), 'Element is not enabled!'
        Click_Add_meeting.click()

        # วาระที่ 1

        send_key = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr/td[1]/div/div/div/div/div/input'))
        )
        assert send_key.is_displayed(), 'Element is not displayed!'
        assert send_key.is_enabled(), 'Element is not enabled!'
        send_key.send_keys('1')
        
        # กรอก ระเบียบวาระการประชุม

        send_key = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr/td[2]/div/div[1]/div/div/div/div/input'))
        )
        assert send_key.is_displayed(), 'Element is not displayed!'
        assert send_key.is_enabled(), 'Element is not enabled!'
        send_key.send_keys('Test')
        
        # คลิกรูปแบบวาระ

        Click_Add = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr/td[3]/div/div/div/div/div/div'))
        )
        assert Click_Add.is_displayed(), 'Element is not displayed!'
        assert Click_Add.is_enabled(), 'Element is not enabled!'
        Click_Add.click()
        
        # รูปแบบวาระ

        Click_Add = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
        )
        assert Click_Add.is_displayed(), 'Element is not displayed!'
        assert Click_Add.is_enabled(), 'Element is not enabled!'
        Click_Add.click()

# --------------------------------------------------------------------------------------------
    # เพิ่มวาระ 2

        Click_Add_meeting = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/button'))
        )
        assert Click_Add_meeting.is_displayed(), 'Element is not displayed!'
        assert Click_Add_meeting.is_enabled(), 'Element is not enabled!'
        Click_Add_meeting.click()

        # วาระที่ 1

        send_key = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/div/div/div/input'))
        )
        assert send_key.is_displayed(), 'Element is not displayed!'
        assert send_key.is_enabled(), 'Element is not enabled!'
        send_key.send_keys('2')
        
        # กรอก ระเบียบวาระการประชุม

        send_key = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[2]/td[2]/div/div[1]/div/div/div/div/input'))
        )
        assert send_key.is_displayed(), 'Element is not displayed!'
        assert send_key.is_enabled(), 'Element is not enabled!'
        send_key.send_keys('Test2')
        
        # คลิกรูปแบบวาระ

        Click_Add = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[2]/td[3]/div/div/div/div/div/div'))
        )
        assert Click_Add.is_displayed(), 'Element is not displayed!'
        assert Click_Add.is_enabled(), 'Element is not enabled!'
        Click_Add.click()
        
        # รูปแบบวาระ

        Click_Add = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]'))
        )
        assert Click_Add.is_displayed(), 'Element is not displayed!'
        assert Click_Add.is_enabled(), 'Element is not enabled!'
        Click_Add.click()


# --------------------------------------------------------------------------------------------
    # เพิ่มวาระ 3 เพิ่มจำนวนคน

        Click_Add_meeting = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/button'))
        )
        assert Click_Add_meeting.is_displayed(), 'Element is not displayed!'
        assert Click_Add_meeting.is_enabled(), 'Element is not enabled!'
        Click_Add_meeting.click()

        # วาระที่ 1

        send_key = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[3]/td[1]/div/div/div/div/div/input'))
        )
        assert send_key.is_displayed(), 'Element is not displayed!'
        assert send_key.is_enabled(), 'Element is not enabled!'
        send_key.send_keys('3')
        
        # กรอก ระเบียบวาระการประชุม

        send_key = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[3]/td[2]/div/div[1]/div/div/div/div/input'))
        )
        assert send_key.is_displayed(), 'Element is not displayed!'
        assert send_key.is_enabled(), 'Element is not enabled!'
        send_key.send_keys('Test3')
        
        # คลิกรูปแบบวาระ

        Click_Add = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[3]/td[3]/div/div/div/div/div/div'))
        )
        assert Click_Add.is_displayed(), 'Element is not displayed!'
        assert Click_Add.is_enabled(), 'Element is not enabled!'
        Click_Add.click()
        
        # รูปแบบวาระ

        Click_Add = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[6]'))
        )
        assert Click_Add.is_displayed(), 'Element is not displayed!'
        assert Click_Add.is_enabled(), 'Element is not enabled!'
        Click_Add.click()

        Key_num = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[3]/td[2]/div/div[2]/div/div/div/div/div/div/div/input'))
        )
        assert Key_num.is_displayed(), 'Element is not displayed!'
        assert Key_num.is_enabled(), 'Element is not enabled!'
        Key_num.send_keys('8')

# ลบวาระทั้งหมด

        Click_Detele = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[3]/td[3]/div/button'))
        )
        assert Click_Detele.is_displayed(), 'Element is not displayed!'
        assert Click_Detele.is_enabled(), 'Element is not enabled!'
        Click_Detele.click()

        if Click_Detele:
            print('Click Delete Already :', True)
        else:
            print('Cannot Click Delete :', False)

        Click_Detele = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[2]/td[3]/div/button'))
        )
        assert Click_Detele.is_displayed(), 'Element is not displayed!'
        assert Click_Detele.is_enabled(), 'Element is not enabled!'
        Click_Detele.click()

        if Click_Detele:
            print('Click Delete Already :', True)
        else:
            print('Cannot Click Delete :', False)

        Click_Detele = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[2]/div/div/table/tbody/tr[1]/td[3]/div/button'))
        )
        assert Click_Detele.is_displayed(), 'Element is not displayed!'
        assert Click_Detele.is_enabled(), 'Element is not enabled!'
        Click_Detele.click()
        
        if Click_Detele:
            print('Click Delete Already :', True)
        else:
            print('Cannot Click Delete :', False)

# Save 

        # Save = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[1]/button'))
        # )
        # assert Save.is_displayed(), 'Element is not displayed!'
        # assert Save.is_enabled(), 'Element is not enabled!'
        # Save.click()

        time.sleep(2)
        
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