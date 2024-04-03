from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.RoomBooking)
admin.site.register(models.DeletedBookingModel)