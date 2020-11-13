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
driver.get("http://127.0.0.1:8000/login/")
time.sleep(2)
try:
    taikhoan = driver.find_element_by_name("usernameLoginForm")
    print('Atritute Username: ', taikhoan)
    print('Displayed Username: ', taikhoan.is_displayed())
    print('Enabled Username: ',taikhoan.is_enabled())
    matkhau = driver.find_element_by_name("passwordLoginForm")
    print('Atritute Password: ', matkhau)
    print('Displayed Password: ', matkhau.is_displayed())
    print('Enabled Password: ',matkhau.is_enabled())
    taikhoan.send_keys("vietdd")
    matkhau.send_keys("admin123")
    loginButton = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]')
    loginButton.click()
    # driver.get("http://127.0.0.1:8000/accountdetail")
except:
    print("Có lỗi xảy ra!")
time.sleep(30)
driver.quit()