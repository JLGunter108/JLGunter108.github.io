from django.urls import path
from .views import AccountView, DeleteView, RegistrationView, UserEditView, PasswordsChangeView, EditProfileView, CreateProfileView

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('profile/<int:pk>', AccountView.as_view(), name='profile'),
    path('profile/<int:pk>/edit_account', UserEditView.as_view(), name='edit_account'),
    path('profile/<int:pk>/edit', EditProfileView.as_view(), name='edit_profile'),
    path('profile/<int:pk>/delete', DeleteView.as_view(), name='delete_profile'),
    path('profile/password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), name='change_password'),
    path('profile/new', CreateProfileView.as_view(), name='create_profile'),
]
