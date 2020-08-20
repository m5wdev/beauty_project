# Generated by Django 3.1 on 2020-08-20 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('salon', '0003_auto_20200820_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='salonservices',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='services.services', verbose_name='Услуга'),
            preserve_default=False,
        ),
    ]