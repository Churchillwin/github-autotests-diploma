from __future__ import annotations

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from config.settings import Settings
from config.urls import LOGIN_URL
from pages.base_page import BasePage, Locator


class LoginPage(BasePage):
    """GitHub login page."""

    _LOGIN_INPUT: Locator = (By.ID, "login_field")
    _PASSWORD_INPUT: Locator = (By.ID, "password")
    _SUBMIT_BUTTON: Locator = (By.NAME, "commit")


    _USER_MENU_CANDIDATES: tuple[Locator, ...] = (
        (By.CSS_SELECTOR, "button[data-testid='user-menu-button']"),
        (By.CSS_SELECTOR, "summary[aria-label='View profile and more']"),
        (By.CSS_SELECTOR, "summary[aria-label*='account menu']"),
        (By.CSS_SELECTOR, "summary[data-ga-click*='show menu']"),
        (By.CSS_SELECTOR, "summary.Header-link[role='button']"),  
    )

    
    _SIGN_OUT_CANDIDATES: tuple[Locator, ...] = (
        (By.XPATH, "//button[normalize-space()='Sign out']"),
        (By.XPATH, "//a[normalize-space()='Sign out']"),
        (By.CSS_SELECTOR, "form.logout-form button[type='submit']"),
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def open_login(self) -> "LoginPage":
        self.open(LOGIN_URL)
        return self

    @allure.step("Login to GitHub via UI")
    def login(self, username: str, password: str) -> None:
        self.type(*self._LOGIN_INPUT, text=username)
        self.type(*self._PASSWORD_INPUT, text=password)
        self.click(*self._SUBMIT_BUTTON)

    @allure.step("Login to GitHub using Settings credentials")
    def login_with_settings(self) -> None:
        self.open_login()
        self.login(Settings.GITHUB_USERNAME, Settings.GITHUB_PASSWORD)

    @allure.step("Open user menu")
    def open_user_menu(self) -> None:
        self.click_any(self._USER_MENU_CANDIDATES)

    @allure.step("Logout from GitHub via UI")
    def logout(self) -> None:
        self.open_user_menu()
        self.click_any(self._SIGN_OUT_CANDIDATES)