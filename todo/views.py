from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Todo
import json 
from rest_framework.views import APIView
from rest_framework.response import Response

def todo_list(request):
    return HttpResponse("This is the todo list view.")


class ToDoListView(View):
    def get(self, request):
        todos = Todo.objects.all()
        context = {
            'todos': todos
        }
        return render(request, "todo_list.html", context  )

    def post(self, request):
        return HttpResponse("form submitted successfully")
    


# ...existing code...

# class ToDoListApiView(View):
#     def get(self, request):
#         todos = Todo.objects.all()
#         formatted_todo = []
#         for todo in todos:
#             formatted_todo.append({
#                 'id': todo.id,
#                 'title': todo.title,
#                 'description': todo.description,
#                 'completed': todo.completed,
#                 'created_at': todo.created_at.strftime('%Y/%m/%d %H:%M:%S'),
#                 'updated_at': todo.updated_at.strftime('%Y/%m/%d %H:%M:%S')
#             })
#         formatted_todo = json.dumps(formatted_todo, indent=4)    
#         return HttpResponse(formatted_todo, content_type="application/json")
# # ...existing code...

#     def post(self, request):
#         formatted_data = json.loads(request.body)
#         # Note: If 'title', 'description', or 'completed' are missing, this will raise KeyError
#         created_todo = Todo.objects.create(
#             title=formatted_data['title'],
#             description=formatted_data['description'],
#             completed=formatted_data['completed']
#         )
#         data_to_return = {
#             'id': created_todo.id,
#             'title': created_todo.title,
#             'description': created_todo.description,
#             'completed': created_todo.completed,
#             'created_at': created_todo.created_at.strftime('%Y/%m/%d %H:%M:%S'),
#             'updated_at': created_todo.updated_at.strftime('%Y/%m/%d %H:%M:%S')
#         }
#         data_to_return = json.dumps(data_to_return, indent=4)
#         return HttpResponse(data_to_return, content_type="application/json")
  
from rest_framework.serializers import ModelSerializer
class TodoSerializers(ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "description", "completed", "created_at", "updated_at"]
        
         
class ToDoListApiView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        formatted_todo = TodoSerializers(todos, many=True).data  
        return Response(formatted_todo)


    def post(self, request):
        # formatted_data = json.loads(request.body)
        formatted_data = request.data  # Use request.data for DRF
        
        serializer = TodoSerializers(data=formatted_data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
       
       
        return Response(serializer.errors)  # Return validation errors if any
    