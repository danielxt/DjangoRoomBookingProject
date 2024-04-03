from django.db import models

# Create your models here.
class Room(models.Model):
    roomName = models.CharField(max_length=50, unique=True)
    capacity = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    roomImage = models.ImageField(null=True, blank=False, upload_to='media/')
    def __str__(self):
        return self.roomName
    
  