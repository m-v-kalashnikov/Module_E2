# Generated by Django 2.2.5 on 2020-01-23 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emailer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='datetime_created',
            field=models.DateTimeField(verbose_name='Дата создания'),
        ),
    ]
