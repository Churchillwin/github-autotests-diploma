import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from config.settings import BASE_URL


class IssuePage(BasePage):

    NEW_ISSUE_BTN = (By.CSS_SELECTOR, "a.btn-primary[href$='/issues/new']")
    TITLE_INPUT = (By.ID, "issue_title")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit'][data-disable-with]")

    @allure.step("Открываем страницу Issues репозитория {owner}/{repo}")
    def open_page(self, owner: str, repo: str) -> None:
        self.open(f"{BASE_URL}/{owner}/{repo}/issues")

    @allure.step("Создаём Issue с названием: {title}")
    def create_issue(self, title: str, timeout: int = 20) -> None:
        wait = WebDriverWait(self.driver, timeout)

        wait.until(EC.element_to_be_clickable(self.NEW_ISSUE_BTN)).click()
        wait.until(EC.visibility_of_element_located(self.TITLE_INPUT)).send_keys(title)

        wait.until(EC.element_to_be_clickable(self.SUBMIT_BTN)).click()