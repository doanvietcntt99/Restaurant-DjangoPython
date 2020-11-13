from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
def viewAtritue(self):
    print('     - Atritute : ', self)
    print('     - Displayed  : ', self.is_displayed())
    print('     - Enabled  : ', self.is_enabled())
    print('     - Selected  :', self.is_selected())
PATH = "E:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://127.0.0.1:8000/register/")
time.sleep(2)
# try:
taikhoan = driver.find_element_by_name("usernameUser")
matkhau = driver.find_element_by_name("passwordUser")
rematkhau = driver.find_element_by_name("rePasswordUser")
hoTen = driver.find_element_by_name("fullnameUser")
phone = driver.find_element_by_name("phoneUser")
email = driver.find_element_by_name("emailUser")
taikhoan.send_keys("thususu2")
matkhau.send_keys("admin123")
rematkhau.send_keys("admin123")
hoTen.send_keys("Nguyễn Thị Thu")
phone.send_keys("090216408")
email.send_keys("thususu@gmail.com")
driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
driver.clear()
taikhoan = driver.find_element_by_name("usernameLoginForm")
matkhau = driver.find_element_by_name("passwordLoginForm")
taikhoan.send_keys("thususu")
matkhau.send_keys("admin123")
loginButton = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]')
loginButton.click()
# except:
#     print("Có lỗi xảy ra!")
time.sleep(30)
driver.quit()