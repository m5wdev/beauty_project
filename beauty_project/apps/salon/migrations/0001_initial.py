# Generated by Django 3.1 on 2020-08-20 15:21

import apps.salon.models.employee
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Опубликован или нет', verbose_name='Активный')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('site_url', models.URLField(blank=True, null=True, verbose_name='Site URL')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='Город')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('metro', models.CharField(blank=True, max_length=255, null=True, verbose_name='Метро')),
                ('latitude', models.CharField(blank=True, max_length=100, null=True, verbose_name='Широта')),
                ('longitude', models.CharField(blank=True, max_length=100, null=True, verbose_name='Долгота')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
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
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.salon', verbose_name='Салон')),
            ],
            options={
                'verbose_name': 'График работы',
                'verbose_name_plural': 'График работы',
            },
        ),
        migrations.CreateModel(
            name='SalonServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('salon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salon.salon', verbose_name='Салон')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
            options={
                'verbose_name': 'Услуга Салона',
                'verbose_name_plural': 'Услуги Салонов',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Опубликован на сайте?', verbose_name='Активный')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=apps.salon.models.employee.image_upload_path)),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
                ('phone', models.CharField(blank=True, max_length=60, null=True, verbose_name='Телефон')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('salon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salon.salon', verbose_name='Салон')),
                ('services', models.ManyToManyField(blank=True, to='services.Services', verbose_name='Услуги')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
            },
        ),
        migrations.CreateModel(
            name='ClientAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время записи')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('status', models.CharField(blank=True, choices=[('cancelled', 'Отменен'), ('done', 'Исполнено'), ('in_progress', 'В процессе'), ('sign_up', 'Запись')], max_length=50, null=True, verbose_name='Статус')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salon.employee', verbose_name='Мастер')),
                ('services', models.ManyToManyField(blank=True, to='services.Services', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Запись Клиента',
                'verbose_name_plural': 'Записи Клиентов',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Опубликован на сайте?', verbose_name='Активный')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('salon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salon.salon', verbose_name='Салон')),
            ],
            options={
                'verbose_name': 'Клиент салона',
                'verbose_name_plural': 'Клиенты салона',
            },
        ),
    ]
