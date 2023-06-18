from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

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

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'

class Parent(models.Model):
    user = models.OneToOneField(
        CustomUser, 
        on_delete = models.CASCADE,
        verbose_name="Родитель",
        primary_key=True
    )

    class Meta:
        verbose_name='Родитель'
        verbose_name_plural='Родители'


class Child(models.Model):
    phone_number_regex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    education_orientation = [
        ('ОБЖ','Основы безопасности жизнедеятельности'),
        ('НПВ',"Нравствено-патриотическое воспитание"),
        ('КЭН',"Культурно-этические нормы"),
        ('ВФК',"Воспитание финансовой культуры"),
        ('ЭВ',"Экологическое воспитание"),
        ('ИЗ',"Индивидуальное развитие"),
        ('РР',"Развитие речи"),
        ('МО',"Методика общения"),
        ('ХЭР',"Художествено-эстетическое развитие"),
        ('МРВ',"Музыкально-ритмическое воспитание"),
        ('ФВ',"Физическое воспитание"),
        ('РКРТ',"Развитие конструирования и ручного труда"),
    ]
    specialist_services = [
        ('ЛД',"Логопед-дефектолог"),
        ('С',"Сурдопедагог (Нарушение слуха)"),
        ('Т',"Тифлопедагог (Нарушение зрения)"),
    ]

    full_name = models.CharField(
        verbose_name='Ф.И.О. ребёнка', 
        max_length=50,
    )
    bdd = models.DateField(verbose_name='Дата рождения')
    parent_full_name = models.CharField(
        verbose_name='Ф.И.О. родителя(ей)', 
        max_length=50,
    )
    phone_number = models.CharField(
        verbose_name='Номер телефона родителя/опекуна', 
        max_length=14,
        validators = [phone_number_regex],
    )
    art_club = models.BooleanField(verbose_name="Юный художник (Рисование)")
    dance_club = models.BooleanField(verbose_name="Танцуем вместе (Танцы)")
    music = models.BooleanField(verbose_name="Весёлые нотки (Музыкальный кружок)")
    physical_culture_club = models.BooleanField(verbose_name="Спортивные ребята (Физкультурный кружок)")
    needlework_club = models.BooleanField("Волшебные ручки (Рукоделие)")
    robotics = models.BooleanField(verbose_name="Ротоботехника")
    foreign_languages = models.BooleanField(verbose_name="Английский язык")
    orientation_of_education = models.CharField(
        verbose_name='Направленость обучения',
        max_length=4,
        choices=education_orientation,
    )
    specialist_service = models.CharField(
        verbose_name='Услуги специалиста',
        max_length=2,
        choices=specialist_services,
    )
    teacher = models.ForeignKey(
        CustomUser, 
        on_delete = models.CASCADE, 
        verbose_name="Педагог",
        blank=True,
        default=None,
    )
    parent = models.ForeignKey(
        Parent, 
        on_delete = models.CASCADE,
        verbose_name="Родитель",
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name='Ребёнок'
        verbose_name_plural='Дети'
