# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):

    domain = models.CharField(u'Домен проекта', max_length=255, unique=True)
    code = models.CharField(u'Код проекта', max_length=4, unique=True)
    owner = models.ForeignKey(User, verbose_name=u'Ответственный')

    class Meta:
        verbose_name = u'Проект'
        verbose_name_plural = u'Проекты'

    def __unicode__(self):
        return self.domain