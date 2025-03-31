from django import forms
from .models import Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Почта")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]