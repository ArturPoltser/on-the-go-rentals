# Generated by Django 5.0.2 on 2024-02-28 15:56

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('max_daily_budget', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=100, message="We don't have such car for this budget. Sorry.")])),
                ('rental_time', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0, message='Rental time should be a non-negative integer.'), django.core.validators.MaxValueValidator(limit_value=31, message='Rental time should not exceed 31 days.')])),
                ('driver_license', models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message='Driver license should consist only of 7 characters: first 2 characters are uppercase letters and last 5 characters are digits', regex='^[A-Z]{2}\\d{5}$')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=2005, message='Year should be from 2005 onwards.'), django.core.validators.MaxValueValidator(limit_value=2023, message='Year should not exceed 2023.')])),
                ('horsepower', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=100, message="We can't rent car with less than 100 horsepowers."), django.core.validators.MaxValueValidator(limit_value=800, message="We can't rent car with more than 800 horsepowers.")])),
                ('fuel_consumption', models.DecimalField(decimal_places=1, max_digits=2)),
                ('daily_cost', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=100, message="We can't rent car with daily price less than 100$."), django.core.validators.MaxValueValidator(limit_value=2000, message="We can't rent car with daily price more than 2000$.")])),
                ('renter', models.ManyToManyField(related_name='cars', to=settings.AUTH_USER_MODEL)),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.insurance')),
            ],
        ),
    ]