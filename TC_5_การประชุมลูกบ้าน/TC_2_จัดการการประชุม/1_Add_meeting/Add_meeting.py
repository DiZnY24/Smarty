
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys 
import traceback

# เว็ปไซต์จะไม่ปิดลง
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# รหัสเข้าหน้า WebSite
password = "00000"

# driver = webdriver.Chrome()
driver.set_window_size(1920, 1000)
driver.get('https://msm-smarty-cms-staging.hr-impact.co/login')
time.sleep(1)
print("Open Smaert")     

# Loop
for i in range(10):
            try:
                print("wait a moment")
                time.sleep(1)
                email = driver.find_element(By.XPATH, '//*[@id=":R3ajalakmn6:"]').send_keys(password)  
                print("break")
                break
            except:
                pass 
# time.sleep(2)

# Click login
for k in range(10):
            try:
                print("wait a moment")
                time.sleep(1)
                OTP = driver.find_element(By.XPATH, '//*[@id=":Rnalakmn6:"]')
                OTP.click() 
                print("break")
                break
            except:
                pass 
                    
# Click 2 
for s in range(10):
            try:
                print("wait a moment")
                time.sleep(1)
                login = driver.find_element(By.XPATH, '//*[@id=":Rnalakmn6:"]')
                login.click() 
                print("break")
                break
            except:
                pass                           
time.sleep(2)

# หน้า จัดการขนส่งพัสดุ

driver.get('https://msm-smarty-cms-staging.hr-impact.co/agm/meetings')
time.sleep(3) 
print("Open Page จัดการการประชุม pass")

for i in range(10):
    try:    
        # กดเพิ่มจัดประชุม
        print("รอสักครู่")
        time.sleep(1)
        Add_Button = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[1]/button')
        Add_Button.click()
        print("Click_Add pass")
        break
    except:
        pass

time.sleep(2)

for so in range(10):
    try:
        # คลิกโครงการ
        time.sleep(1)
        print("รอสักครู่")
        Click = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div')
        Click.click()
        print('Click pass')
        break
    except:
        pass

time.sleep(1)

for s in range(10):
    try:
        # ตีย์กรอก อาคาร C1 
        # time.sleep(1)
        print("รอสักครู่")
        Add_project = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/input')
        Add_project.send_keys('อาคาร C1' + Keys.ARROW_DOWN + Keys.ENTER) 
        print('กรอกสำเร็จ pass')
        break
    except:
        pass

# time.sleep(1)

for s in range(10):
    try:
        # กรอกช่อง ประจำปี
        time.sleep(1)
        print("รอสักครู่")
        # คลิก ประจำปี
        Click = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/input')
        Click.click()
        print('Click pass')

        # time.sleep(1)
        print("รอสักครู่")
        # คีย์ 
        Add_project = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/input')
        Add_project.send_keys('2567' + Keys.ARROW_DOWN + Keys.ENTER) 
        print('Key: 2567 pass') 
        break
    except:     
        pass

# time.sleep(1)

for so in range(10):
    try:    
        # คีย์ ชื่อการประชุม

        # คลิกชื่อประชุม
        time.sleep(1)
        Click = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[3]/div/div/div/div[2]/div/div')
        Click.click()

        # time.sleep(1)
        print("รอสักครู่")
        # ชื่อประชุม
        Key_name = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[2]/div[3]/div/div/div/div[2]/div/div/input')
        Key_name.send_keys('Test_kub')
        print('Key: Test_kub  pass')

        # time.sleep(1)
        print("รอสักครู่")
        # ครั้งที่
        Key_num = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[3]/div[1]/div/div[2]/div/div/input')
        Key_num.send_keys('1')
        print('Key: 1 pass')
        break
    except:
        pass

for mo in range(10):
    try:    
        # คีย์ วันและเวลาที่จัดประชุม

        # คลิก วันและเวลาที่จัดประชุม
        time.sleep(1)
        Click = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div/form/div/div[1]/div[3]/div[2]/div/div/div/button')
        Click.click()

        # time.sleep(1)
        print("รอสักครู่")
        # เลือกวันที่
        Click_date = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[5]/button[6]')
        Click_date.click()
        print('Click pass')

        break
    except:
        pass   

time.sleep(1)
print("รอสักครู่")
# คลิกกรอบเวลา
Click_Time = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[2]/ul[1]')
Click_Time.click()
time.sleep(1)
# Click_Time.send_keys(Keys.ENTER)
print('Click Time pass')
time.sleep(1)
# คลิกเลือกเวลา ตี 02
Click_Time = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[2]/ul[1]/li[3]')
Click_Time.click()
time.sleep(1)
# Click_Time.send_keys(Keys.ENTER)
print('Click Time : 02 pass')

for sx in range(10):
    try:
        # กรอกช่อง สถานที่ประชุม
        time.sleep(1)
        print("รอสักครู่")
        # คลิก สถานที่ประชุม
        Click = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[3]/div[3]/div/div[2]/div/div/input')
        Click.click()
        print('Click pass')

        # time.sleep(1)
        print("รอสักครู่")
        # คีย์ 
        Add_project = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div/form/div/div[1]/div[3]/div[3]/div/div[2]/div/div/input')
        Add_project.send_keys('Impact') 
        print('Key: Impact pass') 
        break
    except:     
        pass
print('Test Case the End')
time.sleep(5)
driver.close()