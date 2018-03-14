# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from myapp.forms import FormOne,FormTwo
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.

def index(request):
    return render(request,'myapp/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == 'POST':
        one = FormOne(request.POST)
        two = FormTwo(request.POST)

        if one.is_valid() and two.is_valid():

            user = one.save()
            user.set_password(user.password)
            user.save()

            profile = two.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered=True
        else:
            print(one.errors,two.errors)
    else:
        one = FormOne()
        two = FormTwo()

    return render(request,'myapp/registration.html',{'formone':one,'formtwo':two,'registered':registered})


def user_login(request):

    if request.method=='POST':

        user1 = request.POST.get('user')
        password = request.POST.get('pass')

        user = authenticate(username = user1,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("session timed out")

        else:
            return HttpResponse("invalid username and password")

    return render(request,'myapp/login.html')