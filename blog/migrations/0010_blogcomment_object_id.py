# Generated by Django 3.1.2 on 2020-11-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blogcomment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
