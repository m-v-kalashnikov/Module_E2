from django.db import models


class Email(models.Model):
    datetime_created = models.DateTimeField('Дата и время создания', auto_now=True)
    subject = models.CharField('Тема', max_length=100)
    message = models.CharField('Сообщение', max_length=500)
    seconds = models.PositiveIntegerField('Когда отправлять')
    to_whom = models.EmailField('Кому отправлять')
    datetime_must_be_send = models.DateTimeField('Дата и время отправки', null=True)

    class Meta:
        verbose_name = 'Електронное письмо'
        verbose_name_plural = 'Електронные письма'

    def __str__(self):
        return self.subject
    #
    # def save(self):
    #     from datetime import timedelta
    #     sec = timedelta(seconds=self.seconds)
    #
    #     if not self.id:
    #         self.datetime_must_be_send = self.datetime_created + sec
    #         super(Email, self).save()
