from django.shortcuts import render, redirect
from .forms import*


button_title = 'Отправить'
app_template = 'app.html'


def home(request):
    data = {
        'form': SendAdaptiveAppForm(),
        'title': 'Детский сад "Фантазия"',
        'button_title': button_title,
    }

    if request.method == 'POST':
        form = SendAdaptiveAppForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('success')

    return render(request, 'home.html', data)


def question(request):
    data = {
        'form': SendQuestionForm(),
        'title': 'Ваши вопросы',
        'button_title': button_title,
    }

    if request.method == 'POST':
        form = SendQuestionForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('success')     

    return render(request, app_template, data)


def teacher_app(request):
    data = {
        'form': SendTeacherAppForm(),
        'title': 'Анкета сотрудника',
        'button_title': button_title,
    }

    if request.method == 'POST':
        form = SendTeacherAppForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('success')

    return render(request, app_template, data)


def child_app(request):
    data = {
        'form': SendChildAppForm(),
        'title': 'Запись ребёнка в группу',
        'button_title': button_title,
    }

    if request.method == 'POST':
        form = SendChildAppForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('success')

    return render(request, app_template, data)


def success(request):
    data = {'title': 'Успех!'}

    return render(request, 'success.html', data)
