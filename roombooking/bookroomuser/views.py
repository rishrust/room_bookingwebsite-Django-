from ast import Return
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from home import views
from home.modelsusers import users
from room.models import rooms 



def bookroom(request):
    roomlist=rooms.objects.filter(date='main')
    user=views.username
    if request.POST.get('viewslots')!=None:
        roomlist=rooms.objects.filter(roomnumber=request.POST['viewslots'])
        return render(request,'roomdets.html',{'roomlist':roomlist[1:],'fullname':users.objects.filter(username=user)[0].firstname})
    if request.POST.get('bking')!=None:
        a=rooms.objects.get(id=request.POST['bking'])
        a.user_register=user
        a.isbooked=True
        a.save()
    return render(request,'bookroom.html',{'roomlist':roomlist,'fullname':users.objects.filter(username=user)[0].firstname})

    




def viewbooking(request):
    user=views.username
    return HttpResponse(views.username)

