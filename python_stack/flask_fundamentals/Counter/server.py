from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsKey'

@app.route('/')
def count():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_two():
    session['count'] += 1
    return redirect ('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect ('/')


app.run(debug=True) 


#counts how many times root route has been viewes
#level 1 = add +2 button under counter that reloads page & increments by 2
#  use another route
#level 2 = add reset button to reset back to 1
#  use another route