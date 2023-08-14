# Pytest with POM

import pytest
from Test_Data import data
from Test_Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Test Suite

class Test_Anirudh:
    # Boot method to run Pytest using POM
    @pytest.fixture
    def startup(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    # login test with invalid username and valid password
    def test_invalid_login_attempt_1(self, startup):
        self.url = data.Data().url
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().invalid_username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().click_button).click()
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().invalid_login_msg).text
        assert msg == 'Invalid credentials'
        print('valid error message: ', msg)

    # login test with valid username and invalid password
    def test_invalid_login_attempt_2(self, startup):
        self.url = data.Data().url
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().invalid_password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().click_button).click()
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().invalid_login_msg).text
        assert msg == 'Invalid credentials'
        print('valid error message: ', msg)

    # login test with invalid username and invalid password
    def test_invalid_login_attempt_3(self, startup):
        self.url = data.Data().url
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().invalid_username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().invalid_password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().click_button).click()
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().invalid_login_msg).text
        assert msg == 'Invalid credentials'
        print('valid error message: ', msg)

    # test for successful login
    def test_login(self, startup):
        self.url = data.Data().url
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
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
        assert cookies_home_page != cookies_login
        print("The user is logged in successfully")

    # test for invalid login
    def test_invalid_login(self, startup):
        self.url = data.Data().url
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().invalid_password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().click_button).click()
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().invalid_login_msg).text
        assert msg == 'Invalid credentials'
        print('valid error message: ', msg)

    # test to add an employee and print the toast message
    def test_add_an_employee(self, startup):
        self.url = data.Data().url
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
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
        assert msg == 'Successfully Saved'
        print('message for successful employee addition: ', msg)

    # test to edit an employee and print the toast message
    def test_edit_an_employee(self, startup):
        self.url = data.Data().url
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().click_button).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().pim_element).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().edit_icon).click()
        self.driver.find_element(by=By.NAME, value='middleName').send_keys('bb')
        self.driver.find_element(by=By.XPATH, value=locators.Locators().save_button_edit).click()
        sleep(3)
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().update_success_msg).text
        assert msg == 'Successfully Updated'
        print('message for successful employee details addition: ', msg)

    # test to delete an employee and print the toast message
    def test_delete_an_employee(self, startup):
        self.url = data.Data().url
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().click_button).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().pim_element).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().delete_icon).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().delete_button).click()
        sleep(3)
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().delete_success_msg).text
        assert msg == 'Successfully Deleted'
        print('message for successful deletion: ', msg)
