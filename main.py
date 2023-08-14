from Test_Data import data
from Test_Locators import locators

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Anirudh:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def invalid_login_attempt_1(self):
        # invalid username and valid password
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().invalid_username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().click_button).click()
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().invalid_login_msg).text
        print('valid error message: ', msg)
        self.driver.quit()

    
    def invalid_login_attempt_2(self):
        # valid username and invalid password
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().invalid_password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().click_button).click()
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().invalid_login_msg).text
        print('valid error message: ', msg)
        self.driver.quit()

    def invalid_login_attempt_3(self):
        # invalid username and invalid password
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().invalid_username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().invalid_password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().click_button).click()
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().invalid_login_msg).text
        print('valid error message: ', msg)
        self.driver.quit()


    def login(self):
        # collecting cookie data before login i.e cookies on home page
        cookies_1 = self.driver.get_cookies()
        cookies_home_page = cookies_1[0]['value']
        print('Home page cookie : ', cookies_home_page)        
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().click_button).click()
        # collecting cookie data after login
        cookies_2 = self.driver.get_cookies()
        cookies_login = cookies_2[0]['value']
        print('Logged in Cookie : ', cookies_login)
        if cookies_home_page != cookies_login:
            print("The user is logged in successfully")
        self.driver.quit()


    def invalid_login(self):       
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().invalid_password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().click_button).click()
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().invalid_login_msg).text
        print('valid error message: ', msg)
        self.driver.quit()

    
    def add_an_employee(self):       
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().click_button).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().pim_element).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().add_button).click()
        self.driver.find_element(by=By.NAME, value='firstName').send_keys('a')
        self.driver.find_element(by=By.NAME, value='middleName').send_keys('b')
        self.driver.find_element(by=By.NAME, value='lastName').send_keys('c')
        self.driver.find_element(by=By.XPATH, value=locators.Locators().save_button).click()
        sleep(3)
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().save_sucess_msg).text
        print('message for successful employee addition: ', msg)
        self.driver.quit()


    def edit_an_employee(self):        
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().click_button).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().pim_element).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().edit_icon).click()
        self.driver.find_element(by=By.NAME, value='middleName').send_keys('bb')
        self.driver.find_element(by=By.XPATH, value=locators.Locators().save_button_edit).click()
        sleep(3)
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().update_success_msg).text
        print('message for successful employee details addition: ', msg)
        self.driver.quit()


    def delete_an_employee(self):        
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().click_button).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().pim_element).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().delete_icon).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().delete_button).click()
        sleep(3)
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().delete_success_msg).text
        print('message for successful deletion: ', msg)
        self.driver.quit()


anirudh = Anirudh(data.Data().url)
# anirudh.invalid_login_attempt_1()
# anirudh.invalid_login_attempt_2()
# anirudh.invalid_login_attempt_3()
# anirudh.login()
# anirudh.invalid_login()
# anirudh.add_an_employee()
# anirudh.edit_an_employee()
# anirudh.delete_an_employee()