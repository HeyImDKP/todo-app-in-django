from django import forms
from .models import Todo_Data, User
from django.utils import timezone

class Todo_Form(forms.ModelForm):
    class Meta:
        model = Todo_Data
        fields = ['title', 'details', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter Title'}),
            'details': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Enter Details'}),
            'date': forms.DateInput(attrs={'class': 'form-input', 'placeholder': f'Enter Date ({timezone.now()})'}),
        }
        
class User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Enter Password'}),
        }