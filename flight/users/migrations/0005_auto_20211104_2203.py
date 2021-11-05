# Generated by Django 3.1.13 on 2021-11-05 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211104_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='defaultAirport',
            field=models.CharField(choices=[('ATL', 'Hartsfield-Jackson International Airport'), ('LAX', 'Los Angeles International Airport'), ('JFK', 'John F. Kennedy International Airport'), ('BOS', 'Logan International Airport'), ('MCO', 'Orlando International Airport')], default='BOS', max_length=3),
        ),
    ]
