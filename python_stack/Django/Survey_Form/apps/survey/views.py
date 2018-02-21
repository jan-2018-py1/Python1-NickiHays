# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 1
    request.session['attempt'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/results')

def results(request):
    return render(request, 'survey/results.html')