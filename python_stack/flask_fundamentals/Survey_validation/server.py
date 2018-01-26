from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "ThisSecretKey"
                         
@app.route('/')                                                           
def index():
    return render_template('index.html')




@app.route('/results', methods=["POST"])
def results():  
    name = request.form['name']
    location = request.form['location']
    language = request.form['favelang']
    comment = request.form['comment']
    
    if len(name) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    else:
        flash("Success! Your name is {}".format(name))
    
    if len(comment) < 1:
        flash("Please add a comment!")
        return redirect('/')
    elif len(comment) > 120:
        flash("Please keep comments at 120 characters or less")  
        return redirect('/')  
    else:
        flash("Thank you for your comments!")

    return render_template('results.html', name=name, location=location, language=language, comment=comment)


app.run(debug=True) 

#validate name & comment to make sure not blank
#validate comment no longer than 120 characters