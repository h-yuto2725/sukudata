from django.contrib import admin
from django.urls import path
from .views import login,student,teacher,group
from .views import timetable
from .views import privateschedule,groupschedule,todo
from .views import clas,classdetails,event
from .views import privateschedule,groupschedule,todo,groupdetails

urlpatterns = [
    #学生
    path('', login.index , name='index'), #mailで検索
    path('stsel/', student.find , name='find'), 
    path('stsel2/', student.find2 , name='find2'), 
    path('stadd/',student.create,name='stadd'),
    path('stdel/',student.delete,name='stdel'),
    #管理者
    path('trsel/',teacher.find , name='find'), 
    path('tradd/',teacher.create,name='tradd'),
    path('rtdel/',teacher.delete,name='trdel'),
    #時間割登録
    path('ttsel/',timetable.ttsel,name='ttsel'),
    path('ttadd/',timetable.ttadd,name='ttadd'),
    path('ttcreate/',timetable.ttcreate,name='ttcreate'),
    path('ttupd/',timetable.ttupd,name='ttupd'),
    path('ttdel/',timetable.ttdel,name='ttdel'),
    #グループ
    path('glall/',group.find,name='glall'),
    path('glsel/',group.gsel,name='glsel'),
    path('gladd/',group.create,name='gladd'),
    path('gldel/',group.delete,name='gldel'),
    #クラス
    path('clall/',clas.find,name='clall'),
    path('cladd/',clas.create,name='cladd'),
    path('cldel/',clas.delete,name='cldel'),
    #クラス詳細
    path('cdselu/',classdetails.find1,name='cdselu'),
    path('cdselc/',classdetails.find2,name='cdselc'),
    path('cdadd/',classdetails.create,name='cdadd'),
    path('cddel/',classdetails.delete,name='cddel'),
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
    #イベント
    path('evsel/',event.find,name='evsel'),
    path('evadd/',event.create,name='evadd'),
    path('evdel/',event.delete,name='evdel'),
    #グループ詳細
    path('gdsel/',groupdetails.find,name='gdsel'),
    path('gdall/',groupdetails.allfind,name='gdall'),
    path('gdadd/',groupdetails.create,name='gdadd'),
    path('gddel/',groupdetails.delete,name='gddel'),
]   