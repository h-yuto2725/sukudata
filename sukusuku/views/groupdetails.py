from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import GroupDetails,Group,User
import json

# Create your views here.

def find(request):
    userid = request.GET['userid'] 
    data = list(GroupDetails.objects.filter(userid = userid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def allfind(request):
    groupid = request.GET['groupid']
    data = list(GroupDetails.objects.filter(groupid = groupid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def create(request): 
    groupid = request.GET['groupid']
    userid = request.GET['userid']
    groupidtemp = Group.objects.get(groupid=groupid)
    useridtemp = User.objects.get(userid=userid)
    groupdetails = GroupDetails(groupid=groupidtemp,userid=useridtemp)
    groupdetails.save()

    data = list(GroupDetails.objects.filter(groupid=groupidtemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def delete(request):
    userid = request.GET['userid']
    groupid = request.GET['groupid']
    groupidtemp = Group.objects.get(groupid=groupid)
    useridtemp = User.objects.get(userid=userid)
    groupdetails = GroupDetails.objects.get(groupid=groupidtemp,userid=useridtemp)
    groupdetails.delete()

    data = list(GroupDetails.objects.filter(groupid=groupidtemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)