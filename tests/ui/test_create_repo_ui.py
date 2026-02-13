from __future__ import annotations

import allure
import pytest
from selenium.webdriver.common.by import By

from config.settings import Settings
from pages.login_page import LoginPage


@allure.story("GitHub UI: Repositories")
@allure.title("User can open New repository page")
@pytest.mark.ui
def test_create_repo_ui(driver) -> None:
    page = LoginPage(driver)
    page.login_with_settings()

    with allure.step("Open New Repository page"):
        page.open(f"{Settings.GITHUB_BASE_URL}/new")

    with allure.step("Verify repository creation form is visible"):
        # Stable element on /new page
        page.wait_visible(By.XPATH, "//h1[contains(., 'Create a new repository') or contains(., 'Create a new repository')]")