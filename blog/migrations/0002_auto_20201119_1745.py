# Generated by Django 3.1.2 on 2020-11-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogfield',
            name='status',
        ),
        migrations.AddField(
            model_name='blogfield',
            name='time_to_read',
            field=models.IntegerField(default=2),
        ),
    ]
