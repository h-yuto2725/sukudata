from django.db import models
from import_export import resources

class Role(models.Model):
    roleid = models.CharField(max_length=10,primary_key=True)
    rolename = models.CharField(max_length=10)

    def __str__(self):
        return '<Role:roleid=' + str(self.roleid) + ', ' + self.rolename + '>'

class User(models.Model):
    userid = models.CharField(max_length=10,primary_key=True)
    mail = models.EmailField(max_length=200)
    roleid = models.ForeignKey(Role, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return '<User:userid=' + str(self.userid) + ', ' + self.username + '>'

class Group(models.Model):
    groupid = models.CharField(max_length=10,primary_key=True)
    groupname = models.CharField(max_length=100)

    def __str__(self):
        return '<Group:groupid=' + str(self.groupid) + ', ' + self.groupname + '>'

class GroupDetails(models.Model):
    groupid = models.ForeignKey(Group, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '<GroupDetails:id=' + str(self.id) + ', ' + str(self.userid) + ':' + str(self.groupid) + '>'

class Class(models.Model):
    classid = models.CharField(max_length=10,primary_key=True)
    classname = models.CharField(max_length=100)

    def __str__(self):
        return '<Class:classid=' + str(self.classid) + ', ' + self.classname + '>'

class ClassDetails(models.Model):
    classid = models.ForeignKey(Class, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '<ClassDetails:id=' + str(self.id) + ', ' + str(self.userid) + ':' + str(self.classid) + '>'

class Timetable(models.Model):
    title = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    color = models.CharField(max_length=10)
    details = models.CharField(max_length=100)
    classid = models.ForeignKey(Class, on_delete=models.CASCADE)
    
    def __str__(self):
        return '<Timetable:title=' + str(self.title) + ', ' + self.details + '>'

    class Meta:
        unique_together = ('start', 'classid')

class Schedule(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    color = models.CharField(max_length=10)
    details = models.CharField(max_length=100)
    
    def __str__(self):
        return '<Schedule:title=' + str(self.title) + ', ' + str(self.userid) + '>'

class GroupSchedule(models.Model):
    groupid = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    color = models.CharField(max_length=10)
    details = models.CharField(max_length=100)
    
    def __str__(self):
        return '<GroupSchedule:title=' + str(self.title) + ', ' + str(self.groupid) + '>'

class Event(models.Model):
    classid = models.ForeignKey(Class, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    details = models.CharField(max_length=100)#なくなる予定
    
    def __str__(self):
        return '<Event:title=' + str(self.title) + ', ' + str(self.classid) + '>'

class Todo(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return '<Todo:title=' + str(self.title) + ', ' + str(self.userid) + '>'