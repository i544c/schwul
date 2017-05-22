# schwul
アニメ上映管理

## Setup
Install `Docker` and `docker-compose`.

`touch .env` and edit.
```
POSTGRES_HOST=localhost
POSTGRES_DB=schwul
POSTGRES_USER=homo
POSTGRES_PASSWORD=caDrufr2Sp7m
TWITTER_KEY=twitterKey
TWITTER_SECRET=twitterSecret
```


## Usage
```
docker-compose up -d
docker-compose exec django python manage.py migrate
docker-compose exec django python manage.py runserver 0.0.0.0:8000
```
