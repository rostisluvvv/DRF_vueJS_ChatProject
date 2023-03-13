from django.db import models
from django.contrib.auth.models import User
# from djoser.urls.base import User


class Room(models.Model):
    creator = models.ForeignKey(User,
                                verbose_name='Создатель комнаты',
                                on_delete=models.CASCADE)
    invited = models.ManyToManyField(User,
                                     verbose_name='участники',
                                     related_name='invited_user')
    date = models.DateTimeField('дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Комната чата'
        verbose_name_plural = 'Комнаты чатов'


class Chat(models.Model):
    room = models.ForeignKey(Room,
                             verbose_name='комната чата',
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             verbose_name='пользователь',
                             on_delete=models.CASCADE)
    text = models.TextField('Сообщение', max_length=500)
    date = models.DateField('дата отправки', auto_now_add=True)

    class Meta:
        verbose_name = 'сообщение чат'
        verbose_name_plural = 'сообщения чатов'
