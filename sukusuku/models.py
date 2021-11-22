from django.db import models

class Roll(models.Model):
    rollid = models.CharField(max_length=10,primary_key=True)
    rollname = models.CharField(max_length=10)

    def __str__(self):
        return '<Roll:rollid=' + str(self.rollid) + ', ' + self.rollname + '>'

class User(models.Model):
    userid = models.CharField(max_length=10,primary_key=True)
    mail = models.EmailField(max_length=200)
    rollid = models.ForeignKey(Roll, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return '<User:userid=' + str(self.userid) + ', ' + self.username + '>'

class Group(models.Model):
    groupid = models.CharField(max_length=10,primary_key=True)
    groupname = models.CharField(max_length=10)

    def __str__(self):
        return '<Group:groupid=' + str(self.groupid) + ', ' + self.groupname + '>'

class GroupDetails(models.Model):
    groupid = models.ForeignKey(Group, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '<GroupDetails:id=' + str(self.id) + ', ' + str(self.userid) + ':' + str(self.groupid) + '>'

"""
class Subject(models.Model):
    subjectid = models.CharField(max_length=10,primary_key=True)
    subjectname = models.CharField(max_length=200)
    subjectnote = models.CharField(max_length=200,default='なし')

    def __str__(self):
        return '<Subject:subjectid=' + str(self.subjectid) + ', ' + self.subjectname + '>'
"""

class Class(models.Model):
    classid = models.CharField(max_length=10,primary_key=True)
    classname = models.CharField(max_length=10)

    def __str__(self):
        return '<Class:classid=' + str(self.classid) + ', ' + self.classname + '>'

class ClassDetails(models.Model):
    classid = models.ForeignKey(Class, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '<ClassDetails:id=' + str(self.id) + ', ' + str(self.userid) + ':' + str(self.classid) + '>'

class Timetable(models.Model):
    title = models.CharField(max_length=10)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    color = models.CharField(max_length=10)
    details = models.CharField(max_length=100)
    classid = models.ForeignKey(Class, on_delete=models.CASCADE)
    
    def __str__(self):
        return '<Timetable:title=' + str(self.title) + ', ' + self.details + '>'