from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=120)
    firstname=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    #website=models.URLField(blank=True)
    # picture=models.ImageField(upload_to='profile_images',blank=True)
    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username
