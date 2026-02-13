from __future__ import annotations

import allure
import pytest

from api_client.github_client import GitHubClient
from config.settings import Settings


@allure.story("GitHub API: Issues")
@allure.title("Create issue returns 201 and contains number")
@pytest.mark.api
def test_issue_api(github_client: GitHubClient, created_repo: str) -> None:
    with allure.step("Create issue via API"):
        r = github_client.create_issue(Settings.GITHUB_USERNAME, created_repo, title="autotest issue")
        assert r.status_code == 201
        assert r.json is not None
        assert "number" in r.json
        assert r.json.get("title") == "autotest issue"