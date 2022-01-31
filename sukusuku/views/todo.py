from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import Todo,User
import json

# Create your views here.
def find(request): #学籍番号で検索を行いJsonファイルでschedule情報を表示する
    userid = request.GET['userid']
    useridtemp = User.objects.get(userid=userid)
    data = list(Todo.objects.filter(userid=useridtemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def create(request):
    userid = request.GET['userid']
    title = request.GET['title']
    done = request.GET['done']
    date = request.GET['date']
    useridtemp = User.objects.get(userid=userid)
    todo = Todo(userid=useridtemp,title=title,done=done,date=date)
    todo.save()

    data = list(Todo.objects.filter(userid=userid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def done(request):
    todoid = request.GET['id']
    userid = request.GET['userid']
    done = request.GET['done']
    useridtemp = User.objects.get(userid=userid)
    todo = Todo(id=todoid,userid=useridtemp,done=done)
    todo.save()

    data = list(Todo.objects.filter(id=todoid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def delete(request):
    tdid = request.GET['tdid']
    userid = request.GET['userid']
    useridtemp = User.objects.get(userid=userid)
    todo = Todo.objects.get(id=tdid)
    todo.delete()

    data = list(Todo.objects.filter(userid=useridtemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)