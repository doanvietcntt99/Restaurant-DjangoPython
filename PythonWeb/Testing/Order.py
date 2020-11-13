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
    nameBooking = driver.find_element_by_name("nameBooking")
    print('nameBooking : ')
    viewAtritue(nameBooking)
    nameBooking.send_keys("Đinh Doãn Việt")
    emailBooking = driver.find_element_by_name("emailBooking")
    print('emailBooking : ')
    viewAtritue(emailBooking)
    emailBooking.send_keys("doanvietcntt99@gmail.com")
    phoneBooking = driver.find_element_by_name("phoneBooking")
    print('phoneBooking : ')
    viewAtritue(phoneBooking)
    phoneBooking.send_keys("0965062715")
    checkInBooking = driver.find_element_by_name("checkInBooking")
    print('checkInBooking : ')
    viewAtritue(checkInBooking)
    checkInBooking.send_keys("11/11/2020")
    timeBooking = driver.find_element_by_name("timeBooking")
    print('timeBooking : ')
    viewAtritue(timeBooking)
    timeBooking.send_keys("0830SA")
    numberOfGuest = driver.find_element_by_name("numberOfGuest")
    print('numberOfGuest : ')
    viewAtritue(numberOfGuest)
    numberOfGuest.send_keys("2")    
    buttonSummit = driver.find_element_by_name("pushOrder")
    buttonSummit.click()
    driver.refresh()
    driver.get("http://127.0.0.1:8000/admin/")
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
    LinkBookings = driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[2]/th/a')
    LinkBookings.click()
except:
    print("Có lỗi xảy ra!")
time.sleep(30)
driver.quit()