# Generated by Django 4.1.4 on 2023-06-18 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_child'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='teacher',
        ),
    ]