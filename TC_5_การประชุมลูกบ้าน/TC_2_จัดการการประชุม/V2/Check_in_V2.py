
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



def page_check_in(driver):

                # เปิดหน้า จัดการประชุม
        try:
                driver.get('https://msm-smarty-cms-staging.hr-impact.co/agm/meetings')
                driver.implicitly_wait(30)

                check_in = WebDriverWait(driver, 30).until(
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

                key_text = WebDriverWait(driver, 30).until(
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
                
                time.sleep(2)
                Add = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="MuiBox-root mui-style-gig06g"]//button'))
                )
                assert Add.is_displayed(), 'Element is not displayed!'
                assert Add.is_enabled(), 'Element is not enabled!'
                Add.click()

                # กรอกเลขห้อง ชั้น/ห้อง

                key_text = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-adornedEnd MuiAutocomplete-inputRoot mui-style-s2ujxz"]//input'))
                )
                assert key_text.is_displayed(), 'Element is not displayed!'
                assert key_text.is_enabled(), 'Element is not enabled!'
                key_text.send_keys('01/03' + Keys.ARROW_DOWN + Keys.ENTER) 
                
                time.sleep(2)

                Add = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-disableElevation MuiButton-root MuiLoadingButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-disableElevation ex3plx0 mui-style-122ldvs"]'))
                )
                assert Add.is_displayed(), 'Element is not displayed!'
                assert Add.is_enabled(), 'Element is not enabled!'
                Add.click()

                time.sleep(2)

                key_text = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/div/input'))
                )
                assert key_text.is_displayed(), 'Element is not displayed!'
                assert key_text.is_enabled(), 'Element is not enabled!'
                key_text.send_keys('01/04' + Keys.ARROW_DOWN + Keys.ENTER)

                time.sleep(2)

                 # ลบห้อง

                # ห้อง 01/03

                # time.sleep(2)
                # Click_detele = WebDriverWait(driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/button'))
                # )
                # assert Click_detele.is_displayed(), 'Element is not displayed!'
                # assert Click_detele.is_enabled(), 'Element is not enabled!'
                # Click_detele.click()

                # ห้อง 01/04
                # time.sleep(1)

                # Click_detele = WebDriverWait(driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/button'))
                # )
                # assert Click_detele.is_displayed(), 'Element is not displayed!'
                # assert Click_detele.is_enabled(), 'Element is not enabled!'
                # Click_detele.click()
                
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
                time.sleep(1)

                 # Save

                # Save = WebDriverWait(driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div[2]/button'))
                # )
                # assert Save.is_displayed(), 'Element is not displayed!'
                # assert Save.is_enabled(), 'Element is not enabled!'
                # actions = ActionChains(driver)
                # actions.move_to_element(Save).click().perform()

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