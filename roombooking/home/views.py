from pickle import FALSE
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from .models import users
#from django.contrib.auth.models import User , auth


def homepage(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        firstname=str(request.POST['firstname'])
        lastname=str(request.POST['lastname'])
        username=str(request.POST['username'])
        email=str(request.POST['email'])
        phone=str(request.POST['phone'])
        psw=str(request.POST['psw'])
        pswrepeat=str(request.POST['psw-repeat'])
        if pswrepeat==psw:
            if users.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/signup')
            else:
                if users.objects.filter(email=email).exists():
                    messages.info(request,'Email Taken')
                    return redirect('/signup')
                else:
                    user=users()
                    user.firstname=firstname
                    user.lastname=lastname
                    user.username=username
                    user.psw=psw
                    user.phone=phone
                    user.email=email
                    user.save()
                    return redirect('/signin')

        else:
             messages.info(request,'Password not Matching')
             return redirect('/signup')
    else:    
        return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username=str(request.POST['username'])
        psw=str(request.POST['psw'])
        if users.objects.filter(username=username).exists():
            a=users.objects.filter(username=username)
            if psw==a[0].psw:
                return HttpResponse('Login Successful')
            else:
                messages.info(request,'Enter correct password')
                return redirect('/signin')
        else:
            messages.info(request,'Username not Registered')
            return redirect('/signin')

    else:
        return render(request,'signin.html')

def signinmanager(request):
    return render(request,'signinmanager.html')

