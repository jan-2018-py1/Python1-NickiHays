# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def index(request):
    if 'user_id' not in request.session:
        return render(request, 'users/index.html')
    else:
        return redirect('/books')

def register(request):
    if 'user_id' in request.session:
        return redirect('/books')
    
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        password = User.objects.password_hash(request.POST['password'])
        User.objects.create(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            alias = request.POST['alias'],
            email = request.POST['email'],
            password = password
        )
        new_user = User.objects.last()
        request.session['user_id'] = new_user.id
        request.session['alias'] = new_user.alias
        return redirect('/books')

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
            alias = login_user[0].alias
            user_id = login_user[0].id
            request.session['user_id'] = user_id
            request.session['alias'] = alias
            return redirect('/books')
        else:
            messages.error(request, 'Login info does not match database- please try again or please register')
            return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')


