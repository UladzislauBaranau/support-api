# Support: API for sending tickets to the support service 

The user describes his problem and sends it to the support service. 
The support service sees the tasks, response to them, and also changes the status of the task. 

## Key Features
- JWT authorization
- Send emails used a message broker

## Technical Requirements/Installation

### Requirements
1. Python 3.8+
2. PostgreSQL 12+
3. Redis-server

### Installation

#### Development tools
```
python3 -m venv .venv
. ./.venv/bin/activate
pip install -r requirements.txt
```
After that,  you'll have *support app* and *all development tools* installed into virtualenv. For correctly **Djoser** 
work, you need to `import six` by the following path `.venv/lib64/python3.8/site-packages/django/utils/__init__.py`.

#### SMTP backend
Replace `EMAIL ADDRESS` and `EMAIL ADDRESS PASSWORD` with your real ones at `setting.py`. Also don't forget to change
email on `tasks.py` module.

#### Setup PostgreSQL
```
sudo -u postgres psql
```
```
postgres=# create database support;
postgres=# create user support with encrypted password 'support';
postgres=# grant all privileges on database support to support;
postgres=# alter user support CREATEDB;
```

## Running and Testing

### Running

#### Run migrations and dev server
```
./manage.py migrate
./manage.py runserver
```

#### Run redis and celery
```
redis-server
celery -A support worker -l INFO
```
Detailed information about the work of **Celery** with **Django** can be found in 
the [documentation](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html).

### Testing
Before running the tests, please enable **redis-server**, and then run the `pytest` command.

## License
See [MIT license](https://github.com/UladzislauBaranau/support-api/blob/master/LICENSE).