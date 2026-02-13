from __future__ import annotations

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from config.urls import REPOS_URL


class ReposPage(BasePage):
    REPO_LIST = (By.ID, "user-repositories-list")
    REPO_ITEMS = (By.CSS_SELECTOR, "#user-repositories-list li")
    TAB_LINK = (By.CSS_SELECTOR, "a[href*='?tab=repositories']")

    @allure.step("Открываем страницу репозиториев")
    def open_page(self, timeout: int = 20) -> None:
        self.open(REPOS_URL)
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        wait.until(EC.presence_of_element_located(self.REPO_LIST))

    @allure.step("Проверяем, что вкладка Repositories открылась")
    def is_opened(self, timeout: int = 20) -> bool:
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located(self.REPO_LIST))
        return "tab=repositories" in self.driver.current_url

    @allure.step("Проверяем, что список репозиториев виден")
    def repo_list_is_visible(self, timeout: int = 20) -> bool:
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(self.REPO_LIST))
        return True

    @allure.step("Получаем количество репозиториев на странице")
    def count_repos(self, timeout: int = 20) -> int:
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located(self.REPO_LIST))
        return len(self.finds(self.REPO_ITEMS))