from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import GroupSchedule, Group
import json

# Create your views here.


def find(request):  # groupidで検索を行いJsonファイルでgroupschedule情報を表示する
    groupid = request.GET['groupid']
    data = list(GroupSchedule.objects.filter(groupid=groupid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def create(request):
    groupid = request.GET['groupid']
    title = request.GET['title']
    start = request.GET['start']
    end = request.GET['end']
    color = request.GET['color']
    details = request.GET['details']
    groupidtemp = Group.objects.get(groupid=groupid)
    groupschedules = GroupSchedule(
        groupid=groupidtemp, title=title, start=start, end=end, color=color, details=details)
    groupschedules.save()

    data = list(GroupSchedule.objects.filter(groupid=groupid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def update(request):
    scheduleid = request.GET['id']
    groupid = request.GET['groupid']
    title = request.GET['title']
    start = request.GET['start']
    end = request.GET['end']
    color = request.GET['color']
    details = request.GET['details']
    groupidtemp = Group.objects.get(groupid=groupid)
    groupschedules = GroupSchedule(id=scheduleid, groupid=groupidtemp,
                                   title=title, start=start, end=end, color=color, details=details)
    groupschedules.save()

    data = list(GroupSchedule.objects.filter(groupid=groupid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def delete(request):
    groupid = request.GET['groupid']
    groupscheduleid = request.GET['id']
    groupschedule = GroupSchedule.objects.get(id=groupscheduleid)
    groupschedule.delete()

    data = list(GroupSchedule.objects.filter(groupid=groupid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)
