"""Index controller"""
from flask import render_template
from app.controllers.controller import ControllerBase

class IndexController(ControllerBase):
    """Index controller"""
    @staticmethod
    def get():
        """Gets the homepage"""
        return render_template("index.html")
