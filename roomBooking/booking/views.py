from django.shortcuts import render,redirect
from .forms import RoomBookingForm, BookingModifyForm
from datetime import datetime, timedelta
from .models import RoomBooking, DeletedBookingModel
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils.timezone import localtime,now
from rooms.models import Room
# Create your views here.



def bookingManagementView(request):
    # show all bookings if admin
    if request.user.is_staff:
        bookings = RoomBooking.objects.all()
    # show only own bookings if just staff
    else:
        userName = User.objects.get(username=request.user.username)
        bookings = RoomBooking.objects.filter(userName = userName)
    context = {
        'roomBooking' : bookings.order_by("date", "start"),
        
    }
    return render(request, "booking/bookingManagement.html", context)


def findBookingOverlap(newBooking):
    bookingsOnDayInRoom = RoomBooking.objects.filter(date=newBooking.date, roomName=newBooking.roomName)
    # 1. new booking completely inside another slot
    # 2. new booking completely enveloping another slot
    # 3. new booking right on top of another slot
    # 4. new booking starts before but ends inside slot
    # 5. new booking starts inside slot but ends outside slot

    overlappingSlots = bookingsOnDayInRoom.filter(
        Q(start__lt=newBooking.start, end__gt=newBooking.end) | 
        Q(start__gt=newBooking.start, end__lt=newBooking.end) |
        Q(start=newBooking.start, end=newBooking.end) | # redundant?
        (Q(start__gte=newBooking.start, end__gte=newBooking.end) & Q(start__lt=newBooking.end)) |
        (Q(start__lte=newBooking.start, end__lte=newBooking.end) & Q(end__gt=newBooking.start))
    )
    return overlappingSlots

# take into account roomname, date, start, end
# Also reorder bookings chronologiclly

def roomBookingView(request):
    # TODO - BOOKING STATUS IS PLACEHOLDER
    rooms = Room.objects.all() # just used to get room images - is there more efficient way?

    context = {
            "bookingStatus" : True, 
            "rooms" : rooms,
            "numRooms" : len(rooms),
    }
    form = RoomBookingForm()
     # handling showing bookings for that day for that room
    if "checkAvailability" in request.POST:
        # save all data previously put in
        roomName = request.POST['roomName']
        date = request.POST['date']
        start = request.POST['start']
        end = request.POST['end']

        initial_dict = {
            "roomName" : roomName,
            "date" : date,
            "start" : start,
            "end" : end,
        }
        form = RoomBookingForm(initial=initial_dict)
        form = RoomBookingForm(request.POST)
        obj = form.save(commit=False)
        obj.userName = request.user
        overlappingBookings = findBookingOverlap(obj)
        if (overlappingBookings.exists()):
            context["bookingStatus"] = False
        bookingsOnDateForRoom = RoomBooking.objects.filter(date=date,roomName=roomName).order_by("date", "start")
        context['bookingsOnDateForRoom'] = bookingsOnDateForRoom
        
    
    # handling form submission
    elif (request.method == "POST"):
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.userName = request.user
            overlappingBookings = findBookingOverlap(obj)
            if (overlappingBookings.exists()):
                context = {
                    'overlappingBookings' : overlappingBookings,
                    'booking' : obj
                }
                return render(request, "booking/invalidBooking.html", context)
            else:
                obj.save()
                return redirect("bookingManagement")
            
   
    context['form'] = form
    return render(request, "booking/roomBooking.html", context)

def modifyBookingView(request,id):
    booking = RoomBooking.objects.get(id=id)
    bookingsForRoom = RoomBooking.objects.filter(roomName=booking.roomName).exclude(id=id).order_by("date", "start")

    
    data = {
        'roomName' : booking.roomName,
        'userName' : booking.userName,
        'date' : booking.date,
        'start' : booking.start,
        'end' : booking.end,        
        'bookingsForRoom' : bookingsForRoom,
        'bookingsForRoomCount' : len(bookingsForRoom)
    }
    form = BookingModifyForm(initial=data)
    return render(request, 'booking/modifyBooking.html', {'form' : form, 'booking': booking, 'bookingsForRoom': bookingsForRoom})

def deleteBookingView(request,id):
    booking = RoomBooking.objects.get(id=id)
    context = {'booking' : booking}
    return render(request, 'booking/deleteBooking.html', context)

def deleteBookingRecord(request, id):
    booking = RoomBooking.objects.get(id=id)
    # TODO - get ID of all users that booked room to be deleted, alert 
    # deletedBooking = DeleteBookingModel.objects.create(
    #     roomName=booking.roomName, userName=booking.userName, date=booking.date, start=booking.start, end=booking.end
    # )
    DeletedBookingModel.objects.create(roomName=booking.roomName, date=booking.date, start=booking.start, end=booking.end, userName=booking.userName)
    booking.delete()
    return redirect("bookingManagement")


def modifyBookingRecord(request,id):
    if(request.method == "POST"):
        booking = RoomBooking.objects.get(id=id)
        booking.date = request.POST['date']
        booking.start = request.POST['start']
        booking.end = request.POST['end']

        overlappingBookings = findBookingOverlap(booking)
        overlappingBookings = overlappingBookings.filter(~Q(id=id)) # remove original booking from queryset
        if (overlappingBookings.exists()):
            context = {
                    'overlappingBookings' : overlappingBookings,
                    'booking' : booking
                }
            return render(request, "booking/invalidBooking.html", context)
        else:
            booking.save()
    return redirect("bookingManagement")


