# Core/forms.py

from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' :'form-control', 'placeholder' : 'username'}) )

    fname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' :'FirstName'}) )

    lname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' :'form-control', 'placeholder' : 'Last Name'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder': 'Enter email'}))

    pass1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' :'form-control', 'placeholder' :'Enter Password '}))

    pass2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password' }))

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('pass1')
        pass2 = cleaned_data.get('pass2')

        if pass1 != pass2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class SignInForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'UserName'}))
    pass1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}))
