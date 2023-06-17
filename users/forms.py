from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Имя пользователя", 
        widget = forms.TextInput(
            attrs={'class': 'form-input'},
        ),
    )
    password1 = forms.CharField(
        label="Пароль", 
        widget = forms.PasswordInput(
            attrs={'class': 'form-input'}
        ),
    )
    password2 = forms.CharField(
        label="Повторите пароль", 
        widget = forms.PasswordInput(
            attrs={'class': 'form-input'}
        ),
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя", 
        widget = forms.TextInput(
            attrs={'class': 'form-input'},
        ),
    )
    password = forms.CharField(
        label="Пароль", 
        widget = forms.PasswordInput(
            attrs={'class': 'form-input'}
        ),
    )