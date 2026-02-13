from __future__ import annotations

from typing import Iterable, Tuple

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import Settings

Locator = Tuple[By, str]


class BasePage:
    """Base PageObject with common Selenium helpers."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, Settings.UI_TIMEOUT)

    def open(self, url: str) -> None:
        with allure.step(f"Open URL: {url}"):
            self.driver.get(url)

    def current_url(self) -> str:
        return self.driver.current_url

    def wait_visible(self, by: By, locator: str) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def wait_clickable(self, by: By, locator: str) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def click(self, by: By, locator: str) -> None:
        with allure.step(f"Click element: {by}={locator}"):
            self.wait_clickable(by, locator).click()

    def type(self, by: By, locator: str, text: str) -> None:
        with allure.step(f"Type into element: {by}={locator}"):
            el = self.wait_visible(by, locator)
            el.clear()
            el.send_keys(text)

    def wait_any_visible(self, locators: Iterable[Locator]) -> WebElement:
        """Wait until ANY of the locators becomes visible; returns the first matched element."""
        last_error: Exception | None = None
        for by, selector in locators:
            try:
                return self.wait_visible(by, selector)
            except Exception as e:  # noqa: BLE001
                last_error = e
        raise last_error or TimeoutError("None of the locators became visible")

    def click_any(self, locators: Iterable[Locator]) -> None:
        """Click the first locator that becomes clickable."""
        last_error: Exception | None = None
        for by, selector in locators:
            try:
                with allure.step(f"Click candidate: {by}={selector}"):
                    self.wait_clickable(by, selector).click()
                return
            except Exception as e:  
                last_error = e
        raise last_error or TimeoutError("None of the locators was clickable")