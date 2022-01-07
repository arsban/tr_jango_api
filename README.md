# Movies
"Каталог Фильмов"


### Разворачиваем проект
- склонируйте репозиторий к себе в директорию
```
git clone https://github.com/arsban/tr_jango_api
```

- перейдите в директорию с общими файлами
```
cd tr_jango_api
```

- создайте вертуальное откружение и активирейте его 
```
python -m venv venv
```

- для Windows
```
source venv/Scripts/activate
```
- для Mac source 
```
venv/bin/activate
```

- обновите пакеты pip
```
python3 -m pip install --upgrade pip
```

- Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

- перейдите в главную директорию проекта
``` 
cd my_applc
```

- в главной директории проекта создайте файл .env и сохраните в нем сдедующие параметры
- параметры и настройки относятся только к gmail.com
```
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = здесь укажите в кавычках почту с которой будет приходить подтверждение для регистрации
EMAIL_HOST_PASSWORD = здесь пароль от почты, тоже в кавычках
EMAIL_PORT = 587
```
будте внимательны, этот файл хранит ваши персональные данные.
так же нужно в вашем google аккаунте, на котором зарегистрирована почта, включить параметр - "Ненадежные приложения, у которых есть доступ к аккаунту"
он доступен в вашем google аккаунте по пути "Безопасность" -> "Ненадежные приложения, у которых есть доступ к аккаунту"

- Выполнить миграции
```
python3 manage.py migrate
```

- создайте суперпользователя
```
python3 manage.py createsuperuser
```

- Запустите проект
```
python3 manage.py runserver
```

- для удобной отправки POST и GET запростов используются специальные программы для работы с "голым" API
- дальнейшие инструкции предназначены для работы с программой postman
- это встроенные ссылки из djoser
- они есть в автоматической документации
```
http://127.0.0.1:8000/redoc/
```
```
http://127.0.0.1:8000/swagger/
```


- ссылка для регистрации прользователя.
- нужно отправить POST запрос с полями username, password, email. 
- в ответ должен придти json с вашим email, username и id который будет присвоем при регистрации.
```
http://127.0.0.1:8000/auth/users/
```


- на почту придет ссылка для подтверждения.
- где uid - OQ
- а token - ayvvr3-553b6e3c6b1e1aec3efcc2d87788dc04
```
пример http://127.0.0.1:8000/#/activate/OQ/ayvvr3-553b6e3c6b1e1aec3efcc2d87788dc04
```

- ссылка для подтверждения пользователя.
- нужно отправить POST запрос с полями uid и token.
```
http://127.0.0.1:8000/auth/users/activation/
```

- ссылка для входа на сервис после подтверждения.
- нужно отправить POST запрос с полями username и password.
- в ответ придет json с параметром - auth_token, это ваш токен который открывает вам доступ к сервису.
```
http://127.0.0.1:8000/auth/token/login/
```

- ссылка для проверки данных пользователя.
- отправте GET запрос после проделанного выше подставив полученный токен в Authorization в программе postman
- в ответ должен придти json с параметрами email, id и username
```
http://127.0.0.1:8000/auth/users/me/
```


- чтобы подтверждение работало прямо по ссылке из почты, надо делать frontend, 
- который автоматический будет отправлять POST запрос в backend по ссылке
