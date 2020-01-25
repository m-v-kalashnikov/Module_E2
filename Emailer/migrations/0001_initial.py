# Generated by Django 2.2.5 on 2020-01-25 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now=True, verbose_name='Дата и время создания')),
                ('subject', models.CharField(max_length=100, verbose_name='Тема')),
                ('message', models.CharField(max_length=500, verbose_name='Сообщение')),
                ('seconds', models.PositiveIntegerField(verbose_name='Когда отправлять')),
                ('to_whom', models.EmailField(max_length=254, verbose_name='Кому отправлять')),
                ('datetime_must_be_send', models.DateTimeField(null=True, verbose_name='Дата и время отправки')),
            ],
            options={
                'verbose_name': 'Електронное письмо',
                'verbose_name_plural': 'Електронные письма',
            },
        ),
    ]
