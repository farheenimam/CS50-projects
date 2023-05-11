from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    # Here 'world' is the default when the user dont type anyting
    # But over here this default will not work even thought u don't type anything beacuse it takes "" this as a parameter
    name = request.form.get("name", "world")
    return render_template("greet.html", name=name)