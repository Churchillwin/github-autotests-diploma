# GitHub Autotests Diploma (UI + API)

Автоматизированные UI- и API-тесты для GitHub в рамках дипломной работы SkyPro по модулю «Автоматизация тестирования».

## Технологии
- Python 3
- Pytest
- Selenium WebDriver (UI)
- Requests (API)
- Allure (отчётность)
- python-dotenv (конфигурация через `.env`)
- Ruff (линтер)

## Что покрыто тестами

### API (5 тестов)
- Получение данных текущего пользователя (`GET /user`)
- Создание репозитория (`POST /user/repos`)
- Получение репозитория (`GET /repos/{owner}/{repo}`)
- Удаление репозитория (`DELETE /repos/{owner}/{repo}`)
- Создание и закрытие issue (`POST/PATCH /repos/{owner}/{repo}/issues`)

### UI (5 тестов)
- Логин и переход к списку репозиториев
- Открытие страницы создания репозитория
- Проверка, что репозиторий виден в UI (репозиторий создаётся через API в предусловии)
- Создание issue через UI (репозиторий создаётся через API в предусловии)
- Logout (через `/logout` + проверка разлогина на защищённой странице)

> Для стабильности UI-тестов часть предусловий/постусловий выполняется через API (создание/удаление репозиториев).

## Структура проекта

```text
github-autotests-diploma/
api_client/
github_client.py

config/
settings.py
urls.py

pages/
base_page.py
login_page.py
logout_page.py

tests/
api/
test_create_repo_api.py
test_delete_repo_api.py
test_get_repo_api.py
test_issue_api.py
test_close_issue_api.py

ui/
test_login_and_open_repos.py
test_create_repo_ui.py
test_create_issue_ui.py
test_logout_ui.py
test_repo_exists_ui.py

conftest.py
pytest.ini
requirements.txt
pyproject.toml
.env.example
README.md

Запуск только API тестов
pytest tests/api -m "api"

Запуск только UI тестов
pytest tests/ui -m "ui"

Запуск всех тестов
pytest

Запуск с генерацией результатов
pytest --alluredir=allure-results

Просмотр отчёта
allure serve allure-results

Проверка качества кода (линтер)
ruff check .

отчёт
http://127.0.0.1:49317

Проект по ручному тестированию 
https://copper-library-244.notion.site/GIT-29ae81404f32802a934bff55a650ac33

Qase io 
https://app.qase.io/public/report/056b49153933d6e03beef89401ce5ac2aba850d1
