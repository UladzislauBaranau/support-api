# Support: API for sending tickets to the support service 

The user describes his problem and sends it to the support service. 
The support service sees the tasks, response to them, and also changes the status of the task. 

## Key Features
- JWT authorization
- Send emails used a message broker

## Installation

### SMTP backend
Replace `EMAIL ADDRESS` and `EMAIL ADDRESS PASSWORD` with your real ones at `setting.py`. Also don't forget to change
email on `tasks.py` module.

### Configuration *.env.dev* file 
Refer to [env example](https://github.com/UladzislauBaranau/support-api/blob/changejwt/.env.dev), as a full configuration file. By default, development environment searched at `./.env.dev`.

## Running project in docker

Run the following commands:
```
docker build -t support .
docker-compose up --build
```
Detailed information about quickstart **Docker** and **Django** can be found in [documentation](https://docs.docker.com/samples/django/).

## License
See [MIT license](https://github.com/UladzislauBaranau/support-api/blob/master/LICENSE).
