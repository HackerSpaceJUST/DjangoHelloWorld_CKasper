from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, "newyear/index.html", {
        "newyear": isNewYear()
    })

def isNewYear():
    now = datetime.now()
    return now.month == 1 and now.day == 1
