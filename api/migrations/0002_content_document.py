# Generated by Django 3.1.1 on 2020-09-15 18:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]