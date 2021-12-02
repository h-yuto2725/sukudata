from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import GroupSchedule
import json

# Create your views here.
def find(request): #学籍番号で検索を行いJsonファイルでgroupschedule情報を表示する
    groupid = request.GET['groupid']
    data = list(GroupSchedule.filter(groupid=groupid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def create(request):
    groupid = request.GET['groupid']
    title = request.GET['title']
    start = request.GET['start']
    end = request.GET['end']
    color = request.GET['color']
    details = request.GET['details']
    groupschedules = GroupSchedule(groupid=groupid,title=title,start=start,end=end,color=color,details=details)
    groupschedules.save()

    data = list(GroupSchedule.filter(userid=userid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def delete(request):
    groupid = request.GET['groupid']
    groupscheduleid = request.GET['groupscheduleid']
    groupschedule = GroupSchedule.objects.get(id=groupscheduleid)
    groupschedule.delete()

    data = list(GroupSchedule.filter(groupid=groupid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)