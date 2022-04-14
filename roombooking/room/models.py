from asyncio.windows_events import NULL
from django.db import models

class rooms(models.Model):
    roomnumber=models.CharField(primary_key=True)
    isbooked=models.BooleanField(default=False)
    usernname=models.CharField(default=NULL)
    
