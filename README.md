# schwul
アニメ上映管理

## Setup
Install `Docker` and `docker-compose`.

`touch .env` and edit.
```
POSTGRES_DB=schwul
POSTGRES_USER=homo
POSTGRES_PASSWORD=caDrufr2Sp7m
```


## Usage
```
docker-compose up -d
docker-compose exec django python manage.py migrate
docker-compose exec django python manage.py runserver 0.0.0.0:8000
```
