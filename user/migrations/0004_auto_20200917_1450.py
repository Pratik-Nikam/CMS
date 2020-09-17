# Generated by Django 3.1.1 on 2020-09-17 14:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200917_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.PositiveIntegerField(db_column='phone', help_text='Phone number of user', validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Only 10 digits allowed.')], verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pincode',
            field=models.PositiveIntegerField(db_column='pincode', help_text='Area Pincode', validators=[django.core.validators.RegexValidator('^\\d{6}$', 'Only 6 digits are allowed.')], verbose_name='Pincode'),
        ),
    ]
