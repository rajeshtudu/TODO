"""TODO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from todo_app import views

urlpatterns = [
    path(
        "",
        views.todo_list,
        name="todo-list",
    ),
    path(
        "todo-create/",
        views.todo_create,
        name="todo-create",
    ),
    path(
        "todo-delete/<int:pk>/",
        views.todo_delete,
        name="todo-delete",
    ),
    path(
        "todo-update/<int:pk>/",
        views.todo_update,
        name="todo-update",
    ),
]
