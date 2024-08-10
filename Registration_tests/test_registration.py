import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Registration_tests.registration_page_objecct import Registration_page


class Test_registration:

    @pytest.mark.registration
    def test_registration_with_valid_credentials(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://skleptest.pl/my-account/")
        self.registration = Registration_page(self.driver)
        self.registration.clickOnAccount()
        self.registration.setEmail("test123@gmail.com")
        self.registration.setPassword("test5555testing")
        self.registration.clickRegister()

        self.actual_message = self.registration.confirmationMessage()
        assert self.actual_message == "MY ACCOUNT"
        self.driver.quit()

    @pytest.mark.registration
    def test_negative_registration_with_missing_email(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://skleptest.pl/my-account/")
        self.registration = Registration_page(self.driver)
        self.registration.clickOnAccount()
        self.registration.setPassword("test5555./")
        self.registration.clickRegister()

        self.actual_message = self.registration.emailErrorMessage()
        assert self.actual_message == "Error: Please provide a valid email address."
        self.driver.quit()

    @pytest.mark.registration
    def test_negative_registration_with_missing_password(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://skleptest.pl/my-account/")
        self.registration = Registration_page(self.driver)
        self.registration.clickOnAccount()
        self.registration.setEmail("test123@gmail.com")
        self.registration.clickRegister()

        self.actual_message = self.registration.passwordErrorMessage()
        assert self.actual_message == "Error: Please enter an account password."
        self.driver.quit()

    @pytest.mark.registration
    def test_existing_email_address(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://skleptest.pl/my-account/")
        self.registration = Registration_page(self.driver)
        self.registration.clickOnAccount()
        self.registration.setEmail("test123@gmail.com")
        self.registration.setPassword("test5555testing")
        self.registration.clickRegister()
        # this test case should not pass as the application cannot register the same email.

    @pytest.mark.registration
    def test_weak_password(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://skleptest.pl/my-account/")
        self.registration = Registration_page(self.driver)
        self.registration.clickOnAccount()
        self.registration.setEmail("test123@gmail.com")
        self.registration.setPassword("abc")
        self.registration.clickRegister()

        self.actual_message = self.registration.weakPasswordErrorMsg()
        assert self.actual_message == "Very weak - Please enter a stronger password."
        self.driver.quit()

