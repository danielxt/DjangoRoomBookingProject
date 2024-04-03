
from django.urls import path
from .views import roomBookingView, deleteBookingView, deleteBookingRecord, modifyBookingView, modifyBookingRecord, bookingManagementView

# TODO - fix url bookings
urlpatterns = [
    path('', bookingManagementView, name='bookingManagement'),
    path('bookRoom/', roomBookingView, name='roomBooking'),  
    path('deleteBooking/<int:id>', deleteBookingView, name='deleteBooking'),
    path('modifyBooking/<int:id>', modifyBookingView, name='modifyBooking'),
    path('modifyBooking/modifyBookingRecord/<int:id>', modifyBookingRecord, name='modifyBookingRecord'),
    path('deleteBooking/deleteBookingRecord/<int:id>', deleteBookingRecord, name='deleteBookingRecord'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
