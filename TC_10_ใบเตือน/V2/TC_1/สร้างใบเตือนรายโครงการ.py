
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
from  selenium.common.exceptions import NoSuchElementException,TimeoutException



def test_page_create_warning(driver):
        
    try:
# หน้า การบริหาร - ผู้ใช้งาน
        driver.get('https://msm-smarty-cms-staging.hr-impact.co/warning')
        driver.implicitly_wait(20)

# สร้างใบเตือน - รายบุคคล  

        create_warning = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div/div[1]/div[1]/div/button[1]'))
            )
        assert create_warning.is_displayed(), 'Element is not displayed!'
        assert create_warning.is_enabled(), 'Element is not enabled!'
        create_warning.click() 
        time.sleep(0.1) 

# สร้างใบเตือนรายบุคคล

        create_warning = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]'))
            )
        assert create_warning.is_displayed(), 'Element is not displayed!'
        assert create_warning.is_enabled(), 'Element is not enabled!'
        create_warning.click() 
        time.sleep(0.1) 

        element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/form/div/div[2]/div/div/div/div/div"))
        )
        print("รอคีย์โครงการ")
        time.sleep(0.1)

# โครงการ

        project = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[2]/div/div/div/div/div/input'))
            )
        assert project.is_displayed(), 'Element is not displayed!'
        assert project.is_enabled(), 'Element is not enabled!'
        project.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(0.1)

        Esc = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[2]/div/div/div/div/div/input')
        Esc.send_keys(Keys.ESCAPE)

# วันครบกำหนดชำระ

        date_buy = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[3]/div[1]/div/div/div'))
        )
        assert date_buy.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
        assert date_buy.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
        date_buy.click()
        time.sleep(0.1)

        date_buy = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[3]'))
        )
        assert date_buy.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
        assert date_buy.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
        date_buy.click()
        time.sleep(0.1)

# วันที่ครบกำหนดชำระ

        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[3]/div[2]/div/div/div'))
        )
        assert button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
        assert button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
        button.click()
        time.sleep(0.1)

        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[5]/button[3]'))
        )
        assert button.is_displayed(), "ปุ่มไม่แสดงอยู่บนหน้า"
        assert button.is_enabled(), "ปุ่มไม่สามารถใช้งานได้"
        button.click()
        time.sleep(0.1)

# หมายเหตุ

        key_text = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[4]/div[1]/div/div[2]/div/div/input'))
            )
        assert key_text.is_displayed(), 'Element is not displayed!'
        assert key_text.is_enabled(), 'Element is not enabled!'
        key_text.send_keys('Test') 
        time.sleep(0.1)

# รหัสผ่านเพื่อทำรายการ

        element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/form/div/div[4]/div[1]/div/div[2]/div/div/input"))
        )
        print("รอคีย์ Password")
        time.sleep(0.1)

        key_password = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[5]/div[1]/div/div[2]/div/div/input'))
        )
        assert key_password.is_displayed(), 'Element is not displayed!'
        assert key_password.is_enabled(), 'Element is not enabled!'
        key_password.send_keys('00000')
        time.sleep(2)

# ยกเลิก

        cancel = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[1]/div[2]/div/button[1]'))
        )
        assert cancel.is_displayed(), 'Element is not displayed!'
        assert cancel.is_enabled(), 'Element is not enabled!'
        cancel.click()
        time.sleep(0.1)

# Save

        # Save = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div/div[1]/div[2]/div/button[2]'))
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
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



