from __future__ import annotations

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from config.urls import NEW_REPO_URL


class NewRepoPage(BasePage):
    REPO_NAME_INPUT = (By.ID, "repository_name")

    OWNER_DROPDOWN = (By.ID, "repository_owner")

    PAGE_H1 = (By.CSS_SELECTOR, "h1")

    CREATE_BUTTON = (
        By.XPATH,
        "//button[.//span[contains(normalize-space(), 'Create repository')] "
        "or contains(normalize-space(), 'Create repository')]",
    )

    LOGIN_FIELD = (By.ID, "login_field")
    VERIFY_HEADERS = (
        By.XPATH,
        "//*[contains(.,'Verify') and contains(.,'device')]"
        "|//*[contains(.,'two-factor') or contains(.,'authentication')]"
        "|//*[contains(.,'Enter code') or contains(.,'code')]",
    )

    @allure.step("Открываем страницу создания репозитория")
    def open_page(self, timeout: int = 25) -> None:
        self.open(NEW_REPO_URL)
        wait = WebDriverWait(self.driver, timeout)

        
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        
        if self._is_present(self.LOGIN_FIELD, 2):
            raise AssertionError(
                f"После перехода на /new нас перекинуло на логин. URL={self.driver.current_url}"
            )

        
        if self._is_present(self.VERIFY_HEADERS, 2):
            raise AssertionError(
                "GitHub требует подтверждение устройства/2FA, поэтому UI-тест создания репо "
                f"не может продолжиться. URL={self.driver.current_url}"
            )


        try:
            wait.until(EC.visibility_of_element_located(self.REPO_NAME_INPUT))
        except Exception:
            h1 = self._safe_text(self.PAGE_H1)
            raise AssertionError(
                "Не нашли поле repository_name на странице создания репозитория.\n"
                f"URL: {self.driver.current_url}\n"
                f"H1: {h1}\n"
                "Скорее всего GitHub показал другой экран (verify/2FA/redirect)."
            )

    @allure.step("Создаём репозиторий: {name}")
    def create_repo(self, name: str, timeout: int = 25) -> None:
        wait = WebDriverWait(self.driver, timeout)

        name_input = wait.until(EC.visibility_of_element_located(self.REPO_NAME_INPUT))
        name_input.clear()
        name_input.send_keys(name)

        btn = wait.until(EC.presence_of_element_located(self.CREATE_BUTTON))
        wait.until(lambda d: btn.is_enabled())
        wait.until(EC.element_to_be_clickable(self.CREATE_BUTTON)).click()

        wait.until(lambda d: f"/{name}" in d.current_url or "/settings" in d.current_url)



    def _is_present(self, locator: tuple, timeout: int) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except Exception:
            return False

    def _safe_text(self, locator: tuple) -> str:
        try:
            el = self.driver.find_element(*locator)
            return (el.text or "").strip()
        except Exception:
            return ""