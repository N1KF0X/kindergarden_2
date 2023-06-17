from django.shortcuts import redirect
from django.contrib.auth.views import LoginView 
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .forms import *


class Register(CreateView):
    form_class = RegisterForm
    template_name = 'user.html'
    extra_context = {
        'title': 'Регистрация',
        'button_title': 'Зарегистрироваться',
    }

    def get_success_url(self):
        return reverse_lazy('home')

class Login(LoginView):
    form_class = LoginForm
    template_name = 'user.html'
    extra_context = {
        'title': 'Войти',
        'button_title': 'Войти',
    }

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')
