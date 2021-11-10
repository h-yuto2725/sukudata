from django.contrib import admin
from django.urls import path
from .views import login
from .views import student,subject

urlpatterns = [
    #学生
    path('', login.index , name='index'), #mailで検索
    path('find/', login.find , name='find'), #useridで検索
    path('stadd/',student.create,name='stadd'),
    path('stdel/',student.delete,name='stdel'),
    #科目
    path('sball/',subject.find,name='sball'),
    path('sbadd/',subject.create,name='sbadd'),
    path('sbdel/',subject.delete,name='sbdel'),
]   