from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView 
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .forms import *
from .models import *


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


def group(request):
    group = Child.objects.filter(teacher_id = request.user.id) 
    data = {
        'group': group, 
        'title': 'Группа',
    }
    return render(request, 'group.html', data)


def children(request):
    parent = Parent.objects.get(user_id = request.user.id)
    children = Child.objects.filter(parent = parent.user_id) 
    data = {
        'children': children, 
        'title': 'Личный кабинет',
    }
    return render(request, 'children.html', data)