"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.internet_history_controller import InternetHistoryController
from app.controllers.oop_controller import OOPController

app = Flask(__name__)
app.secret_key = b'_5#y2LfawFWOjowin\xec]/'

@app.route("/")
def index():
    """Homepage route"""
    return IndexController.get()

@app.route("/calculator", methods=["GET"])
def calculator_get():
    """Calculator route"""
    return CalculatorController.get()

@app.route("/calculator", methods=["POST"])
def calculator_post():
    """Perform calculator actions route"""
    return CalculatorController.post()

@app.route("/internet-history/timeline", methods=["GET"])
def internet_history_timeline_get():
    """Internet history timeline route"""
    return InternetHistoryController.get_timeline()

@app.route("/internet-history/people", methods=["GET"])
def internet_history_people_get():
    """Internet history people route"""
    return InternetHistoryController.get_people()

@app.route("/oop/tips-and-tricks", methods=["GET"])
def oop_tips_and_tricks_get():
    """Tips and tricks route"""
    return OOPController.get_tips_and_tricks()

@app.route("/oop/aaa-testing", methods=["GET"])
def oop_aaa_testing_get():
    """AAA testing route"""
    return OOPController.get_aaa_testing()

@app.route("/oop/oop-principles", methods=["GET"])
def oop_principles_get():
    """OOP principles route"""
    return OOPController.get_oop_principles()

@app.route("/oop/separation-of-concerns", methods=["GET"])
def oop_separation_of_concerns_get():
    """Separation of concerns route"""
    return OOPController.get_separation_of_concerns()
