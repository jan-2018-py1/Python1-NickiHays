from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#display 'No ninja here'                         
@app.route('/')                                                           
def index():
    return render_template('index.html')

#display all 4 Ninja turtles
@app.route('/ninja')                                                           
def turtles():
    return render_template('turtles.html')

#display each turtle based on the color chosen in the url
#blue = Leonardo
#orange = Michelangelo
#red = Raphael
#purple = Donatello
#any other color = notapril.jpg
@app.route('/ninja/<color>')
def ninja_color(color):
    if color == "blue":
        return render_template('leonardo.html')
    elif color == "orange":
        return render_template('michelangelo.html')
    elif color == "red":
        return render_template('raphael.html')
    elif color == "purple":
        return render_template('donatello.html')
    else:
        return render_template('notapril.html')


app.run(debug=True) 

