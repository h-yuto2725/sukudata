#select,search,create,apply,reject,delete
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import Thread,User
import json

# Create your views here.
'''def find(request): #メールアドレスで検索を行いJsonファイルでuser情報を表示する。
    data = list(User.objects.filter(userid__contains='st').values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)'''

def select(request):
    try:
        thid = request.GET['threadid']
        threadtemp = Thread.objects.get(threadid=thid)
        data = list(Thread.objects.filter(threadid=threadtemp.threadid).values())
    except Exception:
        data = list(Thread.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)

def search(request):
    #キーワードが複数の可能性がある
    try:
        kw = request.GET['title']
        data = list(Thread.objects.filter(title__contains=kw).values())
    except Exception:
        data = list(Thread.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)

'''def create(request): #メールアドレスで検索を行いJsonファイルでuser情報を表示する。
    mail = request.GET['mail']
    userid = request.GET['userid']
    role = request.GET['roleid_id']  
    username = request.GET['username']
    roletemp = Role.objects.get(roleid=role)
    users = User(userid=userid,mail=mail,roleid=roletemp,username=username)
    users.save()

    data = list(User.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)'''

def create(request):
    title = request.GET['title']
    flag = request.GET['flag']
    note = request.GET['note']
    master = request.GET['master']
    usertemp = User.objects.get(userid=master)
    thread = Thread(title=title,flag=flag,note=note,master=usertemp)
    thread.save()

    data = list(Thread.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

'''def delete(request):
    userid = request.GET['userid']
    user = User.objects.get(userid=userid)
    user.delete()

    data = list(User.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)'''

'''def update(request):
    scheduleid = request.GET['id']
    userid = request.GET['userid']
    title = request.GET['title']
    start = request.GET['start']
    end = request.GET['end']
    color = request.GET['color']
    details = request.GET['details']
    useridtemp = User.objects.get(userid=userid)
    schedules = Schedule(id=scheduleid,userid=useridtemp,title=title,start=start,end=end,color=color,details=details)
    schedules.save()

    data = list(Schedule.objects.filter(userid=userid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)'''

def approve(request):
    threadid = request.GET['threadid']
    title = request.GET['title']
    flag = request.GET['flag']
    note = request.GET['note']
    master = request.GET['master']
    usertemp = User.objects.get(userid=master)
    thread = Thread(threadid=threadid,title=title,flag=flag,note=note,master=usertemp)
    thread.save()

    data = list(Thread.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def reject(request):
    threadid = request.GET['threadid']
    thread = Thread.objects.get(threadid=threadid)
    thread.delete()

    data = list(Thread.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)

def delete(request):
    threadid = request.GET['threadid']
    title = request.GET['title']
    flag = request.GET['flag']
    note = request.GET['note']
    master = request.GET['master']
    usertemp = User.objects.get(userid=master)
    thread = Thread(threadid=threadid,title=title,flag=flag,note=note,master=usertemp)
    thread.save()

    data = list(Thread.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)