# Generated by Django 3.1.1 on 2020-09-18 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workschedule',
            name='week_day',
            field=models.CharField(blank=True, choices=[('0', 'Понедельник'), ('1', 'Вторник'), ('2', 'Среда'), ('3', 'Четверг'), ('4', 'Пятница'), ('5', 'Суббота'), ('6', 'Воскресенье')], max_length=50, null=True, verbose_name='День недели'),
        ),
    ]