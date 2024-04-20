from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=80)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    status = models.BooleanField()


class Teacher(models.Model):
    name = models.CharField(max_length=80)
    empid = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    salary = models.IntegerField()
    subject = models.CharField(max_length=40)
