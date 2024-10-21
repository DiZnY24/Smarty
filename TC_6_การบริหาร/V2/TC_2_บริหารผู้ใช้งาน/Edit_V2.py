
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from pynput.keyboard import Key, Controller 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException,TimeoutException




def test_page_edit(driver):
        

        # หน้า การบริหาร - จัดการ
        driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/residents')
        driver.implicitly_wait(20)

        # จัดการ ลูกตา

        manage = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[8]/button'))
        )
        assert manage.is_displayed(), 'Element is not displayed!'
        assert manage.is_enabled(), 'Element is not enabled!'
        manage.click()

        # Detele image
        time.sleep(0.1)
        delete_image = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/button'))
        )
        assert delete_image.is_displayed(), 'Element is not displayed!'
        assert delete_image.is_enabled(), 'Element is not enabled!'
        delete_image.click()
        
        # Upload image

        # อัพโหลดรูปภาพ Mac Os
        upload = driver.find_element(by=By.XPATH , value='//div/div[1]/div/form/div/div[1]/input')
        upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')
        time.sleep(0.5)

        # คีย์ ชื่อ

        key_name = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div[2]/div/div/input'))
        )
        assert key_name.is_displayed(), 'Element is not displayed!'
        assert key_name.is_enabled(), 'Element is not enabled!'
        key_name.send_keys(Keys.COMMAND+ 'a' +  Keys.DELETE)
        key_name.send_keys('Test')

        # คีย์ นามสกุล
        time.sleep(0.1)
        key_text = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[1]/div/form/div/div[2]/div[2]/div/div[2]/div/div/input'))
        )
        assert key_text.is_displayed(), 'Element is not displayed!'
        assert key_text.is_enabled(), 'Element is not enabled!'
        key_text.send_keys(Keys.COMMAND+ 'a' +  Keys.DELETE)
        key_text.send_keys('พร้อมจ่าย')
 
        # คีย์ Email 
        time.sleep(0.1)
        key_email = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[1]/div/form/div/div[3]/div[1]/div/div[2]/div/div/input'))
        )
        assert key_email.is_displayed(), 'Element is not displayed!'
        assert key_email.is_enabled(), 'Element is not enabled!'
        key_email.send_keys(Keys.COMMAND+ 'a' +  Keys.DELETE)
        key_email.send_keys('sss@gmail.com')

        # เบอร์โทรศัพท์
        time.sleep(0.1)
        key_number = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[1]/div/form/div/div[3]/div[2]/div/div[2]/div/div/input'))
        )
        assert key_number.is_displayed(), 'Element is not displayed!'
        assert key_number.is_enabled(), 'Element is not enabled!'
        key_number.send_keys(Keys.COMMAND+ 'a' +  Keys.DELETE)
        key_number.send_keys('0924296825')


        # เลขปประจำตัวประชาชน
        time.sleep(0.1)
        key_number = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[4]/div/div[2]/div/div/input'))
        )
        assert key_number.is_displayed(), 'Element is not displayed!'
        assert key_number.is_enabled(), 'Element is not enabled!'
        key_number.send_keys(Keys.COMMAND+ 'a' +  Keys.DELETE)
        key_number.send_keys('012345678912')
        time.sleep(1)

        # เลื่อจอ

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(0.1)

