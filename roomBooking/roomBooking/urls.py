"""roomBooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from .views import setupHomePage, clearDeletedBookingsUser
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    # path("accounts/", include("accounts.urls")),
    # path("booking/", include("booking.urls")),
    path("userManagement/", include("accounts.urls")),
    path("roomManagement/", include("rooms.urls")),
    # path("rooms/", include("rooms.urls")),
    path("bookingManagement/", include('booking.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', setupHomePage, name='home'), 
    path('clearDeletedBookingsUser', clearDeletedBookingsUser, name="clearDeletedBookingsUser")
    # path(r'^clearDeletedBookingsUser$', clearDeletedBookingsUser, name="clearDeletedBookingsUser")
    
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
