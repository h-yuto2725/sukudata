from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import User,Roll
import json

# Create your views here.

def create(request): #メールアドレスで検索を行いJsonファイルでuser情報を表示する。
    mail = request.GET['mail']
    userid = request.GET['userid']
    roll = request.GET['rollid_id']  
    username = request.GET['username']
    rolltemp = Roll.objects.get(rollid=roll)
    users = User(userid=userid,mail=mail,rollid=rolltemp,username=username)
    users.save()

    data = list(User.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def delete(request):
    userid = request.GET['userid']
    user = User.objects.get(userid=userid)
    user.delete()

    data = list(User.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)