from django.contrib import admin
from .models import PC, Booking

@admin.register(PC)
class PCAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active')  # Столбцы в списке


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pc', 'start_time', 'end_time')  
    list_filter = ('pc', 'start_time')
