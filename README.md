# API_django_rest_framework
API using Django's Rest Framework.  Uses JSON Web Tokens for user authentication.

#####Create user:
curl -X POST -H "Content-Type: application/json" -d '{"username": "*USERNAME*", "password": "*USERNAME*"}' http://127.0.0.1:8000/accounts/register/

#####Retrieve JWT (JSON web token):
curl -X POST -H "Content-Type: application/json" -d '{"username": "*USERNAME*", "password": "*PASSWORD*"}' http://127.0.0.1:8000/accounts/api-token-auth/

#####Place JWT in header for further API calls:
curl -H "Authorization: JWT *TOKEN*" http://127.0.0.1:8000/todo/1/?username=*USERNAME*
