from django.db import models

class Games(models.Model):
    name = models.CharField('Game name', max_length=50)
    type = models.CharField('Game type', max_length=50)
    popularity = models.CharField('Game popularity', max_length=50)
    buy = models.CharField('Buy game', max_length=50)
    date = models.DateTimeField('Today:')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

class Users(models.Model):
    username = models.CharField('User name', max_length=50)
    email = models.CharField('Email', max_length=50)
    password = models.CharField('Password', max_length=50)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'