from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import Subject
import json

# Create your views here.

def find(request): 
    data = list(Subject.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def create(request): #メールアドレスで検索を行いJsonファイルでuser情報を表示する。
    subjectid = request.GET['subjectid']
    subjectname = request.GET['subjectname']
    subjectnote = request.GET['subjectnote']
    subject = Subject(subjectid=subjectid,subjectname=subjectname,subjectnote=subjectnote)
    subject.save()

    data = list(Subject.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

def delete(request):
    subjectid = request.GET['subjectid']
    subject = Subject.objects.get(subjectid=subjectid)
    subject.delete()

    data = list(Subject.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)