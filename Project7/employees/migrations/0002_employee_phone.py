# Generated by Django 4.1.5 on 2023-07-06 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
