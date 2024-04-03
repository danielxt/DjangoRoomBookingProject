from django.urls import path
from .views import SignUpView, userManagementView, deleteUserView, deleteUserRecord

urlpatterns = [
    path('', userManagementView, name="userManagement"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('deleteUser/<int:id>', deleteUserView, name="deleteUser"),
    path('deleteUser/deleteUserRecord/<int:id>', deleteUserRecord, name="deleteUserRecord"),
]