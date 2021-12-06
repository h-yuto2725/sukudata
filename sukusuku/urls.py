from django.contrib import admin
from django.urls import path
from .views import login,student,group
from .views import subject
from .views import privateschedule,groupschedule,todo

urlpatterns = [
    #学生
    path('', login.index , name='index'), #mailで検索
    path('stsel/', student.find , name='find'), 
    path('stadd/',student.create,name='stadd'),
    path('stdel/',student.delete,name='stdel'),
    #科目
    #path('sball/',subject.find,name='sball'),
    path('sbadd/',subject.create,name='sbadd'),
    #path('sbdel/',subject.delete,name='sbdel'),
    #グループ
    path('glall/',group.find,name='glall'),
    path('gladd/',group.create,name='gladd'),
    path('gldel/',group.delete,name='gldel'),
    #プライベートスケジュール
    path('pssel/',privateschedule.create,name='pssel'),
    path('psadd/',privateschedule.create,name='psadd'),
    path('psdel/',privateschedule.delete,name='psdel'),
    #グループスケジュール
    path('gssel/',groupschedule.create,name='gssel'),
    path('gsadd/',groupschedule.create,name='gsadd'),
    path('gsdel/',groupschedule.delete,name='gsdel'),
    #Todo
    path('tdsel/',todo.create,name='tdsel'),
    path('tddel/',todo.delete,name='tddel'),
]   