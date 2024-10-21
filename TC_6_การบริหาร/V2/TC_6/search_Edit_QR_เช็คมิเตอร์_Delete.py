
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
from selenium.common.exceptions import NoSuchElementException,TimeoutException


def test_page_search_edit1(driver):
                
        try:
                # หน้า จัดการลูกหนี้
                driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/water-meter')
                driver.implicitly_wait(10)


                # คีย์ โครงการ

                Input_Text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
                )
                assert Input_Text.is_displayed(), 'Element is not displayed!'
                assert Input_Text.is_enabled(), 'Element is not enabled!'
                Input_Text.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
                Input_Text.send_keys('อาคาร C8' + Keys.ARROW_DOWN + Keys.ENTER)

                # คีย์ ชั้น / ห้อง

                floor = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/input'))
                )
                assert floor.is_displayed(), 'Element is not displayed!'
                assert floor.is_enabled(), 'Element is not enabled!'
                floor.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)

                # สถานะมิเตอร์

                status = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[3]/div[1]/div[2]/div/div/div')
                assert status.is_displayed(), 'Element is not displayed!'
                assert status.is_enabled(), 'Element is not enabled!'
                status.click()
                time.sleep(0.1)

                status = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]')
                assert status.is_displayed(), 'Element is not displayed!'
                assert status.is_enabled(), 'Element is not enabled!'
                status.click()

        
                # เลือกปี (สำหรับดาวโหลดประวัติการจดหน่วยน้ำ)

                Dete = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[1]/div[3]/div[2]/div/div/div')
                assert Dete.is_displayed(), 'Element is not displayed!'
                assert Dete.is_enabled(), 'Element is not enabled!'
                Dete.click()
                time.sleep(0.1)

                Dete1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/div[125]/button')
                assert Dete1.is_displayed(), 'Element is not displayed!'
                assert Dete1.is_enabled(), 'Element is not enabled!'
                Dete1.click()
                
                # ตั้งแต่เดือน

                Since_the_month = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[4]/div[2]/div[1]/div/div')
                assert Since_the_month.is_displayed(), 'Element is not displayed!'
                assert Since_the_month.is_enabled(), 'Element is not enabled!'
                Since_the_month.click()
                time.sleep(0.1)

                Since_the_month_1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[10]/button')
                assert Since_the_month.is_displayed(), 'Element is not displayed!'
                assert Since_the_month.is_enabled(), 'Element is not enabled!'
                Since_the_month_1.click() 
                time.sleep(0.1)

                Since_the_month_2 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/button')
                assert Since_the_month.is_displayed(), 'Element is not displayed!'
                assert Since_the_month.is_enabled(), 'Element is not enabled!'
                Since_the_month_2.send_keys(Keys.ESCAPE) 

                # ถึงเดือน
                To_the_month =driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[1]/div[4]/div[2]/div[2]/div/div')
                assert Since_the_month.is_displayed(), 'Element is not displayed!'
                assert Since_the_month.is_enabled(), 'Element is not enabled!'
                To_the_month.click()
                time.sleep(0.1)
                
                To_the_month_1 =driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[10]/button')
                assert Since_the_month.is_displayed(), 'Element is not displayed!'
                assert Since_the_month.is_enabled(), 'Element is not enabled!'
                To_the_month_1.click()
                time.sleep(0.1)

                To_the_month = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/button')
                To_the_month.send_keys(Keys.ESCAPE)

                # เลขมิเตอร์

                number = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[4]/div[2]/div[3]/div/div[2]/div/div/input')
                number.send_keys('00000000')

        # Refresh
                # management =driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div[4]/div[2]/div[4]/button')
                # management.click()
                # time.sleep(0.5)

        # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                                                                # ส่วนของแก้ไข
        # การจัดการ - แก้ไข 

                Edit = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/div/table/tbody/tr/td[8]/div/button[1]')
                assert Edit.is_displayed(), 'Element is not displayed!'
                assert Edit.is_enabled(), 'Element is not enabled!'
                Edit.click()
        
                time.sleep(1)  

        # คีย์ โครงการ

                # project = WebDriverWait(driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
                # )
                # assert project.is_displayed(), 'Element is not displayed!'
                # assert project.is_enabled(), 'Element is not enabled!'
                # time.sleep(2)

                Key_text = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
                )
                assert Key_text.is_displayed(), 'Element is not displayed!'
                assert Key_text.is_enabled(), 'Element is not enabled!'
                Key_text.send_keys(Keys.COMMAND + 'a' + Keys.DELETE) 
                Key_text.send_keys('อาคาร C8' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(1)

                # ชั้น / ห้อง

                floor_room = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/input'))
                )
                assert floor_room.is_displayed(), 'Element is not displayed!'
                assert floor_room.is_enabled(), 'Element is not enabled!'
                floor_room.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)

                # หมายเลขมิเตอร์น้ำ

                number = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[3]/div[1]/div/div[2]/div/div/input')
                assert number.is_displayed(), 'Element is not displayed!'
                assert number.is_enabled(), 'Element is not enabled!'
                number.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
                number.send_keys('950')

                # ขนาดมาตรน้ำ

                siez = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[3]/div[2]/div/div[2]/div/div/input')
                siez.send_keys('32') 

                # สถานะมิเตอร์

                status = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[3]/div[3]/div[2]/div/div/div')
                status.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                status.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                status.click()
                time.sleep(0.1) 

                status = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')
                status.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                status.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                status.click()  

                # วันที่ลงทะเบียน

                button = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[4]/div/div/div')
                assert button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                assert button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                button.click()
                time.sleep(0.1)

                button1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[4]')
                assert button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
                assert button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                button1.click()

                element = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[1]/div[2]/div/button[1]')) 
                )
                assert element.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert element.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                element.click()         
                time.sleep(2)


        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                                                                        # ส่วนของ QR Cord
        # รอให้ Element คลิกได้  # คลิก QR Cord
                click_QR_Code = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/div/table/tbody/tr/td[8]/div/button[2]')) # คลิกขอ เข้าสู่ระบบ
                )
                assert click_QR_Code.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert click_QR_Code.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                click_QR_Code.click()
                time.sleep(0.1)

                element = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button')) 
                )
                element.send_keys(Keys.ESCAPE)
                time.sleep(2)

                
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                                                                        # ส่วนของ 

        # รอให้ Element คลิกได้  # คลิก QR Cord

                QR_Code = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/div/table/tbody/tr/td[8]/div/button[3]')) # คลิกขอ เข้าสู่ระบบ
                )
                assert QR_Code.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert QR_Code.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                QR_Code.click()
                time.sleep(0.1)

        # เลือกปี
                select = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[3]/div[1]/div/div/div')) 
                )
                assert select.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert select.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                select.click()
                time.sleep(0.1)

                select = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/div[125]/button')) 
                )
                assert select.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert select.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                select.click()
                time.sleep(0.1)

                back = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/div[125]/button')
                back.send_keys(Keys.ESCAPE)
                time.sleep(0.1)

                back = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/button')) 
                )
                assert back.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert back.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                back.click()
                time.sleep(2)



        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                                                                        # ส่วน Button Delete
                button_delete = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/div/table/tbody/tr/td[8]/div/button[4]')) 
                )
                assert button_delete.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert button_delete.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                button_delete.click()
                time.sleep(2)

                # delete = WebDriverWait(driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]')) 
                # )
                # assert delete.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                # assert delete.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                # delete.click()
                # time.sleep(0.1)

                cancel = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[1]')) 
                )
                assert cancel.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า'
                assert cancel.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
                cancel.click()
                time.sleep(0.5)

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





