from flask import Flask, request, redirect, render_template
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends_flaskdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

@app.route('/addfriends', methods=['POST'])
def create():
    query = "INSERT INTO friends (name, age, friendship_length, created_at, updated_at) VALUES (:name, :age, :friendship_length, NOW(), NOW())"
    data = {
            'name': request.form['name'],
            'age':  request.form['age'],
            'friendship_length': request.form['length']
           }
    print mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)