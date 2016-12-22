## API_django_rest_framework
API using Django's Rest Framework (DRF).  Uses JSON Web Tokens for user authentication.

####Create user:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "USERNAME", "password": "PASSWORD"}' http://127.0.0.1:8000/accounts/register/
```

####Retrieve JWT (JSON web token):
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "USERNAME", "password": "PASSWORD"}' http://127.0.0.1:8000/accounts/api-token-auth/
```

####Place JWT in header for further API calls:
```bash
curl -H "Authorization: JWT *TOKEN*" http://127.0.0.1:8000/todo/1/?username=USERNAME
```

####Auto-generated DRF docs
http://127.0.0.1:8000/docs/

####CORS origin whitelist
Port 8080 example (e.g. Angular.js) in settings.py:
```python
ORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
    'http://127.0.0.1:8080',
)
```

####Enable SSL
Settings.py:
```python
SECURE_SSL_REDIRECT = True
```