from django.contrib import admin
from django.urls import path
from .views import login,student,teacher,group
from .views import subject
from .views import privateschedule,groupschedule,todo,groupdetails

urlpatterns = [
    #学生
    path('', login.index , name='index'), #mailで検索
    path('stsel/', student.find , name='find'), 
    path('stadd/',student.create,name='stadd'),
    path('stdel/',student.delete,name='stdel'),
    #管理者
    path('trsel/',teacher.find , name='find'), 
    path('tradd/',teacher.create,name='tradd'),
    path('rtdel/',teacher.delete,name='trdel'),
    #時間割登録
    path('ttadd/',subject.ttadd,name='ttadd'),
    #グループ
    path('glall/',group.find,name='glall'),
    path('gladd/',group.create,name='gladd'),
    path('gldel/',group.delete,name='gldel'),
    #プライベートスケジュール
    path('pssel/',privateschedule.find,name='pssel'),
    path('psadd/',privateschedule.create,name='psadd'),
    path('psupd/',privateschedule.update,name='psupd'),
    path('psdel/',privateschedule.delete,name='psdel'),
    #グループスケジュール
    path('gssel/',groupschedule.find,name='gssel'),
    path('gsadd/',groupschedule.create,name='gsadd'),
    path('gsupd/',groupschedule.update,name='gsupd'),
    path('gsdel/',groupschedule.delete,name='gsdel'),
    #Todo
    path('tdsel/',todo.find,name='tdsel'),
    path('tdadd/',todo.create,name='tdadd'),
    path('tddel/',todo.delete,name='tddel'),
    #グループ詳細
    path('gdsel/',groupdetails.find,name='gdsel'),
    path('gdadd/',groupdetails.create,name='gdadd'),
    path('gddel/',groupdetails.delete,name='gddel'),
]   