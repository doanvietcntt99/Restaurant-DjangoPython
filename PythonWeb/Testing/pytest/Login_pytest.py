from selenium import webdriver
import pytest
import time
# pytest -v -s --html=report.html --self-contained-html Login_pytest.py
class TestLoginUser():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome("E:\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()
    def test_LoginPageTitle(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        assert self.driver.title=="EPU - Đăng Nhập"
    def test_Login_User(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        self.driver.find_element_by_name("usernameLoginForm").send_keys("vietdd")
        self.driver.find_element_by_name("passwordLoginForm").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        assert self.driver.title=="Taste.it - Home"
    def test_Login_Admin(self, setup):
        self.driver.get("http://127.0.0.1:8000/admin/")
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("admin123")
        self.driver.find_element_by_xpath("//input[@value='Log in']").click()
        assert self.driver.title=="Site administration | Django site admin"
    def test_Order(self, setup):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element_by_name("nameBooking").send_keys("Đinh Doãn Việt")
        self.driver.find_element_by_name("emailBooking").send_keys("doanvietcntt99@gmail.com")
        self.driver.find_element_by_name("phoneBooking").send_keys("0965062715")
        self.driver.find_element_by_name("checkInBooking").send_keys("11/11/2020")
        self.driver.find_element_by_name("timeBooking").send_keys("0830SA")
        self.driver.find_element_by_name("numberOfGuest").send_keys("2")
        self.driver.find_element_by_name("pushOrder").click()
        assert self.driver.title=="Taste.it - Home"
    def test_Add_New_Food(self, setup):
        self.driver.get("http://127.0.0.1:8000/admin/home/food/add/")
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("admin123")
        self.driver.find_element_by_xpath("//input[@value='Log in']").click()
        self.driver.find_element_by_name("nameFood").send_keys("Bữa sáng 5")
        self.driver.find_element_by_name("ingredientFood").send_keys("Thịt ABC ZUA")
        self.driver.find_element_by_name("payFood").send_keys("200.000")
        self.driver.find_element_by_name("avatarFood").send_keys("C://Users/doanv/OneDrive/Máy tính/BCHLienChiDoan.jpg")
        self.driver.find_element_by_name("nameTypeFood").send_keys("BREAKFAST")
        self.driver.find_element_by_xpath('//*[@id="food_form"]/div/div/input[1]').click()
        assert self.driver.title == "Select food to change | Django site admin"
    def test_Update_UserDetail(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        self.driver.find_element_by_name("usernameLoginForm").send_keys("vietdd")
        self.driver.find_element_by_name("passwordLoginForm").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        self.driver.get("http://127.0.0.1:8000/accountdetail")
        time.sleep(2)
        self.driver.find_element_by_name("fullnameUser").clear()
        self.driver.find_element_by_name("fullnameUser").send_keys("Phạm Nam Phương")
        self.driver.find_element_by_name("dobUser").clear()
        self.driver.find_element_by_name("dobUser").send_keys("05/10/2020")
        self.driver.find_element_by_name("addressUSer").clear()
        self.driver.find_element_by_name("addressUSer").send_keys("Thanh Hóa")
        self.driver.find_element_by_name("emailUser").clear()
        self.driver.find_element_by_name("emailUser").send_keys("phuongpn@gmail.com")
        self.driver.find_element_by_name("phoneUser").clear()
        self.driver.find_element_by_name("phoneUser").send_keys("0986678636")
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/form/div/input[2]").click()
        assert self.driver.title == "Taste.it - Home"
    def test_Reset_UserDetail(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        self.driver.find_element_by_name("usernameLoginForm").send_keys("vietdd")
        self.driver.find_element_by_name("passwordLoginForm").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        self.driver.get("http://127.0.0.1:8000/accountdetail")
        time.sleep(2)
        self.driver.find_element_by_name("fullnameUser").clear()
        self.driver.find_element_by_name("fullnameUser").send_keys("Phạm Nam Phương")
        self.driver.find_element_by_name("dobUser").clear()
        self.driver.find_element_by_name("dobUser").send_keys("05/10/2020")
        self.driver.find_element_by_name("addressUSer").clear()
        self.driver.find_element_by_name("addressUSer").send_keys("Thanh Hóa")
        self.driver.find_element_by_name("emailUser").clear()
        self.driver.find_element_by_name("emailUser").send_keys("phuongpn@gmail.com")
        self.driver.find_element_by_name("phoneUser").clear()
        self.driver.find_element_by_name("phoneUser").send_keys("0986678636")
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/form/div/input[1]").click()
        assert self.driver.title == "Taste.it - Home"
    def test_Comment_Blog(self, setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        self.driver.find_element_by_name("usernameLoginForm").send_keys("vietdd")
        self.driver.find_element_by_name("passwordLoginForm").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        self.driver.get("http://127.0.0.1:8000/blog/2/")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="id_body"]').send_keys("Test CMT 1")
        self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div[1]/div[2]/form/input[2]').click()
        assert self.driver.title == "Taste.it - Blog Title"
    def test_Register_User(self, setup):
        self.driver.get("http://127.0.0.1:8000/register/")
        time.sleep(2)
        self.driver.find_element_by_name("usernameUser").send_keys("thususu123")
        self.driver.find_element_by_name("passwordUser").send_keys("admin123")
        self.driver.find_element_by_name("rePasswordUser").send_keys("admin123")
        self.driver.find_element_by_name("fullnameUser").send_keys("Nguyễn Thị Thu")
        self.driver.find_element_by_name("phoneUser").send_keys("090216408")
        self.driver.find_element_by_name("emailUser").send_keys("thususu@gmail.com")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        self.driver.get("http://127.0.0.1:8000/login/")
        time.sleep(2)
        self.driver.find_element_by_name("usernameLoginForm").send_keys("thususu123")
        self.driver.find_element_by_name("passwordLoginForm").send_keys("admin123")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input[3]').click()
        assert self.driver.title=="Taste.it - Home"
    def test_Add_New_Master_Chefs(self, setup):
        self.driver.get("http://127.0.0.1:8000/admin/home/masterchef/add/")
        time.sleep(2)
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("admin123")
        self.driver.find_element_by_xpath("//input[@value='Log in']").click()
        self.driver.find_element_by_name("nameChef").send_keys("Đầu Bếp 5")
        self.driver.find_element_by_name("positionChef").send_keys("BẾP TRƯỞNG")
        self.driver.find_element_by_name("selfIntroduceChef").send_keys("Tôi là Đầu Bếp 5")
        self.driver.find_element_by_name("avatarChef").send_keys("C://Users/doanv/OneDrive/Máy tính/BichMT.jpg")
        self.driver.find_element_by_xpath('//*[@id="masterchef_form"]/div/div/input[1]').click()
        assert self.driver.title=="Select master chef to change | Django site admin"
    def test_Add_New_Blogs(self, setup):
        self.driver.get("http://127.0.0.1:8000/admin/home/blog/add/")
        time.sleep(2)
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("admin123")
        self.driver.find_element_by_xpath("//input[@value='Log in']").click()
        self.driver.find_element_by_name("nameBlog").send_keys("Blog 8")
        self.driver.find_element_by_name("posterBlog").send_keys("admin")
        self.driver.find_element_by_name("titleBlog").send_keys("Title Blog 8")
        self.driver.find_element_by_name("contentBlog").send_keys("Đây là content Blog 8")
        self.driver.find_element_by_name("avatarBlog").send_keys("C://Users/doanv/OneDrive/Máy tính/BichMT.jpg")
        self.driver.find_element_by_xpath('//*[@id="blog_form"]/div/div/input[1]').click()
        assert self.driver.title=="Select blog to change | Django site admin"