# django mysql
## install python mysqlclient ubuntu os
```bash
sudo apt-get update -y
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
pip install mysqlclient
```
## django migration
```bash
docker-compose up --build -d
docker-compose exec app python manage.py makemigrations
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py createsuperuser
```
