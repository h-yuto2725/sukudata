from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import Group
import json

# Create your views here.

def find(request): 
    data = list(Group.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def gsel(request): 
    groupid = request.GET['groupid']
    data = list(Group.objects.filter(groupid=groupid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def create(request): 
    groupid = request.GET['groupid']
    groupname = request.GET['groupname']
    group = Group(groupid=groupid,groupname=groupname)
    group.save()

    data = list(Group.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def delete(request):
    groupid = request.GET['groupid']
    group = Group.objects.get(groupid=groupid)
    group.delete()

    data = list(Group.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)