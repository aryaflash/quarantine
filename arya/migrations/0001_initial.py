# Generated by Django 3.0.6 on 2020-07-06 14:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('name', models.CharField(help_text='Enter your full name', max_length=20)),
                ('gmail', models.EmailField(blank=True, help_text='optional', max_length=254, validators=[django.core.validators.EmailValidator])),
                ('phoneNumber', models.IntegerField(help_text='this num will be used to access your account', primary_key=True, serialize=False, unique=True)),
                ('address', models.CharField(help_text='Enter your address', max_length=100)),
                ('password', models.CharField(help_text='Enter strong Password', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('name', models.CharField(help_text='Enter your full name', max_length=20)),
                ('gmail', models.EmailField(blank=True, help_text='optional', max_length=254, validators=[django.core.validators.EmailValidator])),
                ('phoneNumber', models.IntegerField(help_text='this num will be used to access your account', primary_key=True, serialize=False, unique=True)),
                ('address', models.CharField(help_text='Enter your address', max_length=100)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arya.Manager')),
            ],
        ),
    ]