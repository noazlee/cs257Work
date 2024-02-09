from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("randStory.html")



@app.route('/rand/<low>/<high>')
def rand(low, high):
    #Input values that come from a URL (i.e., @app.route)
    #   are always strings so I need to convert the type to int
    low_int = int(low)
    high_int = int(high)
    
    num = random.randint(low_int, high_int)
    return render_template("random.html", randNum = num)

@app.route('/pookie')
def pookie():
    return render_template("pookie.html")

if __name__ == '__main__':
    my_port = 5128
    app.run(host='0.0.0.0', port = my_port) 
