# Документация к API проекта YAMDB (v1)

### Описание
Проект YaMDb собирает отзывы пользователей на различные произведения;

### Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/afivan20/api_yamdb.git
cd api_yamdb
``` 

- Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```

- Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

- Выполнить миграции:
```
python3 manage.py migrate
```

- Запустить проект:
```
python3 manage.py runserver
```
Ознакомиться с документацией по адресу.
```
http://127.0.0.1:8000/redoc/
```


### Алгоритм получения токена:
#### 1. Получить код подтвержения.
в теле передать JSON
{
  "username": "имя_пользователя",
  "email": "адрес эл. почты"
}
POST-запрос на эндпоинт:
[http://127.0.0.1:8000/api/v1/auth/signup/](http://127.0.0.1:8000/api/v1/auth/signup/)


в папке sent_emails найти письмо и скопировать полученный код подвтерждения.

#### 2. Получить токен.
в теле передать JSON
{
  "username": "имя_пользователя",
  "confirmation_code": "код_подвтержения"
}
POST-запрос на эндпоинт:
```
http://127.0.0.1:8000/api/v1/auth/token/
```
Использовать полученный токен для авторизации.

### Некоторые примеры запросов к API.
Доступные энд-поинты:
GET-запрос на эндпоинты:
```
http://127.0.0.1:8000/api/v1/users/
```
```
http://127.0.0.1:8000/api/v1/titles/
```
```
http://127.0.0.1:8000/api/v1/categories/
```
```
http://127.0.0.1:8000/api/v1/genres/
```
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
```
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
