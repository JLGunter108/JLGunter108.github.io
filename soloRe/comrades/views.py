from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from theFeed.models import Profile
from .forms import ProfileEditForm, ProfileForm, RegistrationForm, PasswordsChangeForm, CreateProfileForm

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    success_url = reverse_lazy('home')

class RegistrationView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class AccountView(generic.DetailView):
    model = User
    template_name = 'account.html'

class UserEditView(generic.UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'registration/edit.html'
    success_url = reverse_lazy('home')

class EditProfileView(generic.UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

class CreateProfileView(generic.CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'registration/create_profile.html'
    success_url = reverse_lazy('home')

class DeleteView(generic.DeleteView):
    model = User
    template_name = 'delete_profile.html'
    success_url = reverse_lazy('home')