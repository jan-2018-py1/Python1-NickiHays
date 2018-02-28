# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def register(request):
    response = 'Placeholder for users to create a new user record'
    return HttpResponse(response)

def login(request):
    response = 'Placeholder for users to login'
    return HttpResponse(response)

def new(request):
    return redirect('/register')

def users(request):
    response = 'Placeholder to later display all the list of users'
    return HttpResponse(response)