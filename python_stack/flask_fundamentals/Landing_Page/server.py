from flask import Flask, render_template, request, redirect
app = Flask(__name__)    
                         
@app.route('/')                                                           
def index():
  return render_template('index.html')

@app.route('/ninjas')                                                           
def ninja():
  return render_template('ninjas.html')

@app.route('/dojos/new')                                                           
def dojo():
  return render_template('dojos.html')

@app.route('/dojos/new', methods=['POST'])
def create_user():
    print "Got Post Info"
    name = request.form['name']
    email = request.form['email']
    return redirect('/')

app.run(debug=True) 