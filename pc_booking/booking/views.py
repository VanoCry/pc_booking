from django.shortcuts import get_object_or_404, render, redirect
from .forms import BookingForm
from .models import PC



def pc_list(request):
    pcs = PC.objects.filter(is_active=True)  # Важно: объекты PC должны существовать в БД
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