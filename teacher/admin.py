from django.contrib import admin

from .models import *

@admin.register(Teacher)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'specialization', 'education', 'experience']
    list_per_page = 10
