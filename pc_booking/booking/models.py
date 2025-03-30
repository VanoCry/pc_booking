from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class PC(models.Model):
    name = models.CharField(max_length=100) # ��������, PC-1
    is_active = models.BooleanField(default=True) # �������� �� ��
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    start_time = models.DateTimeField() # ������ �����
    end_time = models.DateTimeField() # ����� �����

    def __str__(self):
        return f"{self.user.username} -> {self.pc.name} ({self.start_time})"

