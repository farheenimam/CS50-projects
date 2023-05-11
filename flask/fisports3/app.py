# Implement a register form, storing registrattion in a sqlite database , with support fro eregistration

from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# This means use SQLlite to talk to file locallly
# The first 2 slah is in the url while the 3 slash mean 'in the current folder'
db = SQL("sqlite:///fisports.db")

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():

    #Validate submission
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name or sport not in SPORTS:
        return render_template("failure.html")

   #Remember registrants
    db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)

    # Confirm registrants
    # This redirect function do 301 307 and 302 function for us
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    registrants  = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)

# This is, so someone can remove themselve if they want
# To avoid somoene maliciously typing this in the url (deregister?id=2) and linking this to someone by cross-site request forgey, this can reomve someone from the registration list
# so we use POST
@app.route("/deregister", methods=["POST"])
def deregister():

    # Forget registrant
    id = request.form.get("id")
    if id:
        # Over here we are using id because if want to delete for example 'Carter', but there might be more than one 'Carter'
        # so we uniquely identify each individual using 'id'
        db.execute("DELETE FROM registrants WHERE id = ?", id)
    return redirect("/registrants")
