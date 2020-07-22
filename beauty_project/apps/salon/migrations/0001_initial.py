# Generated by Django 3.0.8 on 2020-07-22 08:48

import apps.salon.models.employee
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Опубликован или нет', verbose_name='Активный')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('site_url', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Site URL')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Салон',
                'verbose_name_plural': 'Салоны',
            },
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(blank=True, choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=50, null=True, verbose_name='День недели')),
                ('working_hours_from', models.TimeField(default='09:00', verbose_name='С')),
                ('working_hours_to', models.TimeField(default='19:00', verbose_name='До')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.Salon', verbose_name='Салон')),
            ],
            options={
                'verbose_name': 'График работы',
                'verbose_name_plural': 'График работы',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Опубликован на сайте?', verbose_name='Активный')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=apps.salon.models.employee.image_upload_path)),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('salon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salon.Salon', verbose_name='Салон')),
                ('services', models.ManyToManyField(blank=True, to='services.Services', verbose_name='Услуги')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
