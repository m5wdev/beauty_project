# Generated by Django 3.0.8 on 2020-07-31 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200730_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(default=0, max_length=100, verbose_name='First Name'),
            preserve_default=False,
        ),
    ]
