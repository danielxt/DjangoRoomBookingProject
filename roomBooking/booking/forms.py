# import form class from django
from django import forms
from django.conf import settings
from .models import RoomBooking
from django.db import models
from datetimewidget.widgets import DateWidget, TimeWidget
from django.core.exceptions import ValidationError
from django.utils.timezone import localtime,now
import datetime

# roomName = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
# userName = models.ForeignKey(User, on_delete=models.CASCADE, default="", name="userName")
# date = models.DateField()
# start = models.TimeField()
# end = models.TimeField()
# bookingDeleteMsg = models.CharField(default="")



# str(localtime(now()).time())[:-10] # removes miliseconds and seconds,
# timeOptions = {
#             'startTime' : "10:00",
#         }

class RoomBookingForm(forms.ModelForm):
    
    class Meta:
        todayDate = datetime.datetime.now()
        dateOptions = {
            'startDate' : todayDate.strftime("%Y-%m-%d") # converts to yyyy/mm/dd format,
            # 'startDate' : str(localtime(now()).date()), 
        }
        model = RoomBooking
        fields = ["roomName", "date", "start", "end"]
        widgets = {
            'date' : DateWidget(usel10n=True, options=dateOptions),
            'start' : TimeWidget(),
            'end' : TimeWidget(),
        }
 

class BookingModifyForm(forms.ModelForm):
    class Meta:
        todayDate = datetime.datetime.now()
        dateOptions = {
            'startDate' : todayDate.strftime("%Y-%m-%d") # converts to yyyy/mm/dd format,
            # 'startDate' : str(localtime(now()).date()), 
        }
        model = RoomBooking
        fields = ["date", "start", "end"]
        widgets = {
            'date' : DateWidget(usel10n=True, options=dateOptions),
            'start' : TimeWidget(),
            'end' : TimeWidget()
        }
    

    