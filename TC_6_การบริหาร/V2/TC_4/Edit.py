
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
from selenium.common.exceptions import NoSuchElementException,TimeoutException



def test_page_edit1(driver):
        # หน้า การบริหาร - ผู้ใช้งาน
        driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/properties')
        driver.implicitly_wait(30)

        try:
            # แก้ไข

            click_edit = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/button'))
            )
            assert click_edit.is_displayed(), 'Element is not displayed!'
            assert click_edit.is_enabled(), 'Element is not enabled!'
            click_edit.click()
            time.sleep(0.3)
            
            # รหัสอาคาร

            key_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)  
            key_number.send_keys('DBL1')
            time.sleep(0.3)
            
            # ชื่อโครงการ (เต็ม)        

            key_project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_project.is_displayed(), 'Element is not displayed!'
            assert key_project.is_enabled(), 'Element is not enabled!'
            key_project.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)  
            key_project.send_keys('นิติบุคคลอาคารชุด ดับเบิ้ลเลค DBL1')
            time.sleep(0.1)

            # ชื่อโครงการ (ย่อ)

            key_name_project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/div[3]/div/div[2]/div/div/input'))
            )
            assert key_name_project.is_displayed(), 'Element is not displayed!'
            assert key_name_project.is_enabled(), 'Element is not enabled!'
            key_name_project.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)  
            key_name_project.send_keys('MTTD-DBL1')
            time.sleep(0.1)

            # เลขที่โครงการ

            key_name_project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_name_project.is_displayed(), 'Element is not displayed!'
            assert key_name_project.is_enabled(), 'Element is not enabled!'
            key_name_project.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)  
            key_name_project.send_keys('3')
            time.sleep(0.1)

            # ขนาดพื้นที่ (ไร่)

            key_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)  
            key_number.send_keys('5')
            time.sleep(0.1)

            # เบอร์ติดต่อ

            key_phone_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[3]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_phone_number.is_displayed(), 'Element is not displayed!'
            assert key_phone_number.is_enabled(), 'Element is not enabled!'
            key_phone_number.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)  
            key_phone_number.send_keys('0659373999')
            time.sleep(0.1)
            
            # เลขประจำตัวผู้เสียภาษี
            
            key_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[3]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_number.is_displayed(), 'Element is not displayed!'
            assert key_number.is_enabled(), 'Element is not enabled!'
            key_number.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)  
            key_number.send_keys('0994001106111')
            time.sleep(0.1)

            # อีเมล

            key_gmail = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[3]/div[3]/div/div[2]/div/div/input'))
                )
            assert key_gmail.is_displayed(), 'Element is not displayed!'
            assert key_gmail.is_enabled(), 'Element is not enabled!'
            key_gmail.send_keys(Keys.COMMAND + 'a' + Keys.DELETE) 
            key_gmail.send_keys('doe@msm-muangthong.com')
            time.sleep(0.1)

            # เลขที่อยู่

            Address_number = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[4]/div[1]/div/div[2]/div/div/input'))
                )
            assert Address_number.is_displayed(), 'Element is not displayed!'
            assert Address_number.is_enabled(), 'Element is not enabled!'
            Address_number.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Address_number.send_keys('100 หมู่6')
            time.sleep(0.1)

            # อาคาร

            building = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div/div/input'))
                )
            assert building.is_displayed(), 'Element is not displayed!'
            assert building.is_enabled(), 'Element is not enabled!'
            building.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            building.send_keys('-')
            time.sleep(0.1)

            # ถนน

            road = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[4]/div[3]/div/div[2]/div/div/input'))
                )
            assert road.is_displayed(), 'Element is not displayed!'
            assert road.is_enabled(), 'Element is not enabled!'
            road.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            road.send_keys('-')
            time.sleep(0.1)

            # อยู่ที่

            Address_number = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[5]/div/div/div/div[2]/div/div/input'))
                )
            assert Address_number.is_displayed(), 'Element is not displayed!'
            assert Address_number.is_enabled(), 'Element is not enabled!'
            Address_number.send_keys('บางตะไนย์ / ปากเกร็ด / นนทบุรี / 11120' + Keys.ARROW_DOWN )
            time.sleep(0.1)

            ESC = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/div/div[5]/div/div/div/div[2]/div/div/input')
            ESC.send_keys(Keys.ESCAPE)
            time.sleep(0.1)

            # Save

            # Save = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/form/button'))
            #     )
            # assert Save.is_displayed(), 'Element is not displayed!'
            # assert Save.is_enabled(), 'Element is not enabled!'
            # Save.click()
            # time.sleep(0.1)
            

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            

            # บัญชีธนาคาร

            bank = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[1]/div[2]/div/button[2]'))
            )
            assert bank.is_displayed(), 'Element is not displayed!'
            assert bank.is_enabled(), 'Element is not enabled!'  
            bank.click()
            time.sleep(0.5)

            # ชื่อบัญชี

            key_name = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/input'))
            )
            assert key_name.is_displayed(), 'Element is not displayed!'
            assert key_name.is_enabled(), 'Element is not enabled!'  
            key_name.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            key_name.send_keys('นิติบุคคลอาคารชุด ดับเบิ้ลเลค คอนโดมิเนียม เฟส 2')
            time.sleep(0.5)
            
            # ชนิดบัญชี
            
            key_bank = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/input'))
            )
            assert key_bank.is_displayed(), 'Element is not displayed!'
            assert key_bank.is_enabled(), 'Element is not enabled!'  
            key_bank.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            key_bank.send_keys('ออมทรัพย์')
            time.sleep(0.5)


            # ธนาคาร

            search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div/input')
            search_box.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            search_box.send_keys('กสิกรไทย')
            time.sleep(0.1)

            # สาขา
            search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/input')
            search_box.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            search_box.send_keys('สำนักแจ้งวัฒนะเมืองทองธานี')
            time.sleep(0.1)

            # เลขที่บัญชี
            search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[3]/div/div/div[2]/div/div/input')
            search_box.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            search_box.send_keys('0053987656')
            time.sleep(0.1)

            # เลขประจำตัวผู้เสียภาษี
            # search_box = driver.find_element(By.XPATH, '')
            # search_box.send_keys('0994001106649')
            # time.sleep(0.1)
            
            # Suffix-code   
            search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div/div/input')
            search_box.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            search_box.send_keys('72')
            time.sleep(0.1)

            # QR CODE

            # Add_image = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[4]/div/div/div')
            # Add_image.click()
            # time.sleep(1)

            # อัพโหลดรูปภาพ
            # อัพโหลดรูปภาพ Mac Os
            upload = driver.find_element(by=By.XPATH , value='/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[4]/div/input')
            upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')
            time.sleep(0.1)

            # ใช้งาน Cross Bank
            Click = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[2]/label/span[1]')
            Click.click()

            # บันทึก
            # Save = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[2]/button').click()

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            # ตั้งค่าการเรียกเก็บ
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[1]/div[2]/div/button[3]'))
            )
            element.click()
            time.sleep(1)

            # เพิ่มโครงการ
            Add_ = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[4]/div/div/button')
            Add_.click()
            time.sleep(1)

            # รหัส
            Key_Text = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[1]/div[1]/div/div[2]/div/div/input')
            # Key_Text.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Key_Text.send_keys('123')
            time.sleep(0.3)
            
            # ชื่อรายการ
            Key_Text = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[1]/div[2]/div/div[2]/div/div/input')
            # Key_Text.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Key_Text.send_keys('test')
            time.sleep(0.3)

            # จำนวนหน่วย
            Key_Text = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[1]/div[3]/div/div[2]/div/div/input')
            # Key_Text.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
            Key_Text.send_keys('20')
            time.sleep(0.3)

            # ส่วนลด
            Key_Text = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[1]/div[4]/div/div[2]/div/div/input')
            # Key_Text.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
            Key_Text.send_keys('5')
            time.sleep(0.3)

            # ราคาต่อหน่วย - ห้องอยู่อาศัย
            Key_Text = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/div[1]/div/div[2]/div/div/input')
            # Key_Text.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
            Key_Text.send_keys('1')
            time.sleep(0.3)

            # ราคาต่อหน่วย - ห้องร้านค้า
            Key_Text = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/div[2]/div/div[2]/div/div/input')
            # Key_Text.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
            Key_Text.send_keys('1')
            time.sleep(0.3)

            # ราคาต่อหน่วย - ห้องพิเศษ
            Key_Text = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/div[3]/div/div[2]/div/div/input')
            # Key_Text.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
            Key_Text.send_keys('1')
            time.sleep(0.3)

            # เรียกเก็บรายเดือน
            Add_ = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/label/span[1]')
            Add_.click()
            time.sleep(0.3)

            # ยกเลิก
            # cancel = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[3]/button[1]')
            # cancel.click()
            # time.sleep(0.3)

            # # ยืนยัน
            # confirm = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/form/div[3]/button[2]')
            # confirm.click()
            # time.sleep(0.3)

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
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



