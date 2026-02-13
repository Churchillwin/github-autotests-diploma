from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import allure
import requests

from config.settings import Settings


@dataclass(frozen=True)
class ApiResponse:
    status_code: int
    json: dict[str, Any] | None


class GitHubClient:
    """Minimal GitHub REST API client for diploma autotests."""

    def __init__(self) -> None:
        self.base_url: str = Settings.GITHUB_API_URL

        self.session: requests.Session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {Settings.GITHUB_TOKEN}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            }
        )

    @allure.step("API: Get current user (GET /user)")
    def get_current_user(self) -> ApiResponse:
        r = self.session.get(f"{self.base_url}/user", timeout=20)
        data = r.json() if r.content else None
        return ApiResponse(r.status_code, data)

    @allure.step("API: Create repo '{name}' (POST /user/repos)")
    def create_repo(self, name: str, private: bool = True) -> ApiResponse:
        payload = {"name": name, "private": private}
        r = self.session.post(f"{self.base_url}/user/repos", json=payload, timeout=20)
        data = r.json() if r.content else None
        return ApiResponse(r.status_code, data)

    @allure.step("API: Get repo '{owner}/{repo}' (GET /repos/{owner}/{repo})")
    def get_repo(self, owner: str, repo: str) -> ApiResponse:
        r = self.session.get(f"{self.base_url}/repos/{owner}/{repo}", timeout=20)
        data = r.json() if r.content else None
        return ApiResponse(r.status_code, data)

    @allure.step("API: Delete repo '{owner}/{repo}' (DELETE /repos/{owner}/{repo})")
    def delete_repo(self, owner: str, repo: str) -> ApiResponse:
        r = self.session.delete(f"{self.base_url}/repos/{owner}/{repo}", timeout=20)
        data = r.json() if r.content else None
        return ApiResponse(r.status_code, data)

    @allure.step("API: Create issue '{title}' in '{owner}/{repo}' (POST /repos/.../issues)")
    def create_issue(self, owner: str, repo: str, title: str, body: str | None = None) -> ApiResponse:
        payload: dict[str, Any] = {"title": title}
        if body:
            payload["body"] = body

        r = self.session.post(
            f"{self.base_url}/repos/{owner}/{repo}/issues",
            json=payload,
            timeout=20,
        )
        data = r.json() if r.content else None
        return ApiResponse(r.status_code, data)

    @allure.step("API: Close issue #{issue_number} in '{owner}/{repo}' (PATCH /repos/.../issues/{issue_number})")
    def close_issue(self, owner: str, repo: str, issue_number: int) -> ApiResponse:
        payload = {"state": "closed"}
        r = self.session.patch(
            f"{self.base_url}/repos/{owner}/{repo}/issues/{issue_number}",
            json=payload,
            timeout=20,
        )
        data = r.json() if r.content else None
        return ApiResponse(r.status_code, data)