# Implement a registration from, confirming via email

import os
import re

from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# This is Flask mail library, this is mostly copy paste from the documentation
# Requires that "Less secure app access" be on
# https://support.google.com/com/accounts/answer.6010255
app.config["MAIL_DEFAULT_SENDER"] = os.enviorn["MAIL_DEFAULT_SENDER"]
app.config["MAIL_PASSWORD"] = os.enviorn["MAIL_PASSWORD"]
# This is TCP port
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smpt.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.confod["MAIL_USERNAME"] = os.enviorn["MAIL_USERNAME"]
mail = Mail(app)

@app.route("/register", methods=["POST"])
def register():

    # Validate submission
    name = request.form.get("name")
    email = request.form.get("email")
    sport = request.form.get("sport")
    if not name or not email or sport not in SPORTS:
        return render_template("failure.html")

    # Send email
    message = Message("You are registered", recipients=[email])
    mail.send(message)

    # Confirm registration
    return render_template("successful.html")