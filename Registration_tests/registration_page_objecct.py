from selenium.webdriver.common.by import By


class Registration_page:
    account_page_xpath = "(//a[normalize-space()='Account'])[1]"
    email_xpath = "(//input[@id='reg_email'])[1]"
    password_xpath = "(//input[@id='reg_password'])[1]"
    register_btn_xpath = "(//input[@name='register'])[1]"
    confirmation_for_registration_xpath = "(//h1[normalize-space()='My account'])[1]"
    email_error_message_xpath = "//div[@class='site-content']//li[1]"
    password_error_message_xpath = "//div[@class='site-content']//li[1]"
    weak_password_error_msg_xpath = "//div[@class='woocommerce-password-strength short']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnAccount(self):
        self.driver.find_element(By.XPATH, self.account_page_xpath).click()

    def setEmail(self, email):
        email_textbox = self.driver.find_element(By.XPATH, self.email_xpath)
        email_textbox.clear()
        email_textbox.send_keys(email)

    def setPassword(self, password):
        password_textbox = self.driver.find_element(By.XPATH, self.password_xpath)
        password_textbox.clear()
        password_textbox.send_keys(password)

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.register_btn_xpath).click()

    def emailErrorMessage(self):
        return self.driver.find_element(By.XPATH, self.email_error_message_xpath).text

    def passwordErrorMessage(self):
        return self.driver.find_element(By.XPATH, self.password_error_message_xpath).text

    def confirmationMessage(self):
        return self.driver.find_element(By.XPATH, self.confirmation_for_registration_xpath).text

    def weakPasswordErrorMsg(self):
        return self.driver.find_element(By.XPATH, self.weak_password_error_msg_xpath).text
