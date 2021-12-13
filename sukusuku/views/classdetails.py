from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import ClassDetails,User,Class
import json


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

def create(request): 
    if request.method == 'POST':
        headers = ('title','start','end','color','classid','details')
        data = []
        df = pd.read_excel (request.body,sheet_name='Tablib Dataset',)
        for i in range(20):
            data.append([df.iat[i,0],df.iat[i,1],df.iat[i,2],df.iat[i,3],df.iat[i,4],df.iat[i,5]])
        classdetails_resource = resources.modelresource_factory(model=ClassDetails)()
        dataset = tablib.Dataset(*data, headers=headers)
        classdetails_resource.import_data(dataset)

        data = list(Timetable.objects.all().values())
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