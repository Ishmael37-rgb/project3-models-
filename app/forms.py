from django import forms
from .models import contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['name', 'email', 'age', 'date_of_birth', 'gender']