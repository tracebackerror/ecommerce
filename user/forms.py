from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from web_app.models import Address


class CustomLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))



class CustomRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'})}


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['locality', 'city', 'state','pincode','country']
        widgets = {'locality':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Popular Place like Restaurant, Religious Site, etc.'}), 'city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), 'state':forms.TextInput(attrs={'class':'form-control', 'placeholder':'State or Province'}), 'pincode':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Pincode'}), 'country':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'})}