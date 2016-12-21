from django.conf.urls import url
from django.contrib import admin
from todo.views import TodoView
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todo/$', TodoView.as_view()),
    url(r'^todo/(?P<pk>[0-9]+)/$', TodoView.as_view())
]
