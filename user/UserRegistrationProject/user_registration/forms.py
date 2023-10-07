from django import forms
from .models import User_Detail

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User_Detail
        fields = ['First_name', 'Last_name', 'Email', 'Address', 'Phone_number', 'Education_detail']

        First_name = forms.CharField(max_length=100, required=True)
        Last_name = forms.CharField(max_length=100, required=True)
        Email = forms.EmailField(required=True)
        Address = forms.CharField(max_length=200, required=True)
        Phone_number = forms.CharField(max_length=15, required=True)
        Education_detail = forms.CharField(max_length=200, required=True)
