from selenium import webdriver
import pytest
import time
# pytest -v -s --html=Login_Funtion_Report.html --self-contained-html Login_Fun.py
class TestLoginUser():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome("E:\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()
    def test_tc1_LoginPageTitle(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        assert self.driver.title=="EPU - Đăng Nhập"
    def test_tc2_noInput(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        time.sleep(2)
        assert self.driver.title=="EPU - Đăng Nhập"
    def test_tc3_onlyUsername(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(1)
        self.driver.find_element_by_name("usernameLoginForm").send_keys("vietdd")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        time.sleep(1)
        assert self.driver.title=="EPU - Đăng Nhập"
    def test_tc4_onlyPassword(self,setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(1)
        self.driver.find_element_by_name("passwordLoginForm").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        time.sleep(1)
        assert self.driver.title=="EPU - Đăng Nhập"
    def test_tc5_UsernamePasswordWrong(self,setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        self.driver.find_element_by_name("usernameLoginForm").send_keys("vietdd123")
        self.driver.find_element_by_name("passwordLoginForm").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        time.sleep(2)
        assert self.driver.title=="EPU - Đăng Nhập"
    def test_tc6_UsernameMore50value(self,setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        self.driver.find_element_by_name("usernameLoginForm").send_keys("dinhdoanvietdinhdoanvietdinhdoanvietdinhdoanvietdinhdoanviet")
        self.driver.find_element_by_name("passwordLoginForm").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        time.sleep(2)
        assert self.driver.title=="EPU - Đăng Nhập"
    def test_tc7_specialValueUsername(self,setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        self.driver.find_element_by_name("usernameLoginForm").send_keys(":) :3 =))")
        self.driver.find_element_by_name("passwordLoginForm").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        time.sleep(2)
        assert self.driver.title=="EPU - Đăng Nhập"
    def test_tc8_loginSuccessfull(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        self.driver.find_element_by_name("usernameLoginForm").send_keys("vietdd")
        self.driver.find_element_by_name("passwordLoginForm").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        time.sleep(2)
        assert self.driver.title=="Taste.it - Home"