# ------------------------------------------------------------------------------------------------------------------


        # เพิ่มโครงการ

        Add_projet = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div/div[1]/button'))
        )
        assert Add_projet.is_displayed(), 'Element is not displayed!'
        assert Add_projet.is_enabled(), 'Element is not enabled!'
        Add_projet.click()
        time.sleep(2.5)

        # เลือกตึกอาคาร

        select = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[2]/div/div'))
        )
        assert select.is_displayed(), 'Element is not displayed!'
        assert select.is_enabled(), 'Element is not enabled!'
        select.click()
        time.sleep(0.1)

        select_10 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[7]'))
        )
        assert select_10.is_displayed(), 'Element is not displayed!'
        assert select_10.is_enabled(), 'Element is not enabled!'
        select_10.click()
        time.sleep(2.5)  

        # ชั้น

        floor = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[2]/div[2]/div/div/div'))
        )
        assert floor.is_displayed(), 'Element is not displayed!'
        assert floor.is_enabled(), 'Element is not enabled!'
        floor.click()
        time.sleep(0.2)

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
        element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/ul/li[5]"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
        )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
        print("Wait Show Element")
        time.sleep(0.5)

        room = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[5]'))
        )
        assert room.is_displayed(), 'Element is not displayed!'
        assert room.is_enabled(), 'Element is not enabled!'
        room.click()

        # ห้อง

        room = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[3]/div[2]/div/div'))
        )
        assert room.is_displayed(), 'Element is not displayed!'
        assert room.is_enabled(), 'Element is not enabled!'
        room.click()
        time.sleep(0.2)   

        C1 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[15]'))
        )
        assert C1.is_displayed(), 'Element is not displayed!'
        assert C1.is_enabled(), 'Element is not enabled!'
        C1.click()
        time.sleep(0.3)

        # # สถานะ

        status = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[4]/div[2]/div/div'))
        )
        assert status.is_displayed(), 'Element is not displayed!'
        assert status.is_enabled(), 'Element is not enabled!'
        status.click()

        C1 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[1]'))
        )
        assert C1.is_displayed(), 'Element is not displayed!'
        assert C1.is_enabled(), 'Element is not enabled!'
        C1.click()
        time.sleep(0.1) 
        
        # Upload image
        # อัพโหลดรูปภาพ Mac Os

        upload = driver.find_element(by=By.XPATH , value='//div[1]/div/form/div/div[5]/div[2]/input')
        upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')
        time.sleep(0.5)
        
        # Save

        # Save = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/button'))
        # )
        # assert Save.is_displayed(), 'Element is not displayed!'
        # assert Save.is_enabled(), 'Element is not enabled!'
        # Save.click()

        # if Save:
        #     print('Click Save Already :', True)
        # else:
        #     print('Cannot Click Save :', False)


        # x

        x1 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//h2/div/button'))
        )
        assert x1.is_displayed(), 'Element is not displayed!'
        assert x1.is_enabled(), 'Element is not enabled!'
        x1.click()
        time.sleep(1)



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
 

                                                                                #  ที่อยู่จัดส่ง

        # คลิก ที่อยู่จัดส่ง

        address = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[6]/button'))
        )
        assert address.is_displayed(), 'Element is not displayed!'
        assert address.is_enabled(), 'Element is not enabled!'
        address.click()
        time.sleep(0.1)
    
# ค้นหา element ที่ต้องการให้มองเห็น
        element_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/button")

# ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
        driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
        time.sleep(1)


        # ประเภทที่อยู่จัดส่ง

        # เลื่อนหน้าจอไปยังองค์ประกอบ
        element = driver.find_element(By.XPATH, '//div/div[1]/form/div/div[1]/div[2]/div/div/div')
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
        time.sleep(0.2)

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
        )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
        print("Wait Show Element")
        time.sleep(0.2)

        click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[2]'))
        )
        assert click.is_displayed(), 'Element is not displayed!'
        assert click.is_enabled(), 'Element is not enabled!'
        click.click()
        time.sleep(0.2)

        # คีย์ ชื่อ

        click_name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[2]/div/div[2]/div/div'))
        )
        assert click_name.is_displayed(), 'Element is not displayed!'
        assert click_name.is_enabled(), 'Element is not enabled!'
        click_name.click()
        time.sleep(0.2)

        key_name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[2]/div/div[2]/div/div/input'))
        )
        assert key_name.is_displayed(), 'Element is not displayed!'
        assert key_name.is_enabled(), 'Element is not enabled!'
        key_name.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_name.send_keys('162/03 โครงการเมืองทองบางนา A2 หมู่ 70')
        time.sleep(0.1)

        # คีย์ ซอย

        key_alley = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[3]/div[1]/div/div[2]/div/div/input'))
        )
        assert key_alley.is_displayed(), 'Element is not displayed!'
        assert key_alley.is_enabled(), 'Element is not enabled!'
        key_alley.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_alley.send_keys('10')
        time.sleep(0.1)

        # คีย์ ถนน

        key_alley = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[3]/div[2]/div/div[2]/div/div/input'))
        )
        assert key_alley.is_displayed(), 'Element is not displayed!'
        assert key_alley.is_enabled(), 'Element is not enabled!'
        key_alley.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_alley.send_keys('10')
        time.sleep(0.1)

        # คีย์ ตำบล

        key_road = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[4]/div[1]/div/div[2]/div/div/input'))
        )
        assert key_road.is_displayed(), 'Element is not displayed!'
        assert key_road.is_enabled(), 'Element is not enabled!'
        key_road.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_road.send_keys('คลองท่อมเหนือ')
        time.sleep(0.1)


        # คีย์ อำเภอ

        key_district = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[4]/div[2]/div/div[2]/div/div/input'))
        )
        assert key_district.is_displayed(), 'Element is not displayed!'
        assert key_district.is_enabled(), 'Element is not enabled!'
        key_district.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_district.send_keys('คลองท่อม')
        time.sleep(0.1)
        

        # คีย์ จังหวัด

        key_province = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[5]/div[1]/div/div[2]/div/div/input'))
        )
        assert key_province.is_displayed(), 'Element is not displayed!'
        assert key_province.is_enabled(), 'Element is not enabled!'
        key_province.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_province.send_keys('กระบี่')
        time.sleep(0.1)

