# Generated by Django 4.1.4 on 2023-06-17 16:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdaptiveApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('full_name', models.CharField(max_length=50, verbose_name='Ваше Ф.И.О.')),
                ('phone_number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Номер телефона')),
                ('child_full_name', models.CharField(max_length=50, verbose_name='Ф.И.О. ребёнка')),
            ],
            options={
                'verbose_name': 'Адаптационная заявка',
                'verbose_name_plural': 'Адаптационные заявки',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('full_name', models.CharField(max_length=50, verbose_name='Ваше Ф.И.О.')),
                ('phone_number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Номер телефона')),
                ('text', models.TextField(verbose_name='Что Вас интересует:')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='TeacherApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('full_name', models.CharField(max_length=50, verbose_name='Ваше Ф.И.О.')),
                ('phone_number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Номер телефона')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]