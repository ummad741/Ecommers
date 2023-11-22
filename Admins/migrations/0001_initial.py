# Generated by Django 4.2.7 on 2023-11-21 14:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admins', models.CharField(choices=[('Superadmin', 'Superadmin'), ('admin', 'admin')], max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=20)),
                ('surname', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=9, unique=True, validators=[django.core.validators.RegexValidator(message='Telefon raqamini +998xxxxxxxxx kabi kriting', regex='d{0,9}')])),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
