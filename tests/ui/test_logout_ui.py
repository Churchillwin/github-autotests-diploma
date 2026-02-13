from __future__ import annotations

import allure
import pytest

from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


@allure.story("GitHub UI: Auth")
@allure.title("User can logout via UI")
@pytest.mark.ui
def test_logout_ui(driver) -> None:
    LoginPage(driver).login_with_settings()
    LogoutPage(driver).logout()