from django.forms import ModelForm
from .models import Room
class CreateRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ["roomName", "capacity", "roomImage"]

class DeleteRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ["roomName"]
    