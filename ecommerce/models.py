from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

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

CHOICES = (('1', 'Mr.',), ('2', 'Mrs.',))
class Account_aff(models.Model):
    user = models.OneToOneField(User)
    affliate_id = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    title = models.CharField(max_length=100,choices=CHOICES,default='')
    dob = models.DateField(default = datetime.now,blank=True)

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username
