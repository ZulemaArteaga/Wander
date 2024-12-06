import os
from seleniumbase import BaseCase
from pages.register_page import RegisterPage
from dotenv import load_dotenv

from tests.test_login import phone_number

load_dotenv()
name = os.getenv("NAME")
user_email = os.getenv("USER_EMAIL")
user_password = os.getenv("USER_PASSWORD")
confirm_password = os.getenv("CONFIRM_PASSWORD")

class Register(BaseCase):

    def test_register(self):
        self.open(RegisterPage.URL_REGISTER)
        self.assert_title("Vite + React + TS") # Assert login page is loaded

        self.type(RegisterPage.NAME, name)
        self.type(RegisterPage.EMAIL_INPUT, user_email)
        self.type(RegisterPage.PASSWORD_INPUT, user_password)
        self.type(RegisterPage.CONFIRM_PASSWORD, user_password)

        phone_code_options = self.find_elements(RegisterPage.PHONE_PREFIX_OPTION)
        for option in phone_code_options:
            if "+1" in option.text:
                option.click()
                break

        self.type(RegisterPage.PHONE_NUMBER, phone_number)
        self.select_option_by_text(RegisterPage.TOURIST_OR_PROVIDER ,"Proveedor")
        self.click(RegisterPage.SELECT_ADULT)
        self.click(RegisterPage.REGISTER_BUTTON)

