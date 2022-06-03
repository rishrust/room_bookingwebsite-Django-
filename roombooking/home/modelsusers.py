from django.db import models

class users(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=220)
    phone=models.CharField(max_length=10)
    psw=models.CharField(max_length=100)
    issroommanager=models.BooleanField(default=False)
