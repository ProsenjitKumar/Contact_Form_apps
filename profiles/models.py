from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(default='description defult text')
    location = models.CharField(max_length=70, default='Bangladesh')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
