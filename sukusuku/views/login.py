from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import User,Role
import json

# Create your views here.

def index(request): #メールアドレスで検索を行いJsonファイルでuser情報を表示する。
    if 'email' in request.GET:
        email = request.GET['email']
        data = list(User.objects.filter(mail__contains=email).values())
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        return HttpResponse(json_str)

    else:
        data = list(User.objects.all().values())
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        return HttpResponse(json_str)

def find(request):
    if 'userid' in request.GET:
        userid = request.GET['userid']
        data = list(User.objects.filter(userid__contains=userid).values())
        json_str = json.dumps(data, ensure_ascii=False, indent=2) 
        return HttpResponse(json_str)

    else:
        data = list(User.objects.all().values())
        json_str = json.dumps(data, ensure_ascii=False, indent=2) 
        return HttpResponse(json_str)  

