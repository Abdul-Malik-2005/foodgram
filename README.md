# Foodgram

*Проект Foodgram - это социальная платформа для обмена рецептами, где пользователи могут делиться своими рецептами, сохранять любимые рецепты и следить за другими пользователями. Проект реализован с использованием Django и PostgreSQL, развернут в контейнерах с помощью Docker и GitHub Actions для CI/CD.*

## Адрес проекта

Проект доступен по адресу: https://foodgram-smm.duckdns.org/


## Технологии

* Python 3.9
* Django 4.2.16
* PostgreSQL
* Docker
* Gunicorn
* Nginx
* GitHub Actions

## Установка

### Локальная установка

1. Перейдите в директорию проекта:

    ```bash
    cd foodgram
    ```

2. Создайте и активируйте виртуальное окружение:

    ```bash
    python -m venv venv
    source venv/bin/activate  # для Linux/MacOS
    source venv/Scripts/activate  # для Windows
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Настройте базу данных:

    * Убедитесь, что у вас установлен PostgreSQL.
    * Создайте базу данных и настройте подключение в `settings.py`.

5. Примените миграции:

    ```bash
    python manage.py migrate
    ```

6. Создайте суперпользователя:

    ```bash
    python manage.py createsuperuser
    ```

7. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

### Запуск в контейнерах

1. Создайте и запустите контейнеры с помощью Docker:

    ```bash
    docker-compose up --build
    ```

2. Для остановки контейнеров используйте команду:

    ```bash
    docker-compose down
    ```

## CI/CD

Проект настроен для автоматической сборки и развертывания с использованием GitHub Actions. При каждом пуше в репозиторий будет происходить автоматическая сборка и деплой на удалённый сервер.

## Структура проекта

* `foodgram/` — основная директория проекта
* `requirements.txt` — зависимости Python
* `docker-compose.yml` — настройка для запуска контейнеров
* `nginx.conf` — конфигурация для Nginx

## Разработчик

https://github.com/Abdul-Malik-2005

## Лицензия

Этот проект лицензируется на условиях MIT.
