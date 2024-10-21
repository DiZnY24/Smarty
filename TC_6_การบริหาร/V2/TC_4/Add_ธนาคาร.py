
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
from pynput.keyboard import Key, Controller 
from selenium.common.exceptions import NoSuchElementException,TimeoutException



def test_page_add_bank2(driver):

        try:
                # หน้า บริหารโครงการ
                driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/properties')
                driver.implicitly_wait(30)

                # เพิ่มโครงการ

                Project = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/div[1]/div[1]/div/button'))
                )
                assert Project.is_displayed(), 'Element is not displayed!'
                assert Project.is_enabled(), 'Element is not enabled!'
                Project.click()
                time.sleep(0.5)

                # บัญชีธนาคาร

                bank = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[1]/div[2]/div/button[2]'))
                )
                assert bank.is_displayed(), 'Element is not displayed!'
                assert bank.is_enabled(), 'Element is not enabled!'
                bank.click()
                time.sleep(0.1)

                button = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[1]/div[2]/div/button[2]')
                assert button.text == 'บัญชีธนาคาร', f"Expected 'Expected Button Text' but got '{button.text}'"
                time.sleep(0.1)

                wait_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/input")) 
                )
                print("Element is visible. Proceeding with the next step.")
                time.sleep(0.1) 

                # ชื่อบัญชี

                Key_Text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/input'))
                )
                assert Key_Text.is_displayed(), 'Element is not displayed!'
                assert Key_Text.is_enabled(), 'Element is not enabled!'
                Key_Text.send_keys('นิติบุคคลอาคารชุด ดับเบิ้ลเลค คอนโดมิเนียม เฟส 2')
                time.sleep(0.1)

                # ชนิดบัญชี
                
                Key_Text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/input'))
                )
                assert Key_Text.is_displayed(), 'Element is not displayed!'
                assert Key_Text.is_enabled(), 'Element is not enabled!'
                Key_Text.send_keys('ออมทรัพย์')
                time.sleep(0.1)

                # ธนาคาร

                bank = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div/input'))
                )
                assert bank.is_displayed(), 'Element is not displayed!'
                assert bank.is_enabled(), 'Element is not enabled!'
                bank.send_keys('กสิกรไทย')
                time.sleep(0.1)
                
                # สาขา

                branch = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/input'))
                )
                assert branch.is_displayed(), 'Element is not displayed!'
                assert branch.is_enabled(), 'Element is not enabled!'
                branch.send_keys('สำนักแจ้งวัฒนะเมืองทองธานี')
                time.sleep(0.1)
                
                # เลขที่บัญชี

                number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[3]/div/div/div[2]/div/div/input'))
                )
                assert number.is_displayed(), 'Element is not displayed!'
                assert number.is_enabled(), 'Element is not enabled!'
                number.send_keys('0053987656')
                time.sleep(0.1)


                # เลขประจำตัวผู้เสียภาษี
                # search_box = driver.find_element(By.XPATH, '')
                # search_box.send_keys('0994001106649')
                # time.sleep(0.1)
                
                # Suffix-code   

                number_code = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div/div/input'))
                )
                assert number_code.is_displayed(), 'Element is not displayed!'
                assert number_code.is_enabled(), 'Element is not enabled!'
                number_code.send_keys('72')
                time.sleep(0.1)
                
                # QR CODE

        #         Add_image = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[4]/div/div/div')
        #         assertTrue(Add_image.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
        #         assertTrue(Add_image.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
        #         Add_image.click()
        #         time.sleep(1)

                # อัพโหลดรูปภาพ

                # อัพโหลดรูปภาพ Mac Os
                upload = driver.find_element(by=By.XPATH , value='/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[1]/div[4]/div/input')
                upload.send_keys('/Users/dizny/Downloads/Image/car.jpg')
                time.sleep(1)

                # ใช้งาน Cross Bank

                Cross_bank = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div[2]/label/span[1]'))
                )
                assert Cross_bank.is_displayed(), 'Element is not displayed!'
                assert Cross_bank.is_enabled(), 'Element is not enabled!'
                Cross_bank.click()
                time.sleep(0.1)

                # บันทึก

                # Save = WebDriverWait(driver, 10).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[2]/button'))
                # )
                # assert Save.is_displayed(), 'Element is not displayed!'
                # assert Save.is_enabled(), 'Element is not enabled!'
                # Save.click()
                # time.sleep(0.1)

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
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



