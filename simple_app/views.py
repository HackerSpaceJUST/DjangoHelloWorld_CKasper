from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "hello/index.html")

def helloWorld(request):
    return HttpResponse("Hello World!")

def sayHello(request, name):
    return render(request, "hello/say_hello.html", {
        "name": name.capitalize()
    })
