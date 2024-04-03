from django.db import models
# from rooms.models import Room 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q,F
from django.utils.timezone import localtime,now

class RoomBooking(models.Model):
    roomName = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
    userName = models.ForeignKey(User, on_delete=models.CASCADE, default="", name="userName")
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()

    
    def clean(self):
        time = localtime(now())
        if self.start > self.end:
            raise ValidationError('Booking start time must be before booking end time')
        if self.date < time.date():
            raise ValidationError('Booking date is before current date')
        if self.start < time.time() and self.date == time.date():
            raise ValidationError('Booking start time is before current time')
        return super().clean()
    def save(self):
        self.full_clean()
        super(RoomBooking,self).save()
    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(start__lte=F('end')), name='start_before_end')
        ]
 
    # def __str__(self):
    #     return self.roomName

class DeletedBookingModel(models.Model):
    roomName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()

