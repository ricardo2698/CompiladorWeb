from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.hello_world,name ='Compiladores'),
    url(r'^saludo/', views.saludo,name ='Saludo'),
    url(r'^lenguaje/(?P<pk>[0-9]+)/$', views.detalleLenguaje),
]
