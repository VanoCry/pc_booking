from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm, RegisterForm
from .models import PC, Booking
from django.urls import reverse_lazy



def pc_list(request):
    print("Запустилась pc_list")
    pcs = PC.objects.filter(is_active=True)  # Важно: объекты PC должны существовать в БД
    print("Список пк: ", list(pcs))
    return render(request, 'booking/pc_list.html', {'pcs': pcs})

def book_pc(request, pc_id):
    pc = get_object_or_404(PC, id=pc_id)  # 404 если ПК не существует
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.pc = pc
            booking.user = request.user
            booking.save()
            return redirect('pc_list')  # Редирект после успеха
    else:
        form = BookingForm()  # Пустая форма для GET-запроса

    # Всегда возвращаем HttpResponse (даже для GET или невалидной формы)
    return render(request, 'booking/book_pc.html', {'form': form, 'pc': pc})

@login_required(login_url=reverse_lazy('login'))
def my_bookings(request):
    user_bookings = Booking.objects.filter(user=request.user).order_by('-start_time')
    return render(request, 'booking/my_bookings.html', {'bookings' : user_bookings})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_bookings') 
    else:
        form = RegisterForm()

    return render(request, 'booking/register.html', {'form': form })