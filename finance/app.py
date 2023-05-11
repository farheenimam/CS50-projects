import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user_id = session["user_id"]

    # For dislaying the information about the user

    user_info = db.execute("SELECT * FROM info WHERE user_id = ?", session["user_id"])

    if len(user_info) == 0:
        cash = db.execute("SELECT cash FROM users WHERE id =?", user_id)
        return render_template("index1.html", cash=cash)

    else:
        cash = db.execute("SELECT cash FROM users WHERE id =?", user_id)
        info = db.execute(
            "SELECT price, symbol, name, share, (price*SUM(share)) AS total FROM info WHERE user_id = ? GROUP BY symbol ORDER BY price DESC", user_id)
        sum = db.execute("SELECT SUM(price*share) AS total FROM info WHERE user_id = ?", user_id)
        sum_total = sum[0]["total"]
        sum_int = float(sum_total)
        cash_total = cash[0]["cash"]
        cash_int = float(cash_total)
        total = round(cash_int + sum_int)

        return render_template("index.html", info=info, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # For post request
    if request.method == "POST":
        symbol = lookup(request.form.get("symbol"))
        share = request.form.get("shares")

        # For errors
        if (request.form.get("symbol") == ""):
            return apology("Information is missing")
        if not symbol:
            return apology("Invalid symbol")
        if (share == ""):
            return apology("Information is missing")
        if not share.isdigit():
            return apology("Enter correct number")
        shares = int(share)
        stock = shares * symbol["price"]

        info = db.execute("SELECT * FROM info WHERE user_id = ? AND symbol = ?", session["user_id"], symbol["symbol"])
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        # For the first row[] of the cash column
        if (user_cash[0]["cash"] < stock):
            return apology("Not enough cash", 400)

        # If worked
        if len(info) == 0:
            db.execute("INSERT INTO info (user_id, symbol, share, name, price) VALUES(?, ?, ?, ?, ?)",
                       session["user_id"], symbol['symbol'], share, symbol['name'], symbol["price"])
            db.execute("INSERT INTO amount(total, user_id, symbol) VALUES(?, ?, ?)", stock, session["user_id"], symbol["symbol"])

        else:
            users = db.execute("SELECT share FROM info WHERE user_id = ? AND symbol = ?", session["user_id"], symbol["symbol"])
            user_share = users[0]["share"]
            total = db.execute("SELECT total FROM amount WHERE user_id = ? AND symbol = ?", session["user_id"], symbol["symbol"])
            user_total = total[0]["total"]

            db.execute("UPDATE info SET share = ? WHERE user_id = ? AND symbol = ?",
                       int(user_share) + shares, session["user_id"], symbol['symbol'])
            db.execute("UPDATE amount SET total = ? WHERE user_id = ? AND symbol = ?",
                       user_total + stock, session["user_id"], symbol['symbol'])
    
        db.execute("INSERT INTO sold (user_id, symbol, share, price) VALUES(?, ?, ?, ?)",
                   session["user_id"], symbol['symbol'], shares, symbol["price"])
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = user_cash[0]["cash"]
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - stock, session["user_id"])

        # Redirect to homepage
        flash("Brought!")
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    history = db.execute("SELECT * FROM sold WHERE user_id = ?", user_id)
    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("Logged In!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = lookup(request.form.get("symbol"))

        # For errors
        if (symbol == ""):
            return apology("Enter a symbol")
        if not symbol:
            return apology("Invalid symbol")
        else:
            return render_template("quoted.html", symbol=symbol)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    if request.method == "GET":
        return render_template("register.html")

    # For post request
    else:
        # For input
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        # For errors
        if (password == ""):
            return apology("Please Provide Password", 400)
        if (username == ""):
            return apology("Please Provide Username", 400)
        if (confirmation == ""):
            return apology("Submit Your Confirmation Password", 400)
        if (password != confirmation):
            return apology("Password Don't Match", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # To see that if the user already exist
        if len(rows) == 1:
            return apology("User alreay exist", 400)

        hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get("username"), hash)

        # Redirect user to the homepage
        flash("Registered!")
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        info = db.execute("SELECT symbol FROM info WHERE user_id = ? GROUP BY symbol", session["user_id"])
        return render_template("sell.html", info=info)

    # For the request via post
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # For errors
        if request.form.get("symbol") == None:
            return apology("Information is missing")
        if request.form.get("shares") == "":
            return apology("No shares")

        if not request.form.get("shares").isdigit():
            return apology("Enter correct number")

        data = db.execute("SELECT SUM(share), price FROM info WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)
        user_share = data[0]["SUM(share)"]
        price = data[0]["price"]

        if int(request.form.get("shares")) > int(user_share):
            return apology("You don't own that much shares")
        stock = int(shares) * price

        if (int(shares) == user_share):
            db.execute("DELETE FROM info WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)
            db.execute("DELETE FROM amount WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)
        else:
            total_share = int(user_share) - int(shares)
            users = db.execute("SELECT total FROM amount WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)
            total = users[0]["total"]
            user_total = round(total - price)
            db.execute("UPDATE info SET share = ? WHERE user_id = ? AND symbol = ?", total_share, session["user_id"], symbol)
            db.execute("UPDATE amount SET total = ? WHERE user_id = ? AND symbol = ?", user_total, session["user_id"], symbol)

        user_cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        cash = user_cash[0]["cash"]
        db.execute("UPDATE users SET cash = ? WHERE id = ?", round(cash + stock), session["user_id"])
        minus = int(shares) * (-1)
        db.execute("INSERT INTO sold (user_id, symbol, share, price) VALUES(?, ?, ?, ?)", session["user_id"], symbol, minus, price)
    flash("Sold!")
    return redirect("/")


@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """ Change Password """

    # if method GET, display password change form
    if request.method == "GET":
        return render_template("password.html")

    # if method POST, change password
    else:
        # return apologies if form not filled out
        if not request.form.get("oldpass") or not request.form.get("newpass") or not request.form.get("confirm"):
            return apology("missing old or new password", 403)

        # save variables from form
        oldpass = request.form.get("oldpass")
        newpass = request.form.get("newpass")
        confirm = request.form.get("confirm")

        # user's previous password
        hash = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])
        hash = hash[0]['hash']

        # if old password incorrect, return apology
        if not check_password_hash(hash, oldpass):
            return apology("old password incorrect", 403)

        # if new passwords don't match, return apology
        if newpass != confirm:
            return apology("new passwords do not match", 403)

        # hash new password
        hash = generate_password_hash(confirm)

        # Insert new hashed password into users table
        db.execute("UPDATE users SET hash = ? WHERE id = ?", hash, session["user_id"])

        # Rediret user
        flash("Password Changed!")
        return redirect("/logout")



