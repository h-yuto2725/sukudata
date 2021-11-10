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

