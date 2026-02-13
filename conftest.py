from __future__ import annotations

import os
import time
from typing import Generator

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from api_client.github_client import GitHubClient
from config.settings import Settings


@pytest.fixture(scope="function")
def driver() -> Generator[webdriver.Firefox, None, None]:
    """Create a fresh Firefox WebDriver instance for each test."""
    options = FirefoxOptions()
    options.set_preference("dom.webnotifications.enabled", False)

    profile_path = os.getenv("FIREFOX_PROFILE")
    if profile_path:
        options.profile = profile_path

    driver_instance = webdriver.Firefox(options=options)
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()


@pytest.fixture(scope="session")
def github_client() -> GitHubClient:
    """API client for GitHub REST API."""
    return GitHubClient()


@pytest.fixture
def repo_name() -> str:
    ts = int(time.time() * 1000)
    return f"{Settings.REPO_PREFIX}-{ts}"


@pytest.fixture
def created_repo(github_client: GitHubClient, repo_name: str) -> str:
    """Create a repo before the test and delete it after."""
    with allure.step("Precondition: create repo via API"):
        r = github_client.create_repo(repo_name, private=True)
        assert r.status_code == 201, f"Repo create failed: {r.status_code} {r.json}"

    yield repo_name

    with allure.step("Postcondition: delete repo via API"):
        github_client.delete_repo(Settings.GITHUB_USERNAME, repo_name)