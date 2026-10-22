# CRM Backoffice (Django)

CRM для учёта услуг, рекламных кампаний, лидов, контрактов и активных клиентов. Существующие HTML-шаблоны из `templates_only.zip` сохранены без изменений; представления, модели, контекст и URL приведены в соответствие с их полями и маршрутами.

## Запуск через Docker

1. Скопируйте `.env.example` в `.env` и задайте собственные `POSTGRES_PASSWORD` и `DJANGO_SECRET_KEY`.
2. Запустите `docker compose up --build`.
3. Создайте администратора в другом терминале: `docker compose exec web python manage.py createsuperuser`.
4. Откройте `http://localhost:8000/` и войдите. Админка доступна по адресу `http://localhost:8000/admin/`.

Docker Compose ждёт готовности PostgreSQL, применяет уже включённые в репозиторий миграции и создаёт/обновляет группы «Оператор», «Маркетолог» и «Менеджер». Новые миграции автоматически не генерируются.

## Запуск локально без Docker

Python 3.12 рекомендуется. Создайте виртуальное окружение, установите зависимости `pip install -r requirements.txt`, затем выполните:

```bash
python manage.py migrate
python manage.py create_roles
python manage.py createsuperuser
python manage.py runserver
```

По умолчанию используется SQLite для простого локального запуска. Для PostgreSQL задайте `DB_ENGINE=postgresql` и переменные `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`.

## Тесты

```bash
pytest
```

Для Docker: `docker compose exec web pytest`.

## Роли

- **Оператор** — создание, просмотр, изменение и удаление лидов.
- **Маркетолог** — управление услугами и рекламными кампаниями.
- **Менеджер** — управление контрактами и активными клиентами, просмотр лидов.
- **Администратор** — суперпользователь Django.

Настройки `DEBUG=1` и встроенный сервер предназначены для учебной/локальной разработки, не для публичного production-развёртывания.
