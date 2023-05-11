from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Configure session
# Here we are telling to store cookie on the server hard drive
# Hence we don't want them to be permanent so thats why we use false, so as you closes the browser the session go away
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# Here we tell app to support session
Session(app)


@app.route("/")
def index():
    if not session.get("name")
        return redirect("/login")
    return render_template("index.html")


# If the user got into this route via post it means they already has submitted the form
  # This means if they are no name in the input again redirect the user to same page login page
    # Or if they did submit the form via post, we are going to store in the session at the name key, whatever the human name is.
    # and then redirect them to the slash as in line#22 otherwise we will show them the login form
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")


# This means when the user logout change the name to null ('as in line#38) and redirect them to slash("first page")
@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")