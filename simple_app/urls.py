from django.urls import path
from . import views

app_name = 'simple_app'
urlpatterns =  [
    path("", views.index, name="index"),
    path("hello/", views.helloWorld, name="helloWorld"),
    path("hello/<str:name>", views.sayHello, name="sayHello")
]