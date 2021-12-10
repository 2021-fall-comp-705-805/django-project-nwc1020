# Generated by Django 3.1.13 on 2021-12-10 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20211209_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='defaultAirport',
            field=models.CharField(choices=[('ATL', 'Hartsfield-Jackson International Airport'), ('LAX', 'Los Angeles International Airport'), ('JFK', 'John F. Kennedy International Airport'), ('BOS', 'Logan International Airport'), ('MCO', 'Orlando International Airport'), ('ABE', 'Lehigh Valley International Airport (was Allentown–Bethlehem–Easton International Airport)')], default='BOS', max_length=3),
        ),
    ]