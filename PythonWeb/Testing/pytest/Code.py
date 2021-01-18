from selenium import webdriver
import pytest
import time
# pytest -v -s --html=report.html --self-contained-html Login_Fun.py
class Login_Function():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome("E:\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()
    def tc1openLoginPage(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(1)
        assert self.driver.title=="EPU - Đăng Nhập"
    def tc2noInput(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        time.sleep(1)
        assert self.driver.title=="Taste.it - Home"
    def tc3onlyUsername(self,setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(1)
        self.driver.find_element_by_name("usernameLoginForm").send_keys("vietdd")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        time.sleep(1)
        assert self.driver.title=="Taste.it - Home"
    def tc4_onlyPassword(self,setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(1)
        self.driver.find_element_by_name("password").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        time.sleep(1)
        assert self.driver.title=="Taste.it - Home"
    def tc5_UsernamePasswordWrong(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(1)
        self.driver.find_element_by_name("usernameLoginForm").send_keys("vietdd123")
        self.driver.find_element_by_name("password").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        time.sleep(1)
        assert self.driver.title=="Taste.it - Home"
    def tc6_UsernameMore50value(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(1)
        self.driver.find_element_by_name("usernameLoginForm").send_keys("dinhdoanvietdinhdoanvietdinhdoanvietdinhdoanvietdinhdoanviet")
        self.driver.find_element_by_name("password").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        time.sleep(1)
        assert self.driver.title=="Taste.it - Home"
    def tc7_specialValueUsername(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(1)
        self.driver.find_element_by_name("usernameLoginForm").send_keys(":) :3 =))")
        self.driver.find_element_by_name("password").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        time.sleep(1)
        assert self.driver.title=="Taste.it - Home"
    def tc8_loginSuccessfull(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(1)
        self.driver.find_element_by_name("usernameLoginForm").send_keys("vietdd")
        self.driver.find_element_by_name("passwordLoginForm").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        assert self.driver.title=="Taste.it - Home"