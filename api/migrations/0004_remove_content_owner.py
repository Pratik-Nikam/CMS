# Generated by Django 3.1.1 on 2020-09-17 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200917_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='owner',
        ),
    ]
