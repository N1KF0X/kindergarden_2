from django.contrib import admin
from django.urls import path
from application.views import *
from users.views import *
from teacher.views import *

admin.site.site_header = 'Детский садик "Фантазия"'
admin.site.index_title = 'Детский садик "Фантазия" - Администрирование'

urlpatterns = [
    path('admin', admin.site.urls),
    path('home', home, name='home'),
    path('child_app', child_app, name='child_app'),
    path('teacher_app', teacher_app, name='teacher_app'),
    path('question', question, name='question'),
    path('success', success, name='success'),

    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('group', group, name='group'),
    path('children', children, name='children'),
    path("logout", logout_user, name = "logout"),

    path('teachers', Teachers.as_view(), name='teachers')
]
