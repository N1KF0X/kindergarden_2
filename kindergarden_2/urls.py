from django.contrib import admin
from django.urls import path
from application.views import *
from users.views import *

admin.site.site_header = 'Детский садик "Фантазия"'
admin.site.index_title = 'Детский садик "Фантазия" - Администрирование'

urlpatterns = [
    path('admin', admin.site.urls),
    path('home', home, name='home'),
    path('success', success, name='success'),
    path('question', question, name='question'),
    path('teacher_app', teacher_app, name='teacher_app'),
    path('child_app', child_app, name='child_app'),
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    #path('children/', ChildList.as_view(), name='children'),
    #path('answer/', answer, name='answer'),
    path("logout/", logout_user, name = "logout"),
    #path("teachers/", Teachers.as_view(), name = "teachers"),
]
