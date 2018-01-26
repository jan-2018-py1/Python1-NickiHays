from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsKey'

import random
import datetime
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d %H:%M")
print today

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    print session['gold']
    print session['activities']   
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def gold_count():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []

    ninja_choice = str(request.form['building'])

    if ninja_choice == 'Farm':
        goldNum = random.randrange(10,20)
        session['gold'] = session['gold'] + goldNum 
        print goldNum
        activity = 'Yay! You earned {} gold from the farm!({})'.format(goldNum, today)
        print activity
        session['activities'].insert(0,activity)

    elif ninja_choice == 'Cave':
        goldNum = random.randrange(5,10)
        session['gold'] = session['gold'] + goldNum
        print goldNum
        activity = 'Yay! You earned {} gold from the cave! ({})'.format(goldNum, today)
        print activity
        session['activities'].insert(0,activity)

    elif ninja_choice == 'House':
        goldNum = random.randrange(2,5)
        session['gold'] = session['gold'] + goldNum
        print goldNum
        activity = 'Yay! You earned {} gold from the house!({})'.format(goldNum, today)
        print activity
        session['activities'].insert(0,activity)

    elif ninja_choice == 'Casino':
        goldNum = random.randrange(-50,50)
        if goldNum > 0:
            session['gold'] = session['gold'] + goldNum
            print goldNum
            activity = 'Yay! You earned {} gold from the casino!({})'.format(goldNum, today)
            print activity
            session['activities'].insert(0,activity)
 
        elif goldNum < 0:
            session['gold'] = session['gold'] + goldNum
            print goldNum
            activity = 'Bummer! You lost {} gold from the casino! Better luck next time.({})'.format(goldNum * -1, today)
            print activity
            session['activities'].insert(0,activity)

        else:
            session['gold'] = session['gold'] + goldNum
            print goldNum
            activity = 'You did not win or lose this time at the casino!({})'.format(today)
            print activity
            session['activities'].insert(0,activity)

    return redirect('/')
 
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
app.run(debug=True) 


