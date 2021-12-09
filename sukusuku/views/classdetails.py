from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import ClassDetails,User,Class
import json


def find(request): 
    userid = request.GET['userid']
    usertemp =  User.objects.get(userid=userid)

    data = list(ClassDetails.objects.filter(userid=usertemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def create(request): 
    classid = request.GET['classid']
    classtemp = Class.objects.get(classid=classid)
    userid = request.GET['userid']
    usertemp =  User.objects.get(userid=userid)
    
    classdetails = Class(classid=classtemp,userid=usertemp)
    classdetails.save()

    data = list(ClassDetails.objects.filter(userid=usertemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)

def delete(request):
    cdid = request.GET['id']
    userid = request.GET['userid']
    usertemp =  User.objects.get(userid=userid)

    classdetails = ClassDetails.objects.get(id=cdid)
    classdetails.delete()
    
    data = list(ClassDetails.objects.filter(userid=usertemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)