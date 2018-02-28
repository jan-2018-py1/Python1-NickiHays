# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def index(request):
    course_list = {
        'courses': Course.objects.all()
    }
    return render(request, 'course_list/index.html', course_list)


def create(request):
    if 'id' not in request.session:
        request.session['id'] =''
    errors = Course.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        Course.objects.create(
            name = request.POST['name'],
            desc = request.POST['description']
        )
        new_course = Course.objects.last()
        request.session['id'] = new_course.id
        return redirect('/')


def remove(request, id):
    info = {
        'course' : Course.objects.get(id=id)
    }
    return render(request, 'course_list/remove.html', info)

def delete(request, id):
    x = Course.objects.get(id=id)
    x.delete()
    return redirect('/')