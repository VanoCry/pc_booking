from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class PC(models.Model):
    name = models.CharField(max_length=100) # Например, PC-1
    is_active = models.BooleanField(default=True) # Работает ли ПК
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    start_time = models.DateTimeField() # Начало брони
    end_time = models.DateTimeField() # Конец брони

    def __str__(self):
        return f"{self.user.username} -> {self.pc.name} ({self.start_time})"

