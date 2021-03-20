from django.urls import path
from . import views


urlpatterns =  [
    path("", views.home, name="home"),
    path("hello/", views.helloWorld, name="helloWorld"),
    path("hello/<str:name>", views.sayHello, name="sayHello")
]