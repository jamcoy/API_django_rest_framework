from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from todo.views import TodoView
from accounts.views import RegistrationView
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todo/$', TodoView.as_view()),
    url(r'^todo/(?P<pk>[0-9]+)/$', TodoView.as_view()),
    url(r'^accounts/register/$', RegistrationView.as_view()),
    url(r'^accounts/api-token-auth/$', obtain_jwt_token),
    url(r'^docs/', include('rest_framework_docs.urls'))
]
