
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
import logging
from selenium.common.exceptions import NoSuchElementException



class WebTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(login):

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        login.driver = webdriver.Chrome(options=options)
        # login.driver = webdriver.Chrome()  # หรือใช้ webdriver.Firefox(), webdriver.Edge(), etc.
        login.driver.get('https://msm-smarty-cms-staging.hr-impact.co/login')
        login.driver.set_window_size(1920, 1000)
        login.driver.implicitly_wait(10)

    def test_page_title(self):
        driver = self.driver
        self.assertEqual(driver.title, 'Smarty msm | Account Receivable Report')  # ตรวจสอบว่า title ของหน้าเว็บถูกต้อง

    def test_Login_Smarty(self):
        time.sleep(1)
        driver = self.driver

        element = self.driver.find_element(By.XPATH, '//div[2]/div/div/div/div/div/div[1]/div/div[1]/p')
        expected_text = 'เบอร์โทรศัพท์ / รหัสพนักงาน'
        self.assertEqual(element.text, expected_text)
        time.sleep(0.1)
        search_box = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input')
        search_box.send_keys('00000')
        assert search_box.is_displayed(), "Element is not visible"

        textbox_element = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input")  
        textbox_value = textbox_element.get_attribute("value")
        text_to_check = "00000"
        self.assertIn(text_to_check, textbox_value, f"ไม่พบ '{text_to_check}' ในกล่องข้อความ")

        Click = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/button')  # ขอ OTP
        assert Click.is_displayed(), "Element is not visible"
        self.assertTrue(Click.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
        self.assertTrue(Click.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
        Click.click()  # คลิกขอ OTP


# รอให้ Element คลิกได้  # คลิกขอ เข้าสู่ระบบ
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/button')) # คลิกขอ เข้าสู่ระบบ
        )
        element.click()
# ทดสอบการคลิก Element
        result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/nav/div/div/div/ul/div[3]/li/div/div[2]')    
        self.assertIsNotNone(result_element)



    def test_function(self):
        # หน้า จัดการลูกหนี้  
        self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/report/accounts-receivable')
        self.driver.implicitly_wait(10)
        time.sleep(1)

# ใช้คำสั่ง print() หรือ logging เพื่อติดตามค่าต่าง ๆ และสถานะของโปรแกรมขณะทำงาน

        logging.basicConfig(level=logging.INFO)
        logging.info('This is an info message')
        time.sleep(0.1)

# คีย์ โครงการ
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div/div/input'))
        )
        element.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(0.1)


# คีย์ ห้อง ชั้น
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div/input'))
        )
        element.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(0.1)

# Search

        try:
                element = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div/div[4]/button")
                assert element.is_displayed(), "Element is not visible"  
                self.assertTrue(element.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
                self.assertTrue(element.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
                element.click()
        except NoSuchElementException:
                print("Element not found")
                time.sleep(0.1)

# Refresh

        try:
                element = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div/div[3]/button")
                assert element.is_displayed(), "Element is not visible"  
                self.assertTrue(element.is_displayed(),'ปุ่มไม่แสดงอยู่บนหน้า')
                self.assertTrue(element.is_enabled(), "ปุ่มไม่สามารถใช้งานได้")
                element.click()
        except NoSuchElementException:
                print("Element not found")
                time.sleep(0.1)

# รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
        element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[9]"))  
                        )
# หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
        print("โครงการขึ้น Show")
        time.sleep(0.1)


    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()   

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



