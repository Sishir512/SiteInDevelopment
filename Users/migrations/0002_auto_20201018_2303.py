# Generated by Django 3.1.2 on 2020-10-18 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='focusususer',
            name='fullname',
            field=models.CharField(max_length=30),
        ),
    ]