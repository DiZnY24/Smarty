
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys 
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


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
        

    def test_page_check_in(self):

                # เปิดหน้า จัดการประชุม
        try:
                self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/agm/meetings')
                self.driver.implicitly_wait(30)

                check_in = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[8]/div/button[2]'))
                )
                assert check_in.is_displayed(), 'Element is not displayed!'
                assert check_in.is_enabled(), 'Element is not enabled!'
                check_in.click()

                if check_in:
                        print('Click Check in Already :', True)
                else:
                        print('Cannot Click Check in :', False)

                # เพิ่มห้อง
                time.sleep(1)

                key_text = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/input'))
                )
                assert key_text.is_displayed(), 'Element is not displayed!'
                assert key_text.is_enabled(), 'Element is not enabled!'
                key_text.send_keys('3110300182281' + Keys.ENTER)
                

                # บทบาท เจ้าของกรรมสิทธิ์ / ผู้รับมอบกรรมสิทธิ์
                
                # Click = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/div/div/div')
                # Click.click()
                # time.sleep(0.5)
                # Click = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')
                # Click.click()
                
                time.sleep(1.5)
                Add = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="MuiBox-root mui-style-gig06g"]//button'))
                )
                assert Add.is_displayed(), 'Element is not displayed!'
                assert Add.is_enabled(), 'Element is not enabled!'
                Add.click()

                # กรอกเลขห้อง ชั้น/ห้อง

                key_text = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-adornedEnd MuiAutocomplete-inputRoot mui-style-s2ujxz"]//input'))
                )
                assert key_text.is_displayed(), 'Element is not displayed!'
                assert key_text.is_enabled(), 'Element is not enabled!'
                key_text.send_keys('01/03' + Keys.ARROW_DOWN + Keys.ENTER) 
                
                time.sleep(2)

                Add = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-disableElevation MuiButton-root MuiLoadingButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-disableElevation ex3plx0 mui-style-122ldvs"]'))
                )
                assert Add.is_displayed(), 'Element is not displayed!'
                assert Add.is_enabled(), 'Element is not enabled!'
                Add.click()

                time.sleep(2)

                key_text = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/div/input'))
                )
                assert key_text.is_displayed(), 'Element is not displayed!'
                assert key_text.is_enabled(), 'Element is not enabled!'
                key_text.send_keys('01/04' + Keys.ARROW_DOWN + Keys.ENTER)
                
                 # ลบห้อง

                # ห้อง 01/03

                # time.sleep(2)
                # Click_detele = WebDriverWait(self.driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/button'))
                # )
                # assert Click_detele.is_displayed(), 'Element is not displayed!'
                # assert Click_detele.is_enabled(), 'Element is not enabled!'
                # Click_detele.click()

                # ห้อง 01/04
                # time.sleep(1)

                # Click_detele = WebDriverWait(self.driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/button'))
                # )
                # assert Click_detele.is_displayed(), 'Element is not displayed!'
                # assert Click_detele.is_enabled(), 'Element is not enabled!'
                # Click_detele.click()
                
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 


                 # Save

                # Save = WebDriverWait(self.driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div[2]/button'))
                # )
                # assert Save.is_displayed(), 'Element is not displayed!'
                # assert Save.is_enabled(), 'Element is not enabled!'
                # actions = ActionChains(self.driver)
                # actions.move_to_element(Save).click().perform()

        except NoSuchElementException:
            self.fail('Element not Found')
        except AssertionError as e:
            self.fail(str(e))
        except Exception as o:
            self.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว')


    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()   

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\5.การประชุมลูกบ้าน\\Reports'))