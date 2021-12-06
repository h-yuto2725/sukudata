from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import Todo
import json

# Create your views here.
def create(request):
    userid = request.GET['userid']
    title = request.GET['title']
    done = request.GET['done']
    todotemp = Todo.objects.get(id=id)
    todo = Todo(userid=userid,title=title,done=done)
    todo.save()

    data = list(Todo.filter(userid=userid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def delete(request):
    id = request.GET['id']
    todo = Todo.objects.get(id=id)
    todo.delete()

    data = list(Todo.filter(id=id).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)