"""OOP controller"""
from flask import render_template
from app.controllers.controller import ControllerBase

class OOPController(ControllerBase):
    """OOP controller"""
    @staticmethod
    def get_tips_and_tricks():
        """Handles getting OOP tips and tricks article template.
        """
        return render_template("oop/tips-and-tricks.html")
    @staticmethod

    def get_aaa_testing():
        """Handles getting OOP AAA testing template.
        """
        return render_template("oop/aaa-testing.html")

    @staticmethod
    def get_oop_principles():
        """Handles getting OOP principles article template.
        """
        return render_template("oop/oop-principles.html")

    @staticmethod
    def get_separation_of_concerns():
        """Handles getting OOP separation of concerns article template.
        """
        return render_template("oop/separation-of-concerns.html")
