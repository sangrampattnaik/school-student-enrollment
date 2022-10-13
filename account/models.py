from email.policy import default

from django.db import models


class School(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pin = models.CharField(max_length=6)
    password = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    username = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=255)
    grade = models.IntegerField()
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
