# Generated by Django 3.1 on 2020-08-07 10:37

import apps.actions.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actions',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=apps.actions.models.image_upload_path),
        ),
    ]
