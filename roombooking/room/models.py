from asyncio.windows_events import NULL
from django.db import models

class rooms(models.Model):
    roomnumber=models.CharField(max_length=100)
    isbooked=models.BooleanField(default=False)
    user_register=models.CharField(max_length=100,default=NULL)
    date=models.CharField(max_length=100,default='main')
    timeslots=models.CharField(max_length=100,default='main')
    expiration=models.BooleanField(default=False)
