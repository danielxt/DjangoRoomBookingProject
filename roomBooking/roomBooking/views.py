from django.shortcuts import render, redirect
from rooms.models import Room
from django.contrib.auth.models import User
from booking.models import RoomBooking,DeletedBookingModel
from django.utils.timezone import localtime,now
from django.db.models import Q

# MASTER VIEW SETUP
def setupHomePage(request): # calls room view, user view, bookings view to display on page
    # roomData = Room.objects.all()
    # userData = User.objects.all()
    if request.user.is_authenticated:
        roomBookingData = RoomBooking.objects.all()
        roomData = Room.objects.all()

        time = localtime(now())
    
        numBookings = roomBookingData.count()
        numMeetingsNow = roomBookingData.filter(date=time.date(), start__lte=time.time(), end__gte=time.time()).count()
        numRoomsAvailable = roomData.count() - numMeetingsNow

        # if the booking date has passed or the booking is today but the end time has passed
        passedBookings = roomBookingData.filter(Q(date__lt=time.date()) | Q(date=time.date(), end__lt=time.time()))
        passedBookings.delete()
    
        deletedBookings = DeletedBookingModel.objects.filter(userName=request.user.username)


        context = {
            # 'rooms' : roomData,
            # 'users' : userData,
            'roomBooking' : roomBookingData,
            'numBookings' : numBookings,
            'time' : time,
            'numMeetingsNow': numMeetingsNow,
            'numRoomsAvailable': numRoomsAvailable,
            'deletedBookings' : deletedBookings,
        }
        return render(request, 'home.html', context)
    else:
        return redirect("login") # if user not authenticated

def clearDeletedBookingsUser(request):
    DeletedBookingModel.objects.filter(userName=request.user.username).delete()
    return redirect("home")
