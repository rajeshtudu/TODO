from django.shortcuts import render, HttpResponseRedirect
from todo_app.models import Todo

# CRUD
# C => CREATE
# R => READ / RETRIEVE
# U => UPDATE
# D => DELETE


def todo_list(request):
    todos = Todo.objects.all()
    return render(
        request=request,
        template_name="bootstrap/todo_list.html",
        context={"todos": todos},
    )


def todo_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        # ORM => Object Relational Mapping
        Todo.objects.create(title=title)
        return HttpResponseRedirect("/")
    return render(request, "bootstrap/todo_create.html")


def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)  # pk is primary key (id)
    todo.delete()
    return HttpResponseRedirect("/")


def todo_update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        title = request.POST["title"]
        todo.title = title
        todo.save()
        return HttpResponseRedirect("/")
    else:
        return render(
            request,
            "bootstrap/todo_update.html",
            {"todo": todo},
        )