from flask import Flask, render_template, request

# __name__ means turn the current file in the flask application
app = Flask(__name__)

@app.route("/")
def index():
    return "hello,world"

