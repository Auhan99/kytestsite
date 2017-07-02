# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here
from random import randrange
from django.contrib.auth.decorators import login_required
from .forms import SignUpForms
from django.contrib.auth import logout


def home(request):
    title='Welcome'
    form=SignUpForms(request.POST or None)
    context ={
        "forms":form
    }
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user_name=instance.email.split('@')[0]+str(randrange(0, 101))
        instance.save()
    if request.method=="POST":
        context={
           
            "uname":"your username is "+instance.user_name
        }
    return render(request,"home.html",context)#it will look for home.html in template dir. of sideapp settings.templates is untouched

def logged_in(request):

    return render(request,'logged_in.html',{})
