from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','bio']
        widgets = {'bio':forms.Textarea()}

    new_password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label='password confirmation',widget=forms.PasswordInput())
