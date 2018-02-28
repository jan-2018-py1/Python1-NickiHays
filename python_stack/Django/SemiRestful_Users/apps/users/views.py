# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import User

def index(request):
    if 'id' not in request.session:
        request.session['id'] = ''
    users = User.objects.all()
    info = {
        'users': users
    }
    return render(request, 'users/index.html', info)

def show(request, id):
    context = {
        'user': User.objects.get(id=id),
        'first_name': User.objects.get(id=id).first_name,
        'last_name': User.objects.get(id=id).last_name,
        'email': User.objects.get(id=id).email,
        'created_at': User.objects.get(id=id).created_at,
    }
    return render(request, 'users/show.html', context)

def create(request):
    User.objects.create(
        first_name = request.POST['fname'],
        last_name = request.POST['lname'],
        email = request.POST['emailaddress']
    )
    new_user = User.objects.last()
    id = new_user.id
    return redirect('/users/{}'.format(id))

def new(request):
    return render(request, 'users/new.html')

def edit(request, id):
    request.session['id'] = id
    user = User.objects.get(id=id)
    info = {
        'user' : user
    }
    return render(request, 'users/edit.html', info)

def update(request):
    id = request.session['id']
    y = User.objects.get(id=id)
    y.first_name = request.POST['first_name']
    y.last_name = request.POST['last_name']
    y.email = request.POST['email']
    y.save()
    return redirect('/users/{}'.format(id))

def destroy(request, id):
    x = User.objects.get(id=id)
    x.delete()
    return redirect('/users')