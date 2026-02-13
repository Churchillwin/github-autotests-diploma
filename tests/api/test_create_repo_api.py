from __future__ import annotations

import allure
import pytest

from api_client.github_client import GitHubClient
from config.settings import Settings


@allure.story("GitHub API: Repositories")
@allure.title("Create repository returns 201 and name matches")
@pytest.mark.api
def test_create_repo_api(github_client: GitHubClient, repo_name: str) -> None:
    with allure.step("Create repo via API"):
        r = github_client.create_repo(repo_name, private=True)
        assert r.status_code == 201
        assert r.json is not None
        assert r.json.get("name") == repo_name

    with allure.step("Cleanup: delete repo"):
        deleted = github_client.delete_repo(Settings.GITHUB_USERNAME, repo_name)
        assert deleted.status_code == 204