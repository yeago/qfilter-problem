from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    info = models.ForeignKey('Info')
    date = models.DateTimeField()
    person = models.ForeignKey('Person')
    def __unicode__(self):
        return "%s - %s - %s " % (self.info, self.date, self.person)


class Info(models.Model):
    name = models.CharField(max_length=1)
    def __unicode__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=1)
    def __unicode__(self):
        return self.name
