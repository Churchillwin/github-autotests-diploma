from __future__ import annotations

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from config.settings import Settings
from pages.base_page import BasePage, Locator


class LogoutPage(BasePage):
    """Stable logout via GitHub /logout confirmation page + auth-required redirect check."""

    _CONFIRM_SIGN_OUT: Locator = (
        By.CSS_SELECTOR,
        "form[action='/logout'] button[type='submit'], form[action='/logout'] input[type='submit']",
    )


    _LOGIN_FIELD: Locator = (By.ID, "login_field")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    @allure.step("Выходим из аккаунта GitHub через /logout")
    def logout(self) -> None:
        
        self.open(f"{Settings.GITHUB_BASE_URL}/logout")

        
        with allure.step("Подтверждаем выход"):
            self.click(*self._CONFIRM_SIGN_OUT)

        
        with allure.step("Проверяем, что сессия завершена (редирект на /login)"):
            self.open(f"{Settings.GITHUB_BASE_URL}/settings/profile")
            self.wait_visible(*self._LOGIN_FIELD)