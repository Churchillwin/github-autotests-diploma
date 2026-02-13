from __future__ import annotations

import allure
import pytest

from config.settings import Settings
from pages.login_page import LoginPage


@allure.story("GitHub UI: Auth & Navigation")
@allure.title("User can login and open repositories tab")
@pytest.mark.ui
def test_login_and_open_repos(driver) -> None:
    page = LoginPage(driver)
    page.login_with_settings()

    repos_url = f"{Settings.GITHUB_BASE_URL}/{Settings.GITHUB_USERNAME}?tab=repositories"
    page.open(repos_url)

    with allure.step("Verify repositories tab opened"):
        assert "tab=repositories" in page.current_url()