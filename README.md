### Python - Django example of API

### Requirements
you need to get docker installed, if you dont have, please go to https://docs.docker.com/install/

### Run application
```bash
docker-compose up [-d] to detach and test on the same window, without it use another window to test, and this to see the logs.
```
### API - Tests
## GET
```bash
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/employees/
```
## POST
```bash
curl -d "name=Thiago Catoto&email=catoto@luizalabs.com&department=Mobile" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://127.0.0.1:8000/employees/
```
## DELETE
```bash
curl -X DELETE http://127.0.0.1:8000/employees/1
```