from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

from todos.models import TodoItem, TodoList


class TodoListView(ListView):
    model = TodoList
    template_name = "todos/list.html"


class TodoDetailView(DetailView):
    model = TodoList
    template_name = "todos/detail.html"


class TodoCreateView(CreateView):
    model = TodoList
    template_name = "todos/create.html"
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("show_todolist", args=[self.object.id])


class TodoUpdateView(UpdateView):
    model = TodoList
    template_name = "todos/edit.html"
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("show_todolist", args=[self.object.id])


class TodoDeleteView(DeleteView):
    model = TodoList
    template_name = "todos/delete.html"
    success_url = reverse_lazy("list_todos")


class TodoItemCreateView(CreateView):
    model = TodoItem
    template_name = "todo_items/create.html"
    fields = ["task", "due_date", "is_completed", "list"]

    def get_success_url(self):
        return reverse_lazy("show_todolist", args=[self.object.list.id])