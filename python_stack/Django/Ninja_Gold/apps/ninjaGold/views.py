# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from time import gmtime, strftime, localtime
import random

today = strftime("%Y-%m-%d %H:%M %p", localtime())

def index(request):
#    if 'gold' not in request.session:
#        request.session['gold'] = 0
#    if 'activities' not in request.session:
#        request.session['activities'] = []
    
    return render(request, 'ninjaGold/index.html')

def process(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []

    ninja_choice = str(request.POST['building'])

    if ninja_choice == 'Farm':
        goldNum = random.randrange(10,20)
        request.session['gold'] = request.session['gold'] + goldNum
        activity = 'Yay! You earned {} gold from the farm!({})'.format(goldNum, today)
        request.session['activities'].insert(0,activity)

    elif ninja_choice == 'Cave':
        goldNum = random.randrange(5,10)
        request.session['gold'] = request.session['gold'] + goldNum
        activity = 'Yay! You earned {} gold from the cave!({})'.format(goldNum, today)
        request.session['activities'].insert(0,activity)

    elif ninja_choice == 'House':
        goldNum = random.randrange(2,5)
        request.session['gold'] = request.session['gold'] + goldNum
        activity = 'Yay! You earned {} gold from the house!({})'.format(goldNum, today)
        request.session['activities'].insert(0,activity)

    elif ninja_choice == 'Casino':
        goldNum = random.randrange(-50,50)
        if goldNum > 0:
            request.session['gold'] = request.session['gold'] + goldNum
            activity = 'Yay! You earned {} gold from the casino!({})'.format(goldNum, today)
            request.session['activities'].insert(0,activity)

        elif goldNum < 0:
            request.session['gold'] = request.session['gold'] + goldNum
            activity = 'Bummer! You lost {} gold from the casino! Better luck next time.({})'.format(goldNum * -1, today)
            request.session['activities'].insert(0,activity)

        else:
            request.session['gold'] = request.session['gold'] + goldNum
            activity = 'You did not win or lose this time at the casino!({})'.format(today)
            request.session['activities'].insert(0,activity)

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
