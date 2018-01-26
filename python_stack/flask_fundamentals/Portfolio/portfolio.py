from flask import Flask, render_template 
app = Flask(__name__)    
                         
@app.route('/')                                                           
def hello_world():
  return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('index_projects.html')

@app.route('/about')
def about_me():
    return render_template('index_about.html')

app.run(debug=True) 