from django.urls import path
from .views import createRoomView, deleteRoomView, modifyRooms, updateRoom,deleteRoomRecord, roomManagementView
urlpatterns = [
    path('', roomManagementView, name='roomManagement'),
    path("createRoom/", createRoomView, name="createRoom"),
    path("deleteRoom/<int:id>", deleteRoomView, name="deleteRoom"),
    path("deleteRoom/deleteRoomRecord/<int:id>", deleteRoomRecord, name="deleteRoom"),
    path("modify/<int:id>", modifyRooms, name="modifyRoom"),
    path("modify/updateRoom/<int:id>", updateRoom, name="updateRoom"),
    # path("home/", getRooms, name="getRoom") # will be rooms/home
]   