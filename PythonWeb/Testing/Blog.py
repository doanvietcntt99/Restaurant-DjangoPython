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
# try:
taikhoan = driver.find_element_by_name("usernameLoginForm")
print('taikhoan : ')
viewAtritue(taikhoan)
matkhau = driver.find_element_by_name("passwordLoginForm")
print('matkhau : ')
viewAtritue(matkhau)
taikhoan.send_keys("vietdd")
matkhau.send_keys("admin123")
loginButton = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]')
print('loginButton : ')
viewAtritue(loginButton)
loginButton.click()
driver.get("http://127.0.0.1:8000/blog/2/")
print(driver.title)
textAreaComment = driver.find_element_by_xpath('//*[@id="id_body"]')
textAreaComment.send_keys("Test CMT 1")
buttonComment = driver.find_element_by_xpath('/html/body/section[2]/div/div/div[1]/div[2]/form/input[2]')
buttonComment.click()
# except:
#     print("Có lỗi xảy ra!")
time.sleep(30)
driver.quit()