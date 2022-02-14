from datetime import date, datetime, time, timedelta
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from ..models import Timetable, Class,Notice
from import_export import resources
from django.views.decorators.csrf import csrf_exempt
import json
import tablib
import pandas as pd


@csrf_exempt
def ttadd(request):
    if request.method == 'POST':
        headers = ('title', 'start', 'end', 'color',
                   'classid', 'details', 'timed')
        data = []
        df = pd.read_excel(request.body, sheet_name='Tablib Dataset',)
        classid = df.iat[0,4]
        for i in range(len(df)):
            data.append([df.iat[i, 0], df.iat[i, 1], df.iat[i, 2],
                        df.iat[i, 3], df.iat[i, 4], df.iat[i, 5], df.iat[i, 6]])
        timetable_resource = resources.modelresource_factory(model=Timetable)()
        dataset = tablib.Dataset(*data, headers=headers)
        timetable_resource.import_data(dataset)

        classidtemp = Class.objects.get(classid=df.iat[0,4])
        uptime = datetime.now().strftime('%Y-%m-%dT%H:%M')
        details = '時間割が一括追加されました。'

        notice = Notice(uptime=uptime,classid=classidtemp,details=details)
        notice.save()

        data = list(Timetable.objects.filter(classid=classidtemp).values())
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        return HttpResponse(json_str)


def ttcreate(request):
    title = request.GET['title']
    start = request.GET['start']
    end = request.GET['end']
    color = request.GET['color']
    classid = request.GET['classid']
    details = request.GET['details']
    timed = request.GET['timed']

    uptime = request.GET['uptime']

    classidtemp = Class.objects.get(classid=classid)
    timetable = Timetable(title=title, start=start, end=end, color=color,
                          details=details, classid=classidtemp, timed=timed)
    timetable.save()

    start = start[0:16] + 'の時間割が追加されました。'

    notice = Notice(uptime=uptime,classid=classidtemp,details=start)
    notice.save()

    data = list(Timetable.objects.filter(classid=classidtemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def ttupd(request):
    ttid = request.GET['id']
    title = request.GET['title']
    start = request.GET['start']
    end = request.GET['end']
    color = request.GET['color']
    classid = request.GET['classid']
    details = request.GET['details']
    timed = request.GET['timed']

    uptime = request.GET['uptime']

    classidtemp = Class.objects.get(classid=classid)
    timetable = Timetable(id=ttid, title=title, start=start, end=end,
                          color=color, details=details, classid=classidtemp, timed=timed)
    timetable.save()

    start = start[0:16] + 'の時間割が変更されました。'

    notice = Notice(uptime=uptime,classid=classidtemp,details=start)
    notice.save()

    data = list(Timetable.objects.filter(classid=classidtemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def ttsel(request):
    classid = request.GET['classid']
    classtemp = Class.objects.get(classid=classid)
    data = list(Timetable.objects.filter(classid=classtemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def ttdel(request):
    ttid = request.GET['id']
    classid = request.GET['classid']
    classtemp = Class.objects.get(classid=classid)

    timetable = Timetable.objects.get(id=ttid)
    timetable.delete()

    data = list(Timetable.objects.filter(classid=classtemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)

def noticesel(request):                 
    classid = request.GET['classid']
    classtemp = Class.objects.get(classid=classid)

    data = list(Notice.objects.filter(classid=classtemp).values()[:10])
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


    