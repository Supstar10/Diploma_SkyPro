# Educational Modules API

Дипломный проект для управления образовательными модулями.

## Структура проекта

Проект состоит из приложения **modules**:
- **modules** — управление образовательными модулями.

## Технологии

- **Django** — веб-фреймворк.
- **Django Rest Framework** — для создания API.
- **PostgreSQL** — база данных.
- **Docker** — для контейнеризации приложения.
- **Swagger** — для автогенерации документации API.

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Supstar10/Diploma_SkyPro.git
cd Diploma_SkyPro
```

### 2. Собрать контейнер Docker(Миграции и фикстуры будут загружены автоматически, код описан в docker/entrypoint.sh)
```bash
docker compose up --build
```

### 3. Доступ к серверу

- API будет доступно по адресу [http://localhost:8000](http://localhost:8000)
- Swagger документация доступна по адресу [http://localhost:8000/swagger](http://localhost:8000/swagger)

### 4. Эндпойнты API

#### Образовательные модули
- GET /api/modules/ — Получить список образовательных модулей.
- POST /api/modules/ — Создать новый образовательный модуль.
- GET /api/modules/{id}/ — Получить информацию о модуле.
- PATCH /api/modules/{id}/ — Обновить образовательный модуль.
- DELETE /api/modules/{id}/ — Удалить образовательный модуль.

### 5. Тесты
Чтобы запустить тесты, выполните команду:
```bash
docker compose exec app python manage.py test
```