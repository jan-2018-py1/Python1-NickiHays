from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "ThisSecretKey"
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

mysql = MySQLConnector(app,'login_regdb')
                         
@app.route('/')                                                           
def index():
    if "user_id" in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def create():
    print request.form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    confirm = md5.new(request.form['confirm']).hexdigest()
    valid = True

    if len(first_name) < 2 or first_name.isalpha() == False:
        flash('Please enter a valid first name')
        valid = False

    if len(last_name) < 2 or last_name.isalpha() == False:
        flash('Please enter a valid last name')
        valid = False

    if len(email) < 1 or not EMAIL_REGEX.match(email):
        flash("Please enter a valid email address.")
        valid = False

    if len(password) < 8 or password != confirm:
        flash('Password must be at least 8 characters long and match the confirm password')

    if valid:
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)"
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password
        }        
        x = mysql.query_db(query, data)
        session['user_id'] = x
        return redirect('/dashboard')

    else:
        return redirect('/')

@app.route('/dashboard')
def dashboard():
    query = "SELECT * FROM users WHERE id = :user_id"
    data = {
		"user_id":session["user_id"]
	}
    user = mysql.query_db(query, data) 
    return render_template("dashboard.html", user = user[0])
    
@app.route("/login", methods=["POST"])
def login():
	query = "SELECT * FROM users WHERE email = :post_email"
	data = {
		"post_email":request.form["email"]
	}
	user = mysql.query_db(query, data)
	print user
	if len(user) > 0:
		user = user[0]
		if user["password"] == md5.new(request.form["password"]).hexdigest():
			session["user_id"] = user["id"]
			return redirect("/dashboard")
	flash("Email and password not found")
	return redirect("/")

@app.route('/logout')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)