# Generated by Django 4.1.5 on 2023-07-06 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_remove_employee_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
