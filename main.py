#This program crates an small web app that allow the user to ingress an small list of names, then
#the app picks one at random, pairs it with an image, and generate a card with the a name, an image,
#and a question, a timer is set and once the timer has run out, another set it's picked, until the list 
#has run out.

from flask import Flask
from flask import render_template, request
import random

app = Flask(__name__)
 
@app.route("/")
def start():
    return render_template('index.html')

@app.route("/picker", methods=["POST"])
def picker():
    if request.method == "POST":
        data = request.form
        participants = []
        for p in request.form:
            participants.append(request.form[p])
        random.shuffle(participants)
        return render_template('success.html', participants=participants)