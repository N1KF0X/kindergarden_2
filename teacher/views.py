from django.views.generic import ListView

from .models import *

class Teachers(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'
    extra_context = {
        'title': 'Наши педагоги',
    }