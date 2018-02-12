from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


app = Flask(__name__)
app.secret_key = "ThisSecretKey"
mysql = MySQLConnector(app,'validemaildb')
                         
@app.route('/')                                                           
def index():
    query = "SELECT * FROM users"
    friends = mysql.query_db(query)
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def create():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)

    email = request.form['email']

    if len(email) < 1:
        flash("Please enter your email address.")
        return redirect('/')
    elif not EMAIL_REGEX.match(email):
        flash("Email is not valid")
        return redirect('/')
    else:
        query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
            'email': request.form['email'],
        }        
        mysql.query_db(query, data)
        flash("The email address you enter {} is a VALID email address! Thank you!".format(email))
        return render_template('success.html', all_users=users)

    
@app.route('/delete', methods=['POST'])
def delete():
    query = "DELETE FROM users ORDER BY id DESC limit 1"
    mysql.query_db(query)
    flash('The email has been successfully deleted')
    return redirect('/')

app.run(debug=True)