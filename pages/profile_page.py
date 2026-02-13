import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from config.urls import PROFILE_URL


class ProfilePage(BasePage):

    REPOS_TAB = (By.XPATH, "//a[contains(@href,'?tab=repositories')]")

    @allure.step("Открываем профиль")
    def open_page(self):
        self.open(PROFILE_URL)

    @allure.step("Переходим во вкладку Repositories")
    def go_to_repos(self):
        wait = WebDriverWait(self.driver, 20)

        wait.until(EC.url_contains("github.com"))

        self.driver.switch_to.window(self.driver.window_handles[-1])

        repos_tab = wait.until(
            EC.element_to_be_clickable(self.REPOS_TAB)
        )

        repos_tab.click()