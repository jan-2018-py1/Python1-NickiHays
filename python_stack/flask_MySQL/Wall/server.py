from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re
import md5

app = Flask(__name__)
app.secret_key = "ThisSecretKey"
mysql = MySQLConnector(app, 'walldb')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
                         
@app.route('/')                                                           
def index():
    if "user_id" in session:
        return redirect('/wall')
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def create():
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
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, Now(), Now())"
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password
        }        
        userNew = mysql.query_db(query, data)
        session['user_id'] = userNew
        session['first_name'] = first_name
        return redirect('/wall')

    else:
        return redirect('/')

@app.route('/wall')
def wall():
    queryMessages = "SELECT users.id as poster_id, users.first_name as poster_fname, users.last_name as poster_lname, messages.id as message_id, messages.message as message, DATE_FORMAT(messages.created_at, '%M %e, %Y %h:%i %p') as message_date FROM users JOIN messages ON users.id = messages.user_id ORDER BY messages.id DESC"
    messages = mysql.query_db(queryMessages)

    queryComments = "SELECT users.id as commenter_id, users.first_name as commenter_fname, users.last_name as commenter_lname, comments.message_id as comment_message_id, comments.comment as comment, DATE_FORMAT(comments.created_at, '%M %e, %Y %h:%i %p') as comment_date FROM users JOIN comments ON users.id = comments.user_id ORDER BY comments.id DESC"
    comments = mysql.query_db(queryComments)


    return render_template("logged_in.html", messages = messages, comments = comments)

@app.route('/messages', methods=['POST'])
def addmessages():
    message = request.form['message']
    if len(message) < 1:
        return redirect('/wall')
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, Now(), Now())"
    data = {
        'user_id': session['user_id'],
        'message': message
    }
    message_id = mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comments', methods=['POST'])
def addcomments():
    comment = request.form['comment']
    if len(comment) < 1:
        return redirect('/wall')
    message_id = request.form['message_id']
    query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, Now(), Now())"
    data = {
        'user_id': session['user_id'],
        'message_id': message_id,
        'comment': comment
    }
    comment_id = mysql.query_db(query, data)
    return redirect('/wall')

@app.route("/login", methods=["POST"])
def login():
	query = "SELECT * FROM users WHERE users.email = :post_email"
	data = {
		"post_email":request.form["email"],
	}
	user = mysql.query_db(query, data)
        if len(user) > 0:
            user = user[0]
            if user['password'] == md5.new(request.form["password"]).hexdigest():
                session['user_id'] = user['id']
                return redirect('/wall')
        flash('Email and Password not found')
        return redirect('/')


@app.route('/logout')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)