# คีย์ รหัสไปรษณีย์

        key_province = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[5]/div[2]/div/div[2]/div/div/input'))
        )
        assert key_province.is_displayed(), 'Element is not displayed!'
        assert key_province.is_enabled(), 'Element is not enabled!'
        key_province.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_province.send_keys('81122')
        time.sleep(0.1)

# x

        x1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/h2/div/button'))
        )
        assert x1.is_displayed(), 'Element is not displayed!'
        assert x1.is_enabled(), 'Element is not enabled!'
        x1.click()
        time.sleep(0.1)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
 
                                                                                #  ย้ายออก

        # คลิก ย้ายออก

        Move_out = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[7]/div/button'))
        )
        assert Move_out.is_displayed(), 'Element is not displayed!'
        assert Move_out.is_enabled(), 'Element is not enabled!'
        Move_out.click()
        time.sleep(0.1)

        # คลิก ยกเลิก

        Cancel = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[1]'))
        )
        assert Cancel.is_displayed(), 'Element is not displayed!'
        assert Cancel.is_enabled(), 'Element is not enabled!'
        Cancel.click()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
 
                                                                                #  Edit


        # คลิก แก้ไข
 
        edit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[8]/div/button'))
        )
        assert edit.is_displayed(), 'Element is not displayed!'
        assert edit.is_enabled(), 'Element is not enabled!'
        edit.click()
        time.sleep(0.1)


# ค้นหา element ที่ต้องการให้มองเห็น
        element_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/button")

# ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
        driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
        time.sleep(1)

# ค้นหา element ที่ต้องการให้มองเห็น
        element_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[2]/div/div/div")

# ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
        driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
        time.sleep(1.5)


        # เลือกตึกอาคาร

        building = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[2]/div/div/div")) 
        )
        assert building.is_displayed(), 'Element is not displayed!'
        assert building.is_enabled(), 'Element is not enabled!'
        building.click()
        time.sleep(2.5)

        select = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/ul/li[6]')
        assert select.is_displayed(), 'Element is not displayed!'
        assert select.is_enabled(), 'Element is not enabled!'
        select.click()
        time.sleep(2.5)  

        # ชั้น

        floor = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[2]/div[2]/div/div/div"))
        )
        assert floor.is_displayed(), 'Element is not displayed!'
        assert floor.is_enabled(), 'Element is not enabled!'
        floor.click()
        time.sleep(0.5)

        wait_floor = WebDriverWait(driver, 30).until(
              EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/ul/li[10]'))
        )
        print('Wait Element :', True)

        select_floor = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/ul/li[8]"))  
        )
        assert select_floor.is_displayed(), 'Element is not displayed!'
        assert select_floor.is_enabled(), 'Element is not enabled!'
        select_floor.click()

        time.sleep(0.1) 

        # ห้อง

        room = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[3]/div[2]/div/div/div"))  
        )
        assert room.is_displayed(), 'Element is not displayed!'
        assert room.is_enabled(), 'Element is not enabled!'
        room.click()
        time.sleep(0.1)   

        select_room = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/ul/li[15]"))  
        )
        assert select_room.is_displayed(), 'Element is not displayed!'
        assert select_room.is_enabled(), 'Element is not enabled!'
        select_room.click()

        # สถานะ

        status = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[4]/div[2]/div/div/div"))  
        )
        assert status.is_displayed(), 'Element is not displayed!'
        assert status.is_enabled(), 'Element is not enabled!'
        status.click()
        time.sleep(0.1)


        status = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/ul/li[4]"))  
        )
        assert status.is_displayed(), 'Element is not displayed!'
        assert status.is_enabled(), 'Element is not enabled!'
        status.click()
        time.sleep(0.1) 
        

        # Upload image

        # อัพโหลดรูปภาพ Mac Os
        upload = driver.find_element(by=By.XPATH , value='/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[5]/div[2]/input')
        upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')
        time.sleep(2)

# Save 

        # Save = WebDriverWait(driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/button"))  
        # )
        # assert Save.is_displayed(), 'Element is not displayed!'
        # assert Save.is_enabled(), 'Element is not enabled!'
        # Save.click()


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



