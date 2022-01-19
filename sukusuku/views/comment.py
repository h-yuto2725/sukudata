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

    data = list(Comment.objects.filter(thread_id=threadtemp).values('id','thread_id','user','user__username','comment','flag'))
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def create(request): #メールアドレスで検索を行いJsonファイルでuser情報を表示する。
    thread = request.GET['thread']
    user = request.GET['user']
    comment = request.GET['comment']
    flag = request.GET['flag']
    threadtemp = Thread.objects.get(threadid=thread)
    usertemp = User.objects.get(userid=user)
    comment = Comment(thread=threadtemp,user=usertemp,comment=comment,flag=flag)
    comment.save()

    data = list(Comment.objects.filter(thread_id=threadtemp).values('id','thread_id','user','user__username','comment','flag'))
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def delete(request):
    commentid = request.GET['id']
    threadtemp = request.GET['thread']
    ctemp = Comment.objects.get(id=commentid)
    comment = Comment(id=commentid,thread=ctemp.thread,user=ctemp.user,comment=ctemp.comment,flag=False)
    comment.save()

    data = list(Comment.objects.filter(thread_id=threadtemp).values('id','thread_id','user','user__username','comment','flag'))
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)