from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import Timetable,Class
from import_export import resources
import json
import tablib
import pandas as pd

# Create your views here.
def ttadd(request):
    if request.method == 'POST':
        headers = ('title','start','end','color','classid','details')
        data = []
        df = pd.read_excel (request.body,sheet_name='Tablib Dataset',)
        for i in range(20):
            data.append([df.iat[i,0],df.iat[i,1],df.iat[i,2],df.iat[i,3],df.iat[i,4],df.iat[i,5]])
        timetable_resource = resources.modelresource_factory(model=Timetable)()
        dataset = tablib.Dataset(*data, headers=headers)
        timetable_resource.import_data(dataset)

        data = list(Timetable.objects.all().values())
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        return HttpResponse(json_str)

def ttsel(request): 
    classid = request.GET['classid']
    classtemp = Class.objects.get(classid=classid)
    data = list(Timetable.objects.filter(classid = classtemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)



def ttdel(request):
    ttid = request.GET['id']
    timetable = Timetable.objects.get(id=ttid)
    timetable.delete()

    data = list(Subject.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)