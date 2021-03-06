from django.contrib import admin
from django.urls import path
from .views import login, student, teacher, group
from .views import timetable
from .views import privateschedule, groupschedule, todo
from .views import clas, classdetails, event
from .views import privateschedule, groupschedule, todo, groupdetails
from .views import thread, comment

urlpatterns = [
    # 学生
    path('', login.index, name='index'),  # mailで検索
    path('stsel/', student.find, name='find'),
    path('stsel2/', student.find2, name='find2'),
    path('stsel/', student.find, name='find'),
    path('stadd/', student.create, name='stadd'),
    path('stdel/', student.delete, name='stdel'),
    path('usadd/', student.useradd, name='usadd'),
    # 管理者
    path('trsel/', teacher.find, name='find'),
    path('tradd/', teacher.create, name='tradd'),
    path('trdel/', teacher.delete, name='trdel'),
    # 時間割登録
    path('ttsel/', timetable.ttsel, name='ttsel'),
    path('ttadd/', timetable.ttadd, name='ttadd'),
    path('ttcreate/', timetable.ttcreate, name='ttcreate'),
    path('ttupd/', timetable.ttupd, name='ttupd'),
    path('ttdel/', timetable.ttdel, name='ttdel'),
    # グループ
    path('glall/', group.find, name='glall'),
    path('glsel/', group.gsel, name='glsel'),
    path('gladd/', group.create, name='gladd'),
    path('glupd/', group.update, name='glupd'),
    path('gldel/', group.delete, name='gldel'),
    # クラス
    path('clall/', clas.find, name='clall'),
    path('cladd/', clas.create, name='cladd'),
    path('cldel/', clas.delete, name='cldel'),
    # クラス詳細
    path('cdselu/', classdetails.find1, name='cdselu'),
    path('cdselc/', classdetails.find2, name='cdselc'),
    path('cdadd/', classdetails.create, name='cdadd'),
    path('cdadd1/', classdetails.create1, name='cdadd1'),
    path('cddel/', classdetails.delete, name='cddel'),
    # プライベートスケジュール
    path('pssel/', privateschedule.find, name='pssel'),
    path('psadd/', privateschedule.create, name='psadd'),
    path('psupd/', privateschedule.update, name='psupd'),
    path('psdel/', privateschedule.delete, name='psdel'),
    # グループスケジュール
    path('gssel/', groupschedule.find, name='gssel'),
    path('gsadd/', groupschedule.create, name='gsadd'),
    path('gsupd/', groupschedule.update, name='gsupd'),
    path('gsdel/', groupschedule.delete, name='gsdel'),
    # Todo
    path('tdsel/', todo.find, name='tdsel'),
    path('tdadd/', todo.create, name='tdadd'),
    path('tddone/', todo.done, name='tddone'),
    path('tddel/', todo.delete, name='tddel'),
    # イベント
    path('evall/', event.findall, name='evall'),
    path('evsel/', event.find, name='evsel'),
    path('evadd/', event.create, name='evadd'),
    path('evdel/', event.delete, name='evdel'),
    # グループ詳細
    path('gdsel/', groupdetails.find, name='gdsel'),
    path('gdall/', groupdetails.allfind, name='gdall'),
    path('gdadd/', groupdetails.create, name='gdadd'),
    path('gddel/', groupdetails.delete, name='gddel'),
    # 掲示板
    path('thsel/', thread.select, name='thsel'),
    path('thsrc/', thread.search, name='thsrc'),
    path('thadd/', thread.create, name='thadd'),
    path('thapp/', thread.approve, name='thapp'),
    path('threj/', thread.reject, name='threj'),
    path('thdel/', thread.delete, name='thdel'),
    # コメント
    path('cmsel/', comment.select, name='cmsel'),
    path('cmadd/', comment.create, name='cmadd'),
    path('cmdel/', comment.delete, name='cmdel'),
    # 通知
    path('noticesel/',timetable.noticesel,name='noticesel'),
    path('threadnoticesel/',thread.threadnotice,name='threadnoticesel'),
]
