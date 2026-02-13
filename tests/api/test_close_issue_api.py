from __future__ import annotations

import allure
import pytest

from api_client.github_client import GitHubClient
from config.settings import Settings


@allure.story("GitHub API: Issues")
@allure.title("Close issue returns 200 and state becomes closed")
@pytest.mark.api
def test_close_issue_api(github_client: GitHubClient, created_repo: str) -> None:
    with allure.step("Precondition: create issue"):
        created = github_client.create_issue(Settings.GITHUB_USERNAME, created_repo, title="issue to close")
        assert created.status_code == 201
        assert created.json is not None
        issue_number = int(created.json["number"])  # type: ignore[index]

    with allure.step("Close issue"):
        closed = github_client.close_issue(Settings.GITHUB_USERNAME, created_repo, issue_number)
        assert closed.status_code == 200
        assert closed.json is not None
        assert closed.json.get("state") == "closed"