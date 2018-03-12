# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from .models import *
from django.core import serializers
import json

def index(request):
    return render(request, 'notes/index.html')

def all_html(request):
    return render(request, 'notes/all.html', {'notes': Note.objects.order_by('-id')})

def create(request):
    notes = Note.objects.create(title=request.POST['title'], content=request.POST['content'])
    request.session['id'] = notes.id
    return render(request, 'notes/all.html', {'notes': Note.objects.order_by('-id')})

def edit(request, id):
    content = {
        "note": Note.objects.get(id=id)
    }
    return render(request, 'notes/edit.html', content)

def change(request,id):
    new_note = Note.objects.get(id=id)
    if len(request.POST['title']) > 0:
        new_note.title = request.POST['title']
    if len(request.POST['content']) > 0:
        new_note.content = request.POST['content']
    new_note.save()
    notes = Note.objects.all()
    return render(request, 'notes/all.html', {'notes': notes})


def delete(request, id):
    x = Note.objects.get(id=id)
    x.delete()
    return render(request, 'notes/all.html', {'notes': Note.objects.order_by('-id')})