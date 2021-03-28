from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .forms import NewTaskForm
from .models import Task

def index(request):
    tasks = Task.objects.all()

    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:index")
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })

def task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        form = NewTaskForm(instance=task)
        return render(request, "tasks/task.html", {
            "task": task,
            "form": form
        })
    except:
        return HttpResponseBadRequest("Task not found")

def update(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(pk=task_id)
        form = NewTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:task", task_id=task_id)
        else:
            return render(request, "tasks/task.html", {
                "task": task,
                "form": form
            })
    else:
        return HttpResponseBadRequest("Invalid Method")