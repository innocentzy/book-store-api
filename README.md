# Book Store API

REST API для книжного магазина на FastAPI с PostgreSQL.

## Стек технологий

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy 2.0 (async)
- Alembic
- Pydantic v2
- JWT аутентификация

## Структура проекта

```
app/
├── main.py           # Точка входа
├── config.py         # Настройки
├── database.py       # Подключение к БД
├── models.py         # SQLAlchemy модели
├── schemas.py        # Pydantic схемы
├── crud.py           # Функции работы с БД
├── security.py       # JWT и хеширование паролей
├── dependencies.py   # FastAPI зависимости
└── routers/
    ├── auth.py       # Аутентификация
    ├── books.py      # Книги
    ├── authors.py    # Авторы
    └── orders.py     # Заказы
```

## Быстрый старт

```bash
# Клонировать репозиторий
git clone https://github.com/innocentzy/book-store-api.git
cd book-store-api

# Создать .env файл
cp .env.example .env

# Запустить контейнеры
docker-compose up --build
```

API будет доступен по адресу: http://localhost:8000

Swagger UI: http://localhost:8000/docs

## API Endpoints

### Аутентификация

| Метод | Endpoint       | Описание                    |
| ----- | -------------- | --------------------------- |
| POST  | /auth/register | Регистрация пользователя    |
| POST  | /auth/login    | Вход (получение JWT токена) |

### Книги

| Метод  | Endpoint    | Описание                            | Доступ |
| ------ | ----------- | ----------------------------------- | ------ |
| GET    | /books      | Список книг (пагинация, фильтрация) | Все    |
| GET    | /books/{id} | Информация о книге                  | Все    |
| POST   | /books      | Добавить книгу                      | Admin  |
| PATCH  | /books/{id} | Обновить книгу                      | Admin  |
| DELETE | /books/{id} | Удалить книгу                       | Admin  |

### Авторы

| Метод | Endpoint      | Описание            | Доступ |
| ----- | ------------- | ------------------- | ------ |
| GET   | /authors      | Список авторов      | Все    |
| GET   | /authors/{id} | Автор с его книгами | Все    |
| POST  | /authors      | Создать автора      | Admin  |

### Заказы

| Метод | Endpoint | Описание       | Доступ         |
| ----- | -------- | -------------- | -------------- |
| POST  | /orders  | Оформить заказ | Авторизованные |

## Тестирование

```bash
# Установить зависимости для тестов
pip install -r requirements.txt

# Запустить тесты
pytest
```

## Переменные окружения

| Переменная                  | Описание                     | По умолчанию                                             |
| --------------------------- | ---------------------------- | -------------------------------------------------------- |
| DATABASE_URL                | URL подключения к PostgreSQL | postgresql+asyncpg://postgres:postgres@db:5432/bookstore |
| SECRET_KEY                  | Секретный ключ для JWT       | dev-secret-key-change-me                                 |
| ALGORITHM                   | Алгоритм JWT                 | HS256                                                    |
| ACCESS_TOKEN_EXPIRE_MINUTES | Время жизни токена           | 30                                                       |

## Миграции

```bash
# Создать новую миграцию
alembic revision --autogenerate -m "description"

# Применить миграции
alembic upgrade head

# Откатить последнюю миграцию
alembic downgrade -1
```
