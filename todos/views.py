from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.

from todos.models import TodoList


class TodoListView(ListView):
    model = TodoList
    template_name = "todos/list.html"


class TodoDetailView(DetailView):
    model = TodoList
    template_name = "todos/detail.html"