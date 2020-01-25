from django.db import models


class Email(models.Model):
    datetime_created = models.DateTimeField('Дата создания')
    subject = models.CharField('Тема', max_length=100)
    message = models.CharField('Сообщение', max_length=500)
    seconds = models.DateTimeField('Когда отправлять', null=True)
    to_whom = models.EmailField('Кому отправлять')

    class Meta:
        verbose_name = 'Електронное письмо'
        verbose_name_plural = 'Електронные письма'

    def __str__(self):
        return self.subject
