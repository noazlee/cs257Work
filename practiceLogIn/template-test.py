from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("/templates/index.html")


if __name__ == '__main__':
    my_port = 5128
    app.run(host='0.0.0.0', port = my_port) 
