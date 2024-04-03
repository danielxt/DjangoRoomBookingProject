from django.shortcuts import render,redirect
from .forms import CreateRoomForm, DeleteRoomForm
from .models import Room
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse_lazy

def roomManagementView(request):
    rooms = Room.objects.all()
    context = {'rooms' : rooms}
    return render(request, "rooms/roomManagement.html", context)


def createRoomView(request):
    if request.POST:
        form = CreateRoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("roomManagement")
        else:
            return redirect("home")
        # TODO - VALIDATE IF UNIQUE ROOM NAME INPUTTED
    return render(request, 'rooms/createRoom.html', {'form' : CreateRoomForm})

def getRooms(request):
    data = Room.objects.filter()
    context = {'rooms': data}
    
    return render(request, 'home.html', context)


# SHOULD BE updateRoomView and updateRoomRecord
def modifyRooms(request, id):
    room = Room.objects.get(id=id)
    context = {
        'room' : room
    }
    return render(request, 'rooms/modifyRoom.html', context)

def updateRoom(request,id):
    roomName = request.POST['roomName']
    capacity = request.POST['capacity']
    room = Room.objects.get(id=id)
    room.roomName = roomName
    room.capacity = capacity
    room.save()
    return redirect("roomManagement")

def deleteRoomView(request,id):
    room = Room.objects.get(id=id)
    context = {'room': room}
    return render(request, 'rooms/deleteRoom.html', context)

def deleteRoomRecord(request,id):
    room = Room.objects.get(id=id)
    room.delete()
    return redirect("roomManagement")