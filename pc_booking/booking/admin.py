from django.contrib import admin

from .models import PC, Booking
# Register your models here.

admin.site.register(PC)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pc', 'start_time', 'end_time')  # ”кажите корректные пол€
    list_filter = ('pc', 'start_time')
