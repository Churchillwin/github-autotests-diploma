from __future__ import annotations

import allure
import pytest

from api_client.github_client import GitHubClient
from config.settings import Settings


@allure.story("GitHub API: Repositories")
@allure.title("Delete repository returns 204")
@pytest.mark.api
def test_delete_repo_api(github_client: GitHubClient, repo_name: str) -> None:
    with allure.step("Precondition: create repo"):
        created = github_client.create_repo(repo_name, private=True)
        assert created.status_code == 201

    with allure.step("Delete repo"):
        deleted = github_client.delete_repo(Settings.GITHUB_USERNAME, repo_name)
        assert deleted.status_code == 204