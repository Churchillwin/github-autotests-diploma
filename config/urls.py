from __future__ import annotations

from config.settings import Settings

BASE_URL = Settings.GITHUB_BASE_URL

LOGIN_URL = f"{BASE_URL}/login"
NEW_REPO_URL = f"{BASE_URL}/new"