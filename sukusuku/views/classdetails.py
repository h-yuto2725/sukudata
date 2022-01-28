from django.shortcuts import render
from django.http import HttpResponse
from ..models import ClassDetails,User,Class
from django.views.decorators.csrf import csrf_exempt
import json
from import_export import resources
import tablib
import pandas as pd


def find1(request): 
    userid = request.GET['userid']
    usertemp =  User.objects.get(userid=userid)

    data = list(ClassDetails.objects.filter(userid=usertemp).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)

def find2(request): 
    classid = request.GET['classid']
    classtemp = Class.objects.get(classid=classid)

    data = list(ClassDetails.objects.filter(classid=classtemp).values('id','userid','classid','userid__username'))
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)

@csrf_exempt
def create(request): 
    if request.method == 'POST':
        headers = ('classid','userid')
        data = []
        df = pd.read_excel (request.body,sheet_name='Tablib Dataset',)
        for i in range(len(df)):
            data.append([df.iat[i,0],df.iat[i,1]])
        classdetails_resource = resources.modelresource_factory(model=ClassDetails)()
        dataset = tablib.Dataset(*data, headers=headers)
        classdetails_resource.import_data(dataset)
        
        data = list(ClassDetails.objects.all().values())
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        return HttpResponse(json_str)

def create1(request): #1は一人追加するの1
    classid = request.GET['classid']
    userid = request.GET['userid'] 
    classtemp =  Class.objects.get(classid=classid)
    usertemp =  User.objects.get(userid=userid)
    cd = ClassDetails(classid=classtemp,userid=usertemp)
    cd.save()

    data = list(ClassDetails.objects.filter(classid=classtemp).values('id','userid','classid','userid__username'))
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)

def delete(request):
    cdid = request.GET['id']
    classid = request.GET['classid']
    classtemp =  Class.objects.get(classid=classid)

    classdetails = ClassDetails.objects.get(id=cdid)
    classdetails.delete()
    
    data = list(ClassDetails.objects.filter(classid=classtemp).values('id','userid','classid','userid__username'))
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)