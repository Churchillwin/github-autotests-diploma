from __future__ import annotations

import os

from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv(), override=True)


def _require(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required env var: {name}")
    return value


class Settings:

    GITHUB_BASE_URL: str = os.getenv("GITHUB_BASE_URL", os.getenv("BASE_URL", "https://github.com"))
    GITHUB_API_URL: str = os.getenv("GITHUB_API_URL", os.getenv("API_BASE_URL", "https://api.github.com"))

    GITHUB_USERNAME: str = os.getenv("GITHUB_USERNAME") or _require("TEST_LOGIN")
    GITHUB_PASSWORD: str = os.getenv("GITHUB_PASSWORD") or _require("TEST_PASSWORD")
    GITHUB_TOKEN: str = _require("GITHUB_TOKEN")

    UI_TIMEOUT: int = int(os.getenv("UI_TIMEOUT", "10"))
    REPO_PREFIX: str = os.getenv("REPO_PREFIX", "autotest-diploma")



BASE_URL: str = Settings.GITHUB_BASE_URL
API_BASE_URL: str = Settings.GITHUB_API_URL
USERNAME: str = Settings.GITHUB_USERNAME
PASSWORD: str = Settings.GITHUB_PASSWORD
GITHUB_TOKEN: str = Settings.GITHUB_TOKEN