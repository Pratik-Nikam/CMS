# Generated by Django 3.1.1 on 2020-09-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_content_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
