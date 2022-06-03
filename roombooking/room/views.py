from ast import Return
from asyncio.windows_events import NULL
from http.client import HTTPResponse
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from pip import main
from home.modelsusers import users
from .models import rooms
from django.db.models import Q
import datetime


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

    if request.method=='POST': ########====main request handler==============##################

        if request.POST.get('username')!=None:# entering page  for login if usernmae in post request
            username=request.POST['username']  
            psw=request.POST['psw']
            if users.objects.filter(username=username).exists() and users.objects.filter(username=username)[0].issroommanager==True:
                global a
                a=users.objects.filter(username=username)
                global roomlist
                roomlist=rooms.objects.filter(date='main')
                if a[0].psw==psw:
                    return render(request,'roomcreate.html',{'firstname':a[0].firstname,'roommain':True,'roomlist':roomlist}) ##pushing manager to room managerment website
                else:
                    messages.info(request,'wrong password')
                    return redirect('/signinmanager')
            elif users.objects.filter(username=username).exists() :
                messages.info(request,'Only Room Manger Can Access')
                return redirect('/signinmanager')
            else:
                messages.info(request,'No Username Registered')
                return redirect('/signinmanager')



         #--------------if request is about adiing rooms and RoomNumberAdd in request objsct------------------
        elif request.POST.get('RoomNumberAdd')!=None:  
            try:
                b=int(str(request.POST.get('RoomNumberAdd')))
                if rooms.objects.filter(roomnumber=str(b)).exists():
                    messages.info(request,'Room Already Exists')    
                    roomlist=rooms.objects.filter(date='main')
                    return render(request,'roomcreate.html',{'firstname':a[0].firstname,'roommain':True,'roomlist':roomlist})
                else:
                    room=rooms()
                    room.roomnumber=str(b)
                    room.save() 
                    messages.info(request,'Roomcreated')  
                    roomlist=rooms.objects.filter(date='main')
                    return render(request,'roomcreate.html',{'firstname':a[0].firstname,'roommain':True,'roomlist':roomlist})
            except ValueError:
                messages.info(request,'Integer RoomNumber Only')   
                 
                roomlist=rooms.objects.filter(date='main')
                return render(request,'roomcreate.html',{'firstname':a[0].firstname,'roommain':True,'roomlist':roomlist})




        #--------------if request is about deleting button------------------
        elif request.POST.get('RoomDel')!=None:
            roomdel=rooms.objects.filter(roomnumber=request.POST.get('RoomDel'))
            for i in roomdel:
                i.delete()
            #reseting roomlist after deleting room
            roomlist=rooms.objects.all()
            return render(request,'roomcreate.html',{'firstname':a[0].firstname,'roommain':True,'roomlist':roomlist})



        #-------------FROM HERE WE WILL TAKE INDIVIDUAL ROOM DATA---------------------
        #--------------if request is about editing or entering roomedit button------------------
        elif request.POST.get('RoomEdit')!=None:
            global roomedit
            roomedit=request.POST.get('RoomEdit')
            roomschedule=rooms.objects.filter(roomnumber=str(roomedit)).filter(~Q(date='main'))
            return render(request,'roomedit.html',{'firstname':a[0].firstname,'roomschedule':roomschedule,'roomnumber':roomedit})
 


        #-----------TAKING DATE ARGUMENT FROM INDIVIDUAL PAGE----------------

#===================entering new date and time schedule=====================
        elif request.POST.get('date')!=None:   
            try:
                date=request.POST.get('date')
                timeslots=[request.POST.get('time1'),request.POST.get('time2')]
                day, month, year = date.split('/')
                datetime.datetime(int(year), int(month), int(day))
                timeformat = "%H:%M"
                datetime.datetime.strptime(timeslots[0], timeformat)
                datetime.datetime.strptime(timeslots[1], timeformat)
                room=rooms()
                room.roomnumber=roomedit
                room.date=date
                room.timeslots=str(timeslots[0])+'-'+timeslots[1]
                room.save()
                roomschedule=rooms.objects.filter(roomnumber=str(roomedit)).filter(~Q(date='main'))
                return render(request,'roomedit.html',{'firstname':a[0].firstname,'roomschedule':roomschedule,'roomnumber':roomedit})
            except ValueError:
                messages.info(request,'Enter Correct Input')
                roomschedule=rooms.objects.filter(roomnumber=str(roomedit)).filter(~Q(date='main'))
                return render(request,'roomedit.html',{'firstname':a[0].firstname,'roomschedule':roomschedule,'roomnumber':roomedit})


#==========updating timeslot=================
#====================FOR INDIVIDUAL TIMESLOT WE WILL USE ROOM ID=====================#
        elif request.POST.get('timeslotupdate')!=None:
            try:
                newtimeslot=str(request.POST.get('newtimeslot'))
                roomid=request.POST.get('timeslotupdate')
                time1,time2=newtimeslot.split('-')
                timeformat = "%H:%M"
                datetime.datetime.strptime(time1, timeformat)
                datetime.datetime.strptime(time2, timeformat)
                room=rooms.objects.filter(id=int(roomid))[0]
                room.timeslots=str(newtimeslot)
                room.save()
                roomschedule=rooms.objects.filter(roomnumber=str(roomedit)).filter(~Q(date='main'))
                messages.info(request,'Updated')
                return render(request,'roomedit.html',{'firstname':a[0].firstname,'roomschedule':roomschedule,'roomnumber':roomedit})
            except ValueError:
                messages.info(request,'Enter Correct Input')
                roomschedule=rooms.objects.filter(roomnumber=str(roomedit)).filter(~Q(date='main'))
                return render(request,'roomedit.html',{'firstname':a[0].firstname,'roomschedule':roomschedule,'roomnumber':roomedit})
            
    else:
        return render(request,'signinmanager.html')







