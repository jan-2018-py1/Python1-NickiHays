# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, "randWord/index.html")

def create(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 1
    else:
        request.session['attempt'] += 1
    context = {
        "rand" : get_random_string(length=14)
    }
    return render(request, "randWord/index.html", context)
    
#def generate(request):
#    return redirect('/random_word')


def reset(request):
    request.session['attempt'] = 0
    return redirect('/random_word')
