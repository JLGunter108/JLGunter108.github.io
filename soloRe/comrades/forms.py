from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views import generic
from django.contrib.auth.models import User
from django import forms
from theFeed.models import Profile

class CreateProfileForm(UserChangeForm):
    password = None
    about_me = forms.CharField(max_length=9999, widget=forms.Textarea(attrs=({'class': 'form-control'})))
    profile_pic = forms.FileField(max_length=128, widget=forms.FileInput(attrs=({'class': 'form-control'})))
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'user': forms.TextInput(attrs=({'class': 'form-control', 'id': 'user', 'value': '', 'type': 'hidden'}))
        }

class ProfileEditForm(UserChangeForm):
    password = None
    about_me = forms.CharField(max_length=9999, widget=forms.Textarea(attrs=({'class': 'form-control'})))
    profile_pic = forms.FileField(max_length=128, widget=forms.FileInput(attrs=({'class': 'form-control'})))
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'user': forms.TextInput(attrs=({'class': 'form-control', 'id': 'user', 'value': '', 'type': 'hidden'}))
            }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs=({'class': 'form-control'})))
    first_name = forms.CharField(max_length=128, widget=forms.TextInput(attrs=({'class': 'form-control'})))
    last_name = forms.CharField(max_length=128, widget=forms.TextInput(attrs=({'class': 'form-control'})))
    username = forms.CharField(max_length=128, widget=forms.TextInput(attrs=({'class': 'form-control'})))
    password1 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs=({'class': 'form-control'})))
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs=({'class': 'form-control'})))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password'
        }

class ProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs=({'class': 'form-control'})))
    first_name = forms.CharField(max_length=128, widget=forms.TextInput(attrs=({'class': 'form-control'})))
    last_name = forms.CharField(max_length=128, widget=forms.TextInput(attrs=({'class': 'form-control'})))
    username = forms.CharField(max_length=128, widget=forms.TextInput(attrs=({'class': 'form-control'})))
    password = None
    last_login = None
    is_superuser = None
    is_staff = None
    date_joined = None
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class PasswordsChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs=({'class': 'form-control', 'type': 'password'})))
    new_password1 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs=({'class': 'form-control', 'type': 'password'})))
    new_password2 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs=({'class': 'form-control', 'type': 'password'})))
    class Meta:
        model = User
        fields = ['__all__']
        labels = {
            'old_password': 'Old Password',
            'new_password1': 'New Password',
            'new_password2': 'Confirm New Password',
        }