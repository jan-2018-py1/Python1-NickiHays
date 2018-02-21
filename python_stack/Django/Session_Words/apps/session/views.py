# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime, localtime


def index(request):
    return render(request, 'session/index.html')


def create(request):
    if 'info' not in request.session:
        request.session['info'] = []
    new_word = {
        'word' : request.POST['word'],
        'color' : request.POST['color'],
        'time' : strftime("%Y-%m-%d %H:%M %p", localtime())
    }

    if 'bold' in request.POST:
        new_word['bold'] = 'bold'
    else:
        new_word['bold'] = 'normal'

    data = request.session['info']
    data.append(new_word)

    request.session['info'] = data
    print data
    
    return render(request, 'session/index.html', new_word)


def reset(request):
    request.session.clear()
    return redirect('/')