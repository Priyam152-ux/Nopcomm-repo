from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    email_textbox_xpath = '//*[@id="Email"]'
    password_textbox_xpath = '//*[@id="Password"]'
    login_button_xpath = '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button'
    logout_button_xpath = '//*[@id="navbarText"]/ul/li[3]/a'

    def __int__(self, driver):
        self.driver = webdriver.Chrome()

    def setEmailId(self, EmailId):
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).send_keys(EmailId)

    def setPassword(self, Password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(Password)

    def clickLoginbtn(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def clickLogoutbtn(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()
