"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController

app = Flask(__name__)
app.secret_key = b'_5#y2LfawFWOjowin\xec]/'

@app.route("/")
def index():
    """index  Route Response"""
    return IndexController.get()

@app.route("/calculator", methods=["GET"])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=["POST"])
def calculator_post():
    return CalculatorController.post()
