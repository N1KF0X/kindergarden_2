# Generated by Django 4.1.4 on 2023-06-17 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_teacherapplication_alter_question_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildApplication',
            fields=[
                ('adaptiveapplication_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='application.adaptiveapplication')),
                ('art_club', models.BooleanField(verbose_name='Юный художник (Рисование)')),
                ('dance_club', models.BooleanField(verbose_name='Танцуем вместе (Танцы)')),
                ('music', models.BooleanField(verbose_name='Весёлые нотки (Музыкальный кружок)')),
                ('physical_culture_club', models.BooleanField(verbose_name='Спортивные ребята (Физкультурный кружок)')),
                ('needlework_club', models.BooleanField(verbose_name='Волшебные ручки (Рукоделие)')),
                ('robotics', models.BooleanField(verbose_name='Ротоботехника')),
                ('foreign_languages', models.BooleanField(verbose_name='Английский язык')),
                ('orientation_of_education', models.CharField(choices=[('ОБЖ', 'Основы безопасности жизнедеятельности'), ('НПВ', 'Нравствено-патриотическое воспитание'), ('КЭН', 'Культурно-этические нормы'), ('ВФК', 'Воспитание финансовой культуры'), ('ЭВ', 'Экологическое воспитание'), ('ИЗ', 'Индивидуальное развитие'), ('РР', 'Развитие речи'), ('МО', 'Методика общения'), ('ХЭР', 'Художествено-эстетическое развитие'), ('МРВ', 'Музыкально-ритмическое воспитание'), ('ФВ', 'Физическое воспитание'), ('РКРТ', 'Развитие конструирования и ручного труда')], max_length=4, verbose_name='Направленость обучения')),
                ('specialist_service', models.CharField(choices=[('Логопед-дефектолог', 'Логопед-дефектолог'), ('Сурдопедагог', 'Сурдопедагог (Нарушение слуха)'), ('Тифлопедагог', 'Тифлопедагог (Нарушение зрения)')], max_length=50, verbose_name='Услуги специалиста')),
            ],
            options={
                'verbose_name': 'Заявка на посесещение садика',
                'verbose_name_plural': 'Заявки на посесещения садика',
            },
            bases=('application.adaptiveapplication',),
        ),
    ]
