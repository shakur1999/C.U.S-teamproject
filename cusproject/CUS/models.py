from django.db import models

class cusapp(models.Model):
    title = models.CharField(max_length=255, default='', blank=True)
    description = models.TextField(max_length=255, default='', blank=True)
    location = models.CharField(max_length=255, default='', blank=True)

def __str__(self):
    return '%s' % self.title
    return '%s' % self.description
    return '%s' % self.location


# Create your models here.
