# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
class SignUp(models.Model):
    email=models.EmailField()
    user_name=models.CharField(max_length=120,blank=True,null=True,default='')
    name=models.CharField(max_length=120,blank=True,null=True,default='')
    time=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    
    def __unicode__(self):
     return self.email

