
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



def test_page_search_edit(driver):
        
    try:
        # หน้า จัดการลูกหนี้
        driver.get('https://msm-smarty-cms-staging.hr-impact.co/warning')
        driver.implicitly_wait(10)

# คีย์ โครงการ

        project = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
        )
        assert project.is_displayed(), 'Element is not displayed!'
        assert project.is_enabled(), 'Element is not enabled!'
        project.send_keys('อาคาร C1' + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(0.1)

# คีย์ ชั้น / ห้อง

        floor_room = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/input'))
        )
        assert floor_room.is_displayed(), 'Element is not displayed!'
        assert floor_room.is_enabled(), 'Element is not enabled!'
        floor_room.send_keys('15/59' + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(0.1)

# วันที่ วันที่ออกเอกสาร

        Date = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div/div[3]/div[1]/div/div/div'))
            )
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

        Date = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/button[3]'))
            )
        assert Date.is_displayed(), 'Element is not displayed!'
        assert Date.is_enabled(), 'Element is not enabled!'
        Date.click()
        time.sleep(0.1)

# สถานะ

        status = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div/div'))
            )
        assert status.is_displayed(), 'Element is not displayed!'
        assert status.is_enabled(), 'Element is not enabled!'
        status.click()
        time.sleep(0.1)

        status = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
            )
        assert status.is_displayed(), 'Element is not displayed!'
        assert status.is_enabled(), 'Element is not enabled!'
        status.click()
        time.sleep(0.1)

# Refresh

        Refresh = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div/div[4]/div/button'))
            )
        assert Refresh.is_displayed(), 'Element is not displayed!'
        assert Refresh.is_enabled(), 'Element is not enabled!'
        Refresh.click()
        time.sleep(0.1)


        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]")) 
        )
        print("รอเลขที่เอกสาร Show ")
        time.sleep(0.1) 

# สถานะ

        status = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[7]/div/div/button'))
            )
        assert status.is_displayed(), 'Element is not displayed!'
        assert status.is_enabled(), 'Element is not enabled!'
        status.click()
        time.sleep(0.1)

# พิมพ์ PDF

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]")) 
        )
        print("รอ พิมพ์ PDF")
        time.sleep(0.1) 

        status = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))
            )
        assert status.is_displayed(), 'Element is not displayed!'
        assert status.is_enabled(), 'Element is not enabled!'
        status.click()
        time.sleep(3)

# ยกเลิกใบเตือน

        # cancel = WebDriverWait(driver, 30).until(
        #         EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]'))
        #     )
        # assert cancel.is_displayed(), 'Element is not displayed!'
        # assert cancel.is_enabled(), 'Element is not enabled!'
        # cancel.click()
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



