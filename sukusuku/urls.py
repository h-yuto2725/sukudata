from django.contrib import admin
from django.urls import path
from .views import login,student,group
from .views import subject

urlpatterns = [
    #学生
    path('', login.index , name='index'), #mailで検索
    path('stsel/', student.find , name='find'), 
    path('stadd/',student.create,name='stadd'),
    path('stdel/',student.delete,name='stdel'),
    #科目
    #path('sball/',subject.find,name='sball'),
    path('ttadd/',subject.ttadd,name='ttadd'),
    #path('sbdel/',subject.delete,name='sbdel'),
    #グループ
    path('glall/',group.find,name='glall'),
    path('gladd/',group.create,name='gladd'),
    path('gldel/',group.delete,name='gldel'),

]   