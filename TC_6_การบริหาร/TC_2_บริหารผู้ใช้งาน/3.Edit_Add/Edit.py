
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


class WebTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(login):

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        login.driver = webdriver.Chrome(options=options)
        # login.driver = webdriver.Chrome()  # หรือใช้ webdriver.Firefox(), webdriver.Edge(), etc.
        login.driver.get('https://msm-smarty-cms-staging.hr-impact.co/login')
        login.driver.set_window_size(1600, 1000)
        login.driver.implicitly_wait(10)

    # def test_page_title(self):
    #     driver = self.driver
    #     self.assertEqual(driver.title, 'Smarty msm')  # ตรวจสอบว่า title ของหน้าเว็บถูกต้อง

    def test_login_smarty(self):
        result = None
        time.sleep(1)

        try:
            wait = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input'))
            )
            print('รอจนกว่าจะสามารถกรอกรหัสได้ : Pass')

        # ป้อนรหัสผ่าน
            element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div/div[1]/div/div[1]/p')
            expected_text = 'เบอร์โทรศัพท์ / รหัสพนักงาน'
            assert element.text == expected_text, f"ข้อความไม่ตรงกัน: คาดว่า '{expected_text}' แต่ได้ '{element.text}'"
            time.sleep(0.1)

            Key_Password = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input'))
            )
            assert Key_Password.is_displayed(), 'Element is not displayed!'
            assert Key_Password.is_enabled(), 'Element is not enabled!'
            Key_Password.send_keys('00000') 


            input_key = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input')
            input_value = input_key.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}')    
            
            Click_Otp = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/button'))
            )
            assert Click_Otp.is_displayed(), 'Element is not displayed!'
            assert Click_Otp.is_enabled(), 'Element is not enabled!'
            Click_Otp.click() 

            if Click_Otp:
                print('กดคลิกขอ Otp สำเร็จ : Pass')
            else:
                print('กดคลิกขอ Otp ไม่สำเร็จ : Fail')

        # รอให้ Element คลิกได้  # คลิกขอ เข้าสู่ระบบ
            Click_submit = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/button')) # คลิกขอ เข้าสู่ระบบ
            )
            assert Click_submit.is_displayed(), 'Element is not displayed!'
            assert Click_submit.is_enabled(), 'Element is not enabled!'
            Click_submit.click()

            if Click_submit:
                print('กดคลิกขอ เข้าสู่ระบบ สำเร็จ : Pass')
            else:
                print('กดคลิกขอ เข้าสู่ระบบ ไม่สำเร็จ : Fail')

        except NoSuchElementException:
            self.fail('Element not Found')
        except AssertionError as e:
            self.fail(str(e))
        except Exception as o:
            self.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว')

        wait = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div/div/div/div[3]/ul/div'))
            )
        print('รอจนหน้าเว็ปโหลดเสร็จ : Pass')

        print('-------------------------------')



    def test_page_edit(self):
        # หน้า การบริหาร - จัดการ
        self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/residents')
        self.driver.implicitly_wait(20)

        # จัดการ ลูกตา

        manage = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[8]/button'))
        )
        assert manage.is_displayed(), 'Element is not displayed!'
        assert manage.is_enabled(), 'Element is not enabled!'
        manage.click()

        # Detele image
        time.sleep(0.1)
        delete_image = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/button'))
        )
        assert delete_image.is_displayed(), 'Element is not displayed!'
        assert delete_image.is_enabled(), 'Element is not enabled!'
        delete_image.click()
        
        # Upload image

        # อัพโหลดรูปภาพ Mac Os
        upload = self.driver.find_element(by=By.XPATH , value='//div/div[1]/div/form/div/div[1]/input')
        upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')
        time.sleep(0.5)

        # คีย์ ชื่อ

        key_name = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div[2]/div/div/input'))
        )
        assert key_name.is_displayed(), 'Element is not displayed!'
        assert key_name.is_enabled(), 'Element is not enabled!'
        key_name.send_keys(Keys.COMMAND+ 'a' +  Keys.DELETE)
        key_name.send_keys('Test')

        # คีย์ นามสกุล
        time.sleep(0.1)
        key_text = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[1]/div/form/div/div[2]/div[2]/div/div[2]/div/div/input'))
        )
        assert key_text.is_displayed(), 'Element is not displayed!'
        assert key_text.is_enabled(), 'Element is not enabled!'
        key_text.send_keys(Keys.COMMAND+ 'a' +  Keys.DELETE)
        key_text.send_keys('พร้อมจ่าย')
 
        # คีย์ Email 
        time.sleep(0.1)
        key_email = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[1]/div/form/div/div[3]/div[1]/div/div[2]/div/div/input'))
        )
        assert key_email.is_displayed(), 'Element is not displayed!'
        assert key_email.is_enabled(), 'Element is not enabled!'
        key_email.send_keys(Keys.COMMAND+ 'a' +  Keys.DELETE)
        key_email.send_keys('sss@gmail.com')

        # เบอร์โทรศัพท์
        time.sleep(0.1)
        key_number = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[1]/div/form/div/div[3]/div[2]/div/div[2]/div/div/input'))
        )
        assert key_number.is_displayed(), 'Element is not displayed!'
        assert key_number.is_enabled(), 'Element is not enabled!'
        key_number.send_keys(Keys.COMMAND+ 'a' +  Keys.DELETE)
        key_number.send_keys('0924296825')


        # เลขปประจำตัวประชาชน
        time.sleep(0.1)
        key_number = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div/div/form/div/div[4]/div/div[2]/div/div/input'))
        )
        assert key_number.is_displayed(), 'Element is not displayed!'
        assert key_number.is_enabled(), 'Element is not enabled!'
        key_number.send_keys(Keys.COMMAND+ 'a' +  Keys.DELETE)
        key_number.send_keys('012345678912')
        time.sleep(1)

        # เลื่อจอ

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(0.1)

