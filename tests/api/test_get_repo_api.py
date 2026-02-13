from __future__ import annotations

import allure
import pytest

from api_client.github_client import GitHubClient
from config.settings import Settings


@allure.story("GitHub API: Repositories")
@allure.title("Get repository returns 200 and correct full_name")
@pytest.mark.api
def test_get_repo_api(github_client: GitHubClient, created_repo: str) -> None:
    r = github_client.get_repo(Settings.GITHUB_USERNAME, created_repo)
    assert r.status_code == 200
    assert r.json is not None
    assert r.json.get("full_name") == f"{Settings.GITHUB_USERNAME}/{created_repo}"