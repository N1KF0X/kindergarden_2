from django.contrib import admin

from .models import *

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'status']
    list_per_page = 10


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_per_page = 10


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'bdd',
        'parent_full_name',
        'phone_number',
        'teacher',
        'parent',
        'art_club',
        'dance_club',
        'music',
        'physical_culture_club',
        'needlework_club',
        'robotics',
        'foreign_languages',
        'orientation_of_education',
        'specialist_service',
    ]
    list_per_page = 10
