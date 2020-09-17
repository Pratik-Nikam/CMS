# Generated by Django 3.1.1 on 2020-09-17 09:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_content_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='document',
            field=models.FileField(default=django.utils.timezone.now, upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
            preserve_default=False,
        ),
    ]
