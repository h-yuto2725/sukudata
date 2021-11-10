from django.contrib import admin
from django.urls import path
from .views import login
from .views import student

urlpatterns = [

    path('', login.index , name='index'),
    path('find/', login.find , name='find'),
    path('stadd/',student.create,name='stadd'),
    path('stdel/',student.delete,name='stdel'),
]   