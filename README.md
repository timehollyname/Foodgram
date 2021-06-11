### FoodGram ![Workflow](https://github.com/timehollyname/foodgram-project/actions/workflows/actions.yml/badge.svg)
____
#### Описание:
> FoodGram - это онлайн-сервис, где пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
____
#### Конфигурационный файл .env:
| Ключ | Тип | Подсказка |
|------|:----------:|-----------|
| SECRET_KEY | str | Случайное значение. Это значение является ключевым аспектом защиты подписанных данных – очень важно сохранять его в тайне. |
| DEBUG | bool | Включает/выключает режим отладки. |
| ALLOWED_HOSTS | str | Имена доменов / хостов, которые может обслуживать этот сайт Django. Указывать через пробелы, например: 127.0.0.1 your-domain.com |
| DB_ENGINE | str | Используемый механизм базы данных. [Django](https://djangodoc.ru/3.1/ref/settings/#engine) |
| DB_NAME && POSTGRES_DB | str | Название используемой базы данных. |
| POSTGRES_USER | str | Имя пользователя используемое при подключении к базе данных. |
| POSTGRES_PASSWORD | str | Пароль, используемый при подключении к базе данных. |
| DB_HOST | str | Пароль, используемый при подключении к базе данных. |
| DB_PORT | str | Порт, используемый при подключении к базе данных. |
| LANGUAGE_CODE | str | [Django](https://djangodoc.ru/3.1/ref/settings/#language-code) |
| TIME_ZONE | str | [Django](https://djangodoc.ru/3.1/ref/settings/#std:setting-TIME_ZONE) |
| EMAIL_HOST | str | Имя хоста используемое для отправки электронных писем. |
| EMAIL_PORT | int | Порт, используемый при подключении к SMTP серверу указанному в ```EMAIL_HOST```. |
| EMAIL_HOST_USER | str | Имя пользователя используемое при подключении к SMTP серверу указанному в ```EMAIL_HOST```. |
| EMAIL_HOST_PASSWORD | str | Пароль для подключения к SMTP сервера, который указан в ```EMAIL_HOST```. Эта настройка используется вместе с ```EMAIL_HOST_USER``` для авторизации при подключении к SMTP серверу. |
| EMAIL_USE_TLS | bool | Указывает использовать ли TLS (защищенное) соединение с SMTP сервером. Используется для явного использования TLS подключения, обычно к 587 порту. |
| EMAIL_USE_SSL | bool | Указывает использовать ли неявное TLS (защищенное) соединение с SMTP сервером. В документации этот тип TLS подключения обычно называется SSL. По умолчанию использует 465 порт. |
| INTERNAL_IPS | bool | Django Debug Toolbar отображается только в том случае, если в списке INTERNAL_IPS есть IP приложения и включен режим отладки. |
____
#### Как запустить проект:
1. Работа с файлами:
    1. ```.env```
        - **Обязательно на начальном этапе**. Настроить конфигурационный файл.
    2. ```project/foodgram/settings.py```
        - **По желанию**. Настроить второй конфигурационный файл. [Настройки - Django](https://djangodoc.ru/3.1/ref/settings/)
2. Работа с терминалом:
    1. ```sudo systemctl stop nginx```
        - **Обязательно**. Временно отключить службу nginx.
    2. ```sudo docker-compose up -d```
        - **Обязательно на начальном этапе**. Создать образы и запустить проект в фоновом режиме.
    3. ```sudo docker-compose exec web python project/manage.py collectstatic --no-input```
        - **Обязательно на начальном этапе**. Собрать всю статику приложений в одну папку. 
    4. ```sudo docker-compose exec web python project/manage.py makemigrations --no-input```
        - **Обязательно на начальном этапе**. Создать новые миграций на основе изменений в моделях.
    5. ```sudo docker-compose exec web python project/manage.py migrate --no-input```
        - **Обязательно на начальном этапе**. Создав новые миграции следует применить их к базе данных.
    6. ```sudo docker-compose exec web python project/manage.py createsuperuser```
        - **По желанию**. Создать пользователя, который может заходить на интерфейс администратора.
    7. ```sudo docker-compose exec web python project/manage.py loaddata db.json```
        - **По желанию**. Заполнение базы данных начальными данными. Если не создан хотя-бы один пользователь, может вылететь ошибка.
3. Демо:
    1. API:
        - [ya-project-thn.ru](http://ya-project-thn.ru/api/v1/)
    2. Главная страница:
        - [ya-project-thn.ru](http://ya-project-thn.ru/)
    3. Интерфейс администратора:
        - [ya-project-thn.ru](http://ya-project-thn.ru/admin/)
