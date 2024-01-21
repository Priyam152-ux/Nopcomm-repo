import webbrowser
from Objectrepository.LoginPage import Login
from selenium import webdriver


class TestLogin:
    baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    EmailId = "admin@yourstore.com"
    Password = "admin"

    def setup_method(self):
        # Create a WebDriver instance (e.g., Chrome)
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)

    def teardown_method(self):
        # Close the WebDriver after the test
        self.driver.quit()

    def test_homepage_title(self):
        act_title = self.driver.title
        assert act_title == "Your store. Login"

    def test_login(self):
        self.lp = Login()
        self.lp.setEmailId(self.EmailId)
        self.lp.setPassword(self.Password)
        self.lp.clickLoginbtn()
        act_title2 = self.driver.title
        assert act_title2 == "Dashboard / nopCommerce administration"


test_login = TestLogin()
test_login.setup_method()
test_login.test_homepage_title()
test_login.test_login()
