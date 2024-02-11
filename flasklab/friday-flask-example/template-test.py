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

@app.route('/randS')
def randSentence():
    listNames = ["Jeremiah", "Noah", "Warren", "Daya"]
    listAdj = ["Coward", "Loser", "Poopy", "Ugly", "Musty", "Crusty"]
    listPlace = ["O-Block", "Italy", "Chicago", "Ugly-stan"]
    listYear = ["5 BC", "2005", "2004", "2000", "1945", "1998"]
    num1 = random.randint(0,len(listNames)-1)
    name = listNames[num1]
    num2 = random.randint(0,len(listAdj)-1)
    adj = listAdj[num2]
    num3 = random.randint(0,len(listPlace)-1)
    place = listPlace[num3]
    num4 = random.randint(0,len(listYear)-1)
    year = listYear[num4]

    return render_template("randStory.html", randName=name, randAdjective=adj,randPlace=place,randYear=year)


if __name__ == '__main__':
    my_port = 5128
    app.run(host='0.0.0.0', port = my_port) 
