from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

def todo_list(request):
    return HttpResponse("This is the todo list view.")


class ToDoListView(View):
    def get(self, request):
        return HttpResponse("This is the todo list view.")
    def post(self, request):
        return HttpResponse("form submitted successfully")