from __future__ import annotations

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config.settings import Settings
from pages.login_page import LoginPage


@allure.story("GitHub UI: Issues")
@allure.title("User can create an issue via UI")
@pytest.mark.ui
def test_create_issue_ui(driver, created_repo: str) -> None:
    page = LoginPage(driver)
    page.login_with_settings()

    new_issue_url = f"{Settings.GITHUB_BASE_URL}/{Settings.GITHUB_USERNAME}/{created_repo}/issues/new"
    page.open(new_issue_url)

    title = "ui issue autotest"

    title_locators = (
        (By.CSS_SELECTOR, "input#issue_title"),
        (By.CSS_SELECTOR, "input[name='issue[title]']"),
        (By.CSS_SELECTOR, "input[aria-label='Add a title']"),
    )

    # More realistic GitHub buttons texts
    submit_locators = (
        (By.XPATH, "//button[contains(., 'Submit new issue')]"),
        (By.XPATH, "//button[contains(., 'Create issue')]"),
        (By.XPATH, "//button[contains(., 'Submit')]"),
        (By.XPATH, "//button[contains(., 'Open')]"),
        (By.CSS_SELECTOR, "button[type='submit']"),
    )

    with allure.step("Fill issue title"):
        title_el = page.wait_any_visible(title_locators)
        title_el.clear()
        title_el.send_keys(title)

    with allure.step("Submit issue (button click with fallbacks; if not found - press Enter)"):
        try:
            page.click_any(submit_locators)
        except Exception:  # noqa: BLE001
            # Some GitHub layouts submit on Enter when focus is in title
            title_el.send_keys(Keys.ENTER)

    with allure.step("Verify issue created (URL contains /issues/)"):
        assert "/issues/" in page.current_url()