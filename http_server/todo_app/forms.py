from django import forms
from .models import Todo_Data
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
        