from __future__ import annotations

import allure
import pytest
from selenium.webdriver.common.by import By

from config.settings import Settings
from pages.login_page import LoginPage


@allure.story("GitHub UI: Repositories")
@allure.title("Created repo is visible in UI repositories list")
@pytest.mark.ui
def test_repo_exists_ui(driver, created_repo: str) -> None:
    page = LoginPage(driver)
    page.login_with_settings()

    repos_url = f"{Settings.GITHUB_BASE_URL}/{Settings.GITHUB_USERNAME}?tab=repositories"
    page.open(repos_url)

    with allure.step("Verify repository link exists on the page"):
        repo_link = (By.CSS_SELECTOR, f"a[href='/{Settings.GITHUB_USERNAME}/{created_repo}']")
        page.wait_visible(*repo_link)