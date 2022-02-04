from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import Event, Class
import json


def find(request):  # メールアドレスで検索を行いJsonファイルでuser情報を表示する。
    classid = request.GET['classid']
    classtemp = Class.objects.get(classid=classid)

    data = list(Event.objects.filter(classid=classtemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def findall(request):  # メールアドレスで検索を行いJsonファイルでuser情報を表示する。
    data = list(Event.objects.all().values('id', 'classid',
                'title', 'end', 'details', 'classid__classname'))
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def create(request):  # メールアドレスで検索を行いJsonファイルでuser情報を表示する。
    classid = request.GET['classid']
    classtemp = Class.objects.get(classid=classid)
    eventname = request.GET['eventname']
    eventdetails = request.GET['eventdetails']
    end = request.GET['end']

    event = Event(classid=classtemp, title=eventname,
                  details=eventdetails, end=end)
    event.save()

    data = list(Event.objects.all().values('id', 'classid',
                'title', 'end', 'details', 'classid__classname'))
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def delete(request):
    evid = request.GET['id']

    event = Event.objects.get(id=evid)
    event.delete()

    data = list(Event.objects.all().values('id', 'classid',
                'title', 'end', 'details', 'classid__classname'))
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)
