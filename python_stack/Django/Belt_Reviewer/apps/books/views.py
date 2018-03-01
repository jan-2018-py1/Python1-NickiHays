# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def books(request):
    user = User.objects.get(id=request.session['user_id'])
    books = Book.objects.all()
    last_three = Review.objects.all().order_by('-created_at')[:3]
    content = {
        'alias': user.alias,
        'books': books,
        'recent_reviews': last_three
    }
    return render(request, 'books/dashboard.html', content)

def add(request):
    if 'user_id' not in request.session:
        return redirect('/')
    content = {
        'authors': Author.objects.all()
    }

    return render(request, 'books/books_add.html', content)

def books_create(request):
    if 'user_id' not in request.session:
        return redirect('/')

    if 'book_id' not in request.session:
        request.session['book_id'] = ''

    if request.POST['new_author'] != '':
        if len(Author.objects.filter(name=request.POST['new_author'])):
            messages.error(request, "The author you entered already exists, please try again and select the author from the provided list")
            return redirect('/books/add')
        else:
            author = Author.objects.create(name=request.POST['new_author'])
    else:
        author = Author.objects.get(name=request.POST['author'])
    
    new_book = Book.objects.create(
        title = request.POST['title'],
        author = author
    )
    
    Review.objects.create(
        book = Book.objects.get(id=new_book.id),
        user = User.objects.get(id=request.session['user_id']),
        content = request.POST['book_review'],
        stars = request.POST['rating']
    )
    request.session['book_id'] = new_book.id
    url = '/books/{}'.format(new_book.id)

    return redirect(url)

def books_info(request, book_id):
    if Book.objects.filter(id=book_id).exists():
        current_book = Book.objects.get(id=book_id)
    else:
        return redirect('/books')


    content = {
        'current_book': current_book.title,
        'author': Author.objects.get(books=current_book.id).name,
        'book_id': current_book.id,
        'reviews': Review.objects.filter(book=current_book),
        'books': Book.objects.all(),
        'user_id': request.session['user_id']
    }
    return render(request, 'books/books_info.html', content)

def reviews_create(request):
    if 'user_id' not in request.session:
        return redirect('/')
    book_id = Book.objects.get(id=request.POST['book_id'])
    Review.objects.create(
        book = book_id,
        user = User.objects.get(id=request.session['user_id']),
        content = request.POST['review'],
        stars = request.POST['rating']
    )
    url = '/books/{}'.format(request.POST['book_id'])
    return redirect(url)

def reviews_delete(request, review_id):
    y = Review.objects.get(id=review_id).book.id
    x = Review.objects.get(id=review_id)
    x.delete()
    
    url = '/books/{}'.format(y)
    return redirect(url)

def user_info(request, user_id):
    if User.objects.filter(id=user_id).exists():
        user = User.objects.get(id=user_id)
    else:
        return redirect('/')
    info = {
        'alias': user.alias,
        'name': user.first_name + " " + user.last_name,
        'email': user.email,
        'reviews': len(user.reviews.all()),
        'books': user.reviews.all()
    }
    return render(request, 'books/user_info.html', info)