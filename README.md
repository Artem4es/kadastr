### [Что это за kadastr?] :smiley_cat: 
Kadastr - это эмулятор взаимодействия клиентского API и внешнего API реализованные на FastAPI. Клиент вводит координаты объекта (широту, долготу и его кадастровый номер). После этого клиентский API передаёт запрос внешнему сервису для обработки. Клиенту возвращается уникальный query_id по которому он может узнать результат через эндпоинт /result. 

### Как запустить? :space_invader:
Проект можно запустить, используя Docker-compose для этого:

Клонировать репозиторий:

```
git clone git@github.com:Artem4es/kadastr.git
```

Перейти в папку infra и создать файл .env :
```
EXTERNAL_API = http://172.17.0.1:8000  # local machine address for docker container
REDIS_HOST = redis
REDIS_PORT = 6379
DEBUG = False
API_NAME = KadastrAPI
```

и файл .ext_env :
```
REDIS_PORT = 6379
REDIS_HOST = redis_ext
DEBUG = False
API_NAME = ExternalAPI
```

Cоздать и запустить контейнеры из папки infra:
```
docker compose up -d
```

### Документация проекта: :blue_book:
После запуска проекта доступная документация Swagger и Redoc по адресам:
Клиентский API: http://localhost/docs/
или тут
http://localhost/redoc/

Внешний API: http://localhost:8000/docs/
или тут
http://localhost:8000/redoc/

