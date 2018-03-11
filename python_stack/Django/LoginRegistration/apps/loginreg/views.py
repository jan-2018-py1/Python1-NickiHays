# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def index(request):
    if 'id' not in request.session:
        request.session['id'] = ''
    return render(request, 'loginreg/index.html')

def add(request):
    if 'id' not in request.session:
        request.session['id'] = ''
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        password = User.objects.password_hash(request.POST['password'])
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = password,
        )
        new_user = User.objects.last()
        request.session['id'] = new_user.id
        request.session['name'] = new_user.first_name
        return redirect('/success')

def login(request):
    print request.POST
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        login_user = User.objects.filter(email=request.POST['email'])
        if len(login_user) > 0:
            name = login_user[0].first_name
            request.session['name'] = name
            return redirect('/success')
        else:
            messages.error(request, 'Login info does not match database- please try again or please register')
            return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def success(request):
    return render(request, 'loginreg/success.html')