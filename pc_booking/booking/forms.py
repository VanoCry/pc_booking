from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    def clean(self):
        if self.cleaned_data['end_time'] <= self.cleaned_data['start_time']:
            raise forms.ValidationError("Конец брони должен быть позже начала!")