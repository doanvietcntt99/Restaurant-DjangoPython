from selenium import webdriver
from seleniumrequests import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
import time
def viewAtritue(self):
    print('     - Atritute : ', self)
    print('     - Displayed  : ', self.is_displayed())
    print('     - Enabled  : ', self.is_enabled())
    print('     - Selected  :', self.is_selected())
PATH = "E:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://127.0.0.1:8000/")
assert 'Home' in driver.title
print(driver.title)
print(driver.current_url)
#Test với Form đăng ký
try:
    driver.get("http://127.0.0.1:8000/admin/home/food/add/")
    username = driver.find_element_by_name("username")
    print('username : ')
    viewAtritue(username)
    username.send_keys("admin")
    password = driver.find_element_by_name("password")
    print('password : ')
    viewAtritue(password)
    password.send_keys("admin123")
    loginButton = driver.find_element_by_xpath("//input[@value='Log in']")
    print('loginButton : ')
    viewAtritue(loginButton)
    loginButton.click()
    # AddFoodLink = driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[4]/td[1]/a')
    # print('AddFoodLink : ')
    # viewAtritue(AddFoodLink)
    # AddFoodLink.click()
    nameFood = driver.find_element_by_name("nameFood")
    print('nameFood : ')
    viewAtritue(nameFood)
    nameFood.send_keys("Bữa sáng 5")
    ingredientFood = driver.find_element_by_name("ingredientFood")
    print('ingredientFood : ')
    viewAtritue(ingredientFood)
    ingredientFood.send_keys("Thịt ABC ZUA")
    payFood = driver.find_element_by_name("payFood")
    print('payFood : ')
    viewAtritue(payFood)
    payFood.send_keys("200.000")
    avatarFood = driver.find_element_by_name("avatarFood")
    print('avatarFood : ')
    viewAtritue(avatarFood)
    avatarFood.send_keys("C://Users/doanv/OneDrive/Máy tính/BCHLienChiDoan.jpg")
    nameTypeFood = driver.find_element_by_name("nameTypeFood")
    print('nameTypeFood : ')
    viewAtritue(nameTypeFood)
    nameTypeFood.send_keys("BREAKFAST")
    buttonSave = driver.find_element_by_xpath('//*[@id="food_form"]/div/div/input[1]')
    buttonSave.click()
except:
    print("Có lỗi xảy ra!")
time.sleep(30)
driver.quit()