#select,create,delete
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import Comment,Thread,User
import json

# Create your views here.
def select(request):
    threadid = request.GET['threadid']
    threadtemp = Thread.objects.get(threadid=threadid)

    data = list(Comment.objects.filter(thread_id=threadtemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def create(request): #メールアドレスで検索を行いJsonファイルでuser情報を表示する。
    thread = request.GET['thread']
    user = request.GET['user']
    name = request.GET['name']
    comment = request.GET['comment']
    flag = request.GET['flag']
    threadtemp = Thread.objects.get(threadid=thread)
    usertemp = User.objects.get(userid=user)
    comment = Comment(thread=threadtemp,user=usertemp,name=name,comment=comment,flag=flag)
    comment.save()

    data = list(Comment.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def delete(request):
    thread = request.GET['thread']
    user = request.GET['user']
    name = request.GET['name']
    comment = request.GET['comment']
    flag = request.GET['flag']
    threadtemp = Thread.objects.get(threadid=thread)
    usertemp = User.objects.get(userid=user)
    comment = Comment(thread=threadtemp,user=usertemp,name=name,comment=comment,flag=flag)
    comment.save()

    data = list(Comment.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)