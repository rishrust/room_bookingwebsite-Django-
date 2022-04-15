from ast import Return
from asyncio.windows_events import NULL
from http.client import HTTPResponse
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from home.models import users



def signinmanager(request):     ## manager signin by default ia am creating one manager rishabhadmin 
    if users.objects.filter(username='rishabhadmin').exists():
        pass
    else:
        user=users()
        user.firstname='rishabhAdmin'
        user.lastname=NULL
        user.username='rishabhadmin'
        user.psw='12345678'
        user.phone=NULL
        user.email=NULL
        user.issroommanager=True
        user.save()

    if request.method=='POST':
        username=request.POST['username']  
        psw=request.POST['psw']
        if users.objects.filter(username=username).exists() and users.objects.filter(username=username)[0].issroommanager==True:
            a=users.objects.filter(username=username)
            if a[0].psw==psw:
                return render(request,'roomcreate.html') ##pushing manager to room managerment website
            else:
                messages.info(request,'wrong password')
                return redirect('/signinmanager')
        elif users.objects.filter(username=username).exists() :
            messages.info(request,'Only Room Manger Can Access')
            return redirect('/signinmanager')
        else:
            messages.info(request,'No Username Registered')
            return redirect('/signinmanager')
    else:
        return render(request,'signinmanager.html')
