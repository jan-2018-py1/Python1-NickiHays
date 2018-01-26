from flask import Flask, render_template, request, redirect, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "ThisSecretKey"
                         
@app.route('/')                                                           
def index():
    return render_template('index.html')




@app.route('/process', methods=["POST"])
def results():  
    fname = request.form['first_name']
    lname = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm = request.form['confirm']

    
    if len(fname) < 1:
        flash("Please enter your first name.")

    if fname.isalpha() == False:
        flash("Your first name cannot contain numbers.")

    if len(lname) < 1:
        flash("Please enter your last name.")

    if lname.isalpha() == False:
        flash("Your last name cannot contain numbers.")

    if len(email) < 1:
        flash("Please enter your email address.")
    elif not EMAIL_REGEX.match(email):
        flash("Please enter a valid email address.")

    if len(password) < 8:
        flash("Please enter a password that is at least 8 characters long.")

    if len(confirm) < 1:
        flash("Please confirm your password.")
    
    if password > confirm:
        flash("Your passwords do not match!")

    if password < confirm:
        flash("Your passwords do not match!")

    if password.islower() == True:
        flash("Your password must contain one uppercase character.")

    if password.isalpha() == True:
        flash("Your password must contain one number.")
        
        return redirect('/')

    else:
        flash("Thank you for submitting your information, {}".format(fname))

        return redirect('/')


app.run(debug=True) 

#validate all fields required
#validate no numbers in name
#password > 8 characters
#valid email
#passwoard & confirm should match


#Ninja- password with 1 uppercase & 1 number

#Hacker- add birthdate, validate & from the past