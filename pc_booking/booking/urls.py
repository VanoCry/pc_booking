from django.urls import path
from . import views


urlpatterns = [
    path('', views.pc_list, name='pc_list'),
    path('book/<int:pc_id>/', views.book_pc, name='book_pc'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('register/', views.register, name='register'),
]