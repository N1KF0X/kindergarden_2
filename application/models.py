from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse


class Application(models.Model):
    phone_number_regex = RegexValidator(regex = r"^\+?1?\d{8,15}$")

    email = models.EmailField(verbose_name="Электронная почта")
    full_name = models.CharField(verbose_name="Ваше Ф.И.О.", max_length=50)    
    phone_number = models.CharField(
        verbose_name='Номер телефона',
        max_length=14,
        validators = [phone_number_regex],
    )

    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'posr_id': self.pk})
    
    class Meta:
        abstract = True
    

class AdaptiveApplication(Application):
    child_full_name = models.CharField(
        verbose_name="Ф.И.О. ребёнка", 
        max_length=50,
    )

    class Meta:
        verbose_name='Адаптационная заявка'
        verbose_name_plural='Адаптационные заявки'


class Question(Application):
    text = models.TextField(verbose_name="Что Вас интересует:")
    
    class Meta:
        verbose_name='Вопрос'
        verbose_name_plural='Вопросы'


class TeacherApplication(Application):
    specialization = [
        ('Воспитатель', 'Воспитатель'),
        ('Помощник воспитателя', 'Помощник воспитателя'),
        ('Педагог доп. образования', 'Педагог доп. образования'),
        ('Специалист', 'Специалист'),
        ('Другое', 'Другое'),
    ]
    educations = [
        ('Основное общее', 'Основное общее'),
        ('Среднее общее', 'Среднее общее'),
        ('Среднее проф.', 'Среднее проф.'),
        ('Высшее', 'Высшее'),
    ]

    education = models.CharField(
        verbose_name='Образование',
        max_length=50,
        choices=educations,
    ) 
    experience = models.IntegerField(verbose_name='Стаж работы')
    specialization = models.CharField(
        verbose_name='Специальность',
        max_length=50,
        choices=specialization,
    )
    about_me = models.TextField(
        verbose_name='О себе',
        blank=True
    )

    class Meta:
        verbose_name='Заявка на трудоустройство'
        verbose_name_plural='Заявки на трудоустройство'


class ChildApplication(AdaptiveApplication):
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


    class Meta:
        verbose_name='Заявка на посесещение садика'
        verbose_name_plural='Заявки на посесещения садика'
