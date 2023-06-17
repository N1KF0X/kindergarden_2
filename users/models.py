from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    statuses = [
        ('Педагог', 'Педагог'),
        ('Родитель', 'Родитель'),
    ]

    status = models.CharField(
        verbose_name='Статус',
        max_length=8,
        choices=statuses,
        default='Родитель',
    ) 

    def __str__(self):
        return self.username