# ------------------------------------------------------------------------------------------------------------------


        # เพิ่มโครงการ

        Add_projet = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div/div[1]/button'))
        )
        assert Add_projet.is_displayed(), 'Element is not displayed!'
        assert Add_projet.is_enabled(), 'Element is not enabled!'
        Add_projet.click()
        time.sleep(0.5)

        # เลือกตึกอาคาร

        select = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[2]/div/div[1]'))
        )
        assert select.is_displayed(), 'Element is not displayed!'
        assert select.is_enabled(), 'Element is not enabled!'
        select.click()
        time.sleep(0.1)

        select_10 = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[7]'))
        )
        assert select_10.is_displayed(), 'Element is not displayed!'
        assert select_10.is_enabled(), 'Element is not enabled!'
        select_10.click()
        time.sleep(1)  

        # ชั้น

        floor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[2]/div[2]/div/div/div'))
        )
        assert floor.is_displayed(), 'Element is not displayed!'
        assert floor.is_enabled(), 'Element is not enabled!'
        floor.click()
        time.sleep(0.2)

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
        element = WebDriverWait(self.driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/ul/li[5]"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
        )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
        print("Wait Show Element")
        time.sleep(0.5)

        room = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[5]'))
        )
        assert room.is_displayed(), 'Element is not displayed!'
        assert room.is_enabled(), 'Element is not enabled!'
        room.click()

        # ห้อง

        room = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[3]/div[2]/div/div'))
        )
        assert room.is_displayed(), 'Element is not displayed!'
        assert room.is_enabled(), 'Element is not enabled!'
        room.click()
        time.sleep(0.2)   

        C1 = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[15]'))
        )
        assert C1.is_displayed(), 'Element is not displayed!'
        assert C1.is_enabled(), 'Element is not enabled!'
        C1.click()
        time.sleep(0.3)

        # # สถานะ

        status = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[4]/div[2]/div/div'))
        )
        assert status.is_displayed(), 'Element is not displayed!'
        assert status.is_enabled(), 'Element is not enabled!'
        status.click()

        C1 = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[1]'))
        )
        assert C1.is_displayed(), 'Element is not displayed!'
        assert C1.is_enabled(), 'Element is not enabled!'
        C1.click()
        time.sleep(0.1) 
        
        # Upload image
        # อัพโหลดรูปภาพ Mac Os

        upload = self.driver.find_element(by=By.XPATH , value='//div[1]/div/form/div/div[5]/div[2]/input')
        upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')
        time.sleep(0.5)
        
        # Save

        # Save = WebDriverWait(self.driver, 30).until(
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

        x1 = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//h2/div/button'))
        )
        assert x1.is_displayed(), 'Element is not displayed!'
        assert x1.is_enabled(), 'Element is not enabled!'
        x1.click()
        time.sleep(1)



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
 

                                                                                #  ที่อยู่จัดส่ง

        # คลิก ที่อยู่จัดส่ง

        address = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[6]/button'))
        )
        assert address.is_displayed(), 'Element is not displayed!'
        assert address.is_enabled(), 'Element is not enabled!'
        address.click()
        time.sleep(0.1)
    
# ค้นหา element ที่ต้องการให้มองเห็น
        element_2 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/button")

# ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
        time.sleep(1)


        # ประเภทที่อยู่จัดส่ง

        # เลื่อนหน้าจอไปยังองค์ประกอบ
        element = self.driver.find_element(By.XPATH, '//div/div[1]/form/div/div[1]/div[2]/div/div/div')
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        time.sleep(0.2)

        # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
        element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
        )
        # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
        print("Wait Show Element")
        time.sleep(0.2)

        click = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[2]'))
        )
        assert click.is_displayed(), 'Element is not displayed!'
        assert click.is_enabled(), 'Element is not enabled!'
        click.click()
        time.sleep(0.2)

        # คีย์ ชื่อ

        click_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[2]/div/div[2]/div/div'))
        )
        assert click_name.is_displayed(), 'Element is not displayed!'
        assert click_name.is_enabled(), 'Element is not enabled!'
        click_name.click()
        time.sleep(0.2)

        key_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[2]/div/div[2]/div/div/input'))
        )
        assert key_name.is_displayed(), 'Element is not displayed!'
        assert key_name.is_enabled(), 'Element is not enabled!'
        key_name.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_name.send_keys('162/03 โครงการเมืองทองบางนา A2 หมู่ 70')
        time.sleep(0.1)

        # คีย์ ซอย

        key_alley = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[3]/div[1]/div/div[2]/div/div/input'))
        )
        assert key_alley.is_displayed(), 'Element is not displayed!'
        assert key_alley.is_enabled(), 'Element is not enabled!'
        key_alley.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_alley.send_keys('10')
        time.sleep(0.1)

        # คีย์ ถนน

        key_alley = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[3]/div[2]/div/div[2]/div/div/input'))
        )
        assert key_alley.is_displayed(), 'Element is not displayed!'
        assert key_alley.is_enabled(), 'Element is not enabled!'
        key_alley.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_alley.send_keys('10')
        time.sleep(0.1)

        # คีย์ ตำบล

        key_road = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[4]/div[1]/div/div[2]/div/div/input'))
        )
        assert key_road.is_displayed(), 'Element is not displayed!'
        assert key_road.is_enabled(), 'Element is not enabled!'
        key_road.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_road.send_keys('คลองท่อมเหนือ')
        time.sleep(0.1)


        # คีย์ อำเภอ

        key_district = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[4]/div[2]/div/div[2]/div/div/input'))
        )
        assert key_district.is_displayed(), 'Element is not displayed!'
        assert key_district.is_enabled(), 'Element is not enabled!'
        key_district.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_district.send_keys('คลองท่อม')
        time.sleep(0.1)
        

        # คีย์ จังหวัด

        key_province = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[5]/div[1]/div/div[2]/div/div/input'))
        )
        assert key_province.is_displayed(), 'Element is not displayed!'
        assert key_province.is_enabled(), 'Element is not enabled!'
        key_province.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_province.send_keys('กระบี่')
        time.sleep(0.1)

# คีย์ รหัสไปรษณีย์

        key_province = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[1]/form/div/div[5]/div[2]/div/div[2]/div/div/input'))
        )
        assert key_province.is_displayed(), 'Element is not displayed!'
        assert key_province.is_enabled(), 'Element is not enabled!'
        key_province.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_province.send_keys('81122')
        time.sleep(0.1)

# x

        x1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/h2/div/button'))
        )
        assert x1.is_displayed(), 'Element is not displayed!'
        assert x1.is_enabled(), 'Element is not enabled!'
        x1.click()
        time.sleep(0.1)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
 
                                                                                #  ย้ายออก

        # คลิก ย้ายออก

        Move_out = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[7]/div/button'))
        )
        assert Move_out.is_displayed(), 'Element is not displayed!'
        assert Move_out.is_enabled(), 'Element is not enabled!'
        Move_out.click()
        time.sleep(0.1)

        # คลิก ยกเลิก

        Cancel = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[1]'))
        )
        assert Cancel.is_displayed(), 'Element is not displayed!'
        assert Cancel.is_enabled(), 'Element is not enabled!'
        Cancel.click()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
 
                                                                                #  Edit


        # คลิก แก้ไข
 
        edit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[8]/div/button'))
        )
        assert edit.is_displayed(), 'Element is not displayed!'
        assert edit.is_enabled(), 'Element is not enabled!'
        edit.click()
        time.sleep(0.1)


# ค้นหา element ที่ต้องการให้มองเห็น
        element_2 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/button")

# ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
        time.sleep(1)

        result_element = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/button')    
        self.assertIsNotNone(result_element)
        time.sleep(0.1)

# ค้นหา element ที่ต้องการให้มองเห็น
        element_2 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[2]/div/div/div")

# ใช้ JavaScript เพื่อเลื่อนให้ element มองเห็น
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
        time.sleep(1.5)


        # เลือกตึกอาคาร

        building = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[1]/div[2]/div/div/div")) 
        )
        assert building.is_displayed(), 'Element is not displayed!'
        assert building.is_enabled(), 'Element is not enabled!'
        building.click()
        time.sleep(0.1)

        select = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/ul/li[6]')
        assert select.is_displayed(), 'Element is not displayed!'
        assert select.is_enabled(), 'Element is not enabled!'
        select.click()
        time.sleep(1)  

        # ชั้น

        floor = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[2]/div[2]/div/div/div"))  # เปลี่ยนเป็น selector ที่คุณต้องการ
        )
        assert floor.is_displayed(), 'Element is not displayed!'
        assert floor.is_enabled(), 'Element is not enabled!'
        floor.click()
        time.sleep(1)

        select_floor = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/ul/li[8]"))  
        )
        assert select_floor.is_displayed(), 'Element is not displayed!'
        assert select_floor.is_enabled(), 'Element is not enabled!'
        select_floor.click()

        time.sleep(0.1) 

        # ห้อง

        room = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[3]/div[2]/div/div/div"))  
        )
        assert room.is_displayed(), 'Element is not displayed!'
        assert room.is_enabled(), 'Element is not enabled!'
        room.click()
        time.sleep(0.1)   

        select_room = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/ul/li[15]"))  
        )
        assert select_room.is_displayed(), 'Element is not displayed!'
        assert select_room.is_enabled(), 'Element is not enabled!'
        select_room.click()

        # สถานะ

        status = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[4]/div[2]/div/div/div"))  
        )
        assert status.is_displayed(), 'Element is not displayed!'
        assert status.is_enabled(), 'Element is not enabled!'
        status.click()
        time.sleep(0.1)


        status = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/ul/li[4]"))  
        )
        assert status.is_displayed(), 'Element is not displayed!'
        assert status.is_enabled(), 'Element is not enabled!'
        status.click()
        time.sleep(0.1) 
        

        # Upload image

        # อัพโหลดรูปภาพ Mac Os
        upload = self.driver.find_element(by=By.XPATH , value='/html/body/div[2]/div[3]/div/div[1]/div/form/div/div[5]/div[2]/input')
        upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')
        time.sleep(1)

# Save 

        # Save = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/form/button"))  
        # )
        # assert Save.is_displayed(), 'Element is not displayed!'
        # assert Save.is_enabled(), 'Element is not enabled!'
        # Save.click()


    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        # print('___Test Pass__')
        cls.driver.quit()   

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



