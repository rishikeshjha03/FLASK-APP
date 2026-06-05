from flask import Flask
import pickle


app = Flask(__name__)
@app.route("/")

def hello_world():
    return "<h2> Hello, Welcome to my world! </h2>"