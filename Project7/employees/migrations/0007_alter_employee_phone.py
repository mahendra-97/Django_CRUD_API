# Generated by Django 4.1.5 on 2023-07-06 06:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_alter_employee_email_alter_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(default=0, max_length=13, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{10}$')]),
        ),
    ]
