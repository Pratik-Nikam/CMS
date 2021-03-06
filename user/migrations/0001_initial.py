# Generated by Django 3.1.1 on 2020-09-17 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(db_column='id', help_text='Primary key auto incremental unique interger values.', primary_key=True, serialize=False, verbose_name='Id')),
                ('email', models.EmailField(db_column='email', help_text='Email Id of the user,should be unique for each user', max_length=254, unique=True)),
                ('name', models.CharField(db_column='name', help_text='Please enter Full Name', max_length=254, unique=True)),
                ('phone', models.IntegerField(db_column='phone', help_text='Phone number of user', max_length=10, verbose_name='Phone Number')),
                ('address', models.CharField(blank=True, db_column='address', help_text='Please enter Address', max_length=254, null=True)),
                ('city', models.CharField(blank=True, db_column='city', help_text='Please enter City name', max_length=50, null=True)),
                ('state', models.CharField(blank=True, db_column='state', help_text='Please enter State name', max_length=50, null=True)),
                ('country', models.CharField(blank=True, db_column='country', help_text='Please enter Country name', max_length=50, null=True)),
                ('pincode', models.IntegerField(db_column='pincode', help_text='Area Pincode', max_length=6, verbose_name='Pincode')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='created_date', help_text='Date on which the record was inserted. This is by default values and will be updated using python function save.', verbose_name='Created Date')),
                ('update_date', models.DateTimeField(auto_now_add=True, db_column='update_date', help_text='Date on which the record was updated. This is by default values and will be updated using python function save.', verbose_name='Update Date')),
                ('is_active', models.BooleanField(db_column='is_active', default=True, help_text='This column is used for soft delete. Users can reactivate the entry via portal', verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(db_column='is_deleted', default=False, help_text='This column is used for hard delete. Users cannot reactivate the entry via portal', verbose_name='Is Delete')),
                ('user', models.OneToOneField(db_column='user_id', help_text="User Id is the foreign key of User Table. This Id is linked with a particular. All the user's will have an entry in this table.", on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Id')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'db_table': 'user_profile',
            },
        ),
    ]
