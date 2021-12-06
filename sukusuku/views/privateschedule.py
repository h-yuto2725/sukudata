from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import Schedule,User
import json

# Create your views here.
def find(request): #学籍番号で検索を行いJsonファイルでschedule情報を表示する
    userid = request.GET['userid']
    useridtemp = User.objects.get(userid=userid)
    data = list(Schedule.objects.filter(userid=userid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    print(json_str)
    return HttpResponse(json_str)

def create(request):
    userid = request.GET['userid']
    title = request.GET['title']
    start = request.GET['start']
    end = request.GET['end']
    color = request.GET['color']
    details = request.GET['details']
    useridtemp = User.objects.get(userid=userid)
    schedules = Schedule(userid=useridtemp,title=title,start=start,end=end,color=color,details=details)
    schedules.save()

    data = list(Schedule.objects.filter(userid=userid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def delete(request):
    userid = request.GET['userid']
    scheduleid = request.GET['scheduleid']
    schedule = Schedule.objects.get(id=scheduleid)
    schedule.delete()

    data = list(Schedule.objects.filter(userid=userid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)