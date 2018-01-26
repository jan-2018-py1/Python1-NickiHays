from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsKey'

#import random


@app.route('/')
def index():
    import random
    if 'myNum' in session:
        print session['myNum']
        return render_template('index.html')
    else:
        session['myNum'] = random.randint(0,101)
        print session['myNum']
        return render_template('index.html')

@app.route('/process', methods=['POST'])
def random():
    session['guess'] = int(request.form['guess'])
    return render_template('guess.html')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('myNum')
    return redirect('/')


app.run(debug=True) 


