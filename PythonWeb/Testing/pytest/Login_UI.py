from selenium import webdriver
import pytest
import time
def viewAtritue(self):
    print('     - Atritute : ', self)
    print('     - Displayed  : ', self.is_displayed())
    print('     - Enabled  : ', self.is_enabled())
    print('     - Selected  :', self.is_selected())
# pytest -v -s --html=Login_UI_Report.html --self-contained-html Login_UI.py
class TestLoginUser():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome("E:\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()
    def test_tc1_CheckButton_is_displayed(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        loginButton = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]')
        viewAtritue(loginButton)
        assert loginButton.is_displayed() == True 
    def test_tc1_CheckButton_is_enabled(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        loginButton = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]')
        viewAtritue(loginButton)
        assert loginButton.is_enabled() == True 
    def test_tc2_checkLink(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        Link = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/a')
        viewAtritue(Link)
        assert Link.is_enabled() == True
    def test_tc3_font(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        WelcomeTitle = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/h2')
        print(WelcomeTitle.get_attribute("text-transform"))
        assert WelcomeTitle.is_enabled() == True
    def test_tc6_placeholderUsername (self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        PlaceHolder = self.driver.find_element_by_xpath('//*[@id="id_usernameLoginForm"]').get_attribute("placeholder")
        assert PlaceHolder == 'Username'
    def test_tc6_placeholderPassword(self,setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        PlaceHolder = self.driver.find_element_by_xpath('//*[@id="id_passwordLoginForm"]').get_attribute("placeholder")
        assert PlaceHolder == 'Password'
    def test_tc8_iconTab(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        iconTab = self.driver.find_element_by_xpath('/html/body/link[4]')
        viewAtritue(iconTab)
        assert iconTab.is_displayed() == True 
