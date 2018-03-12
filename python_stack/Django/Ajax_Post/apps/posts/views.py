# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from .models import Post
from django.core import serializers
import json

def index(request):
    return render(request, 'posts/index.html')

def all_json(request):
    posts = Post.objects.all()
    posts_json = serializers.serialize('json', posts)
    return HttpResponse(posts_json, content_type='application/json')

def all_html(request):
    return render(request, 'posts/all.html', {'posts': Post.objects.all() })

def create(request):
    Post.objects.create(content=request.POST['content'])
    return render(request, 'posts/all.html', {"posts": Post.objects.order_by('-id')})
