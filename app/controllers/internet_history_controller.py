from flask import render_template
from app.controllers.controller import ControllerBase

class InternetHistoryController(ControllerBase):
    @staticmethod
    def get_timeline():
        """Handles getting Internet History timeline article template.
        """
        return render_template("internet_history/timeline.html")

    @staticmethod
    def get_people():
        """Handles getting Internet History people article template.
        """
        return render_template("internet_history/people.html")
