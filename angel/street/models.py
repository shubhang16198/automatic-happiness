from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
	
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	art = models.TextField(max_length=100,blank=False)
	mobile_no = models.TextField(blank=False)