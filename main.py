#This program crates an small web app that allow the user to ingress an small list of names, and then
#the app picks one at random, pairs with an image, and generate a card with the a name, an image, and
#a question, a timer is set and once the timer has run out, another set it's picked, until the list 
#has run out.

from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route("/")
def start():
    return render_template('index.html')
    