# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'amadon_app/index.html')

def buy(request):
    if 'item_count' not in request.session:
        request.session['item_count'] = 0

    if 'purchase_cost' not in request.session:
        request.session['purchase_cost'] = 0

    if 'total_cost' not in request.session:
        request.session['total_cost'] = 0

    product_id = request.POST['product_id']
    products = {
        '1001' : {'item': 'Dojo Shirt', 'price': 19.99},
        '1002' : {'item': 'Dojo Sweater', 'price': 29.99},
        '1003' : {'item': 'Dojo Cup', 'price': 4.99},
        '1004' : {'item': 'Algorithm Book', 'price': 49.99}
    }

    purchase = {
        'item' : products[product_id]['item'],
        'quantity' : request.POST['quantity'],
        'price' : products[product_id]['price']
    }

    request.session['item'] = products[product_id]['item']
    purchase_cost = purchase['price'] * int(purchase['quantity'])
    
    request.session['purchase_cost'] = purchase_cost
    request.session['total_cost'] += purchase_cost
    request.session['item_count'] += int(purchase['quantity'])

    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'amadon_app/checkout.html')



def back(request):
    return redirect('/')