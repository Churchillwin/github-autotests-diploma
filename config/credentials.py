import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
LOGIN = os.getenv("TEST_LOGIN")
PASSWORD = os.getenv("TEST_PASSWORD")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")