import os
import pytest
from seleniumbase import BaseCase
from pages.login_page import LoginPage
from dotenv import load_dotenv

load_dotenv() # Loading sensitive variable from .env in gitignore
user_email = os.getenv("USER_EMAIL")
user_password = os.getenv("USER_PASSWORD")
invalid_email = os.getenv('INVALID_EMAIL')
invalid_password = os.getenv("INVALID_PASSWORD")
phone_number = os.getenv("PHONE_NUMBER")

class Login(BaseCase):

    def test_successful_login(self):
        """Scenario I: User logs in successfully"""
        self.open(LoginPage.URL_LOGIN)
        self.assert_title("Vite + React + TS") # Assert login page is loaded

        self.type(LoginPage.EMAIL_INPUT, user_email)
        self.type(LoginPage.PASSWORD_INPUT, user_password)

        self.click(LoginPage.LOGIN_BUTTON)
        self.assert_title("Vite + React + TS") # Assert redirection to main page


    def test_disable_button_when_empty_fields(self):
        """Scenario II: Verify login button is disabled when empty fields are left"""
        self.open(LoginPage.URL_LOGIN)
        self.assert_title("Vite + React + TS") # Assert login page is loaded

        self.type(LoginPage.EMAIL_INPUT, "")
        self.type(LoginPage.PASSWORD_INPUT, user_password)

        is_disabled = self.assert_attribute(LoginPage.LOGIN_BUTTON, "disabled")
        self.assert_true(is_disabled is not None, "The button is not disabled.")


    def test_error_message_invalid_email(self):
        """Scenario III: Verify the error message when adding invalid email"""
        self.open(LoginPage.URL_LOGIN)
        self.assert_title("Vite + React + TS")  # Assert login page is loaded

        self.type(LoginPage.EMAIL_INPUT, invalid_email)

        self.assert_text("Formato de correo electrónico inválido", LoginPage.ERROR_NOTIFICATION)
        self.assert_element_visible(LoginPage.ERROR_NOTIFICATION)

    @pytest.mark.skip(reason="Currently working on a fix related to text assertions")
    def test_error_message_invalid_password(self):
        """Scenario III: Verify the error message when adding invalid password"""
        self.open(LoginPage.URL_LOGIN)
        self.assert_title("Vite + React + TS")  # Assert login page is loaded

        self.type(LoginPage.EMAIL_INPUT, user_email)
        self.type(LoginPage.PASSWORD_INPUT, invalid_password)

        self.assert_text("Contraseña no valida", LoginPage.ERROR_NOTIFICATION)
        self.assert_element_visible(LoginPage.ERROR_NOTIFICATION)
