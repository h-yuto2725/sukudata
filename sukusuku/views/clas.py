from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import Class
import json


def find(request): #全件表示
    data = list(Class.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def create(request): #
    classid = request.GET['classid']
    classname = request.GET['classname']
    
    classadd = Class(classid=classid,classname=classname)
    classadd.save()

    data = list(Class.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)

def delete(request):
    classid = request.GET['classid']

    classdel = Class.objects.get(classid=classid)
    classdel.delete()
    
    data = list(Class.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)