from flask import request, render_template, flash
from datetime import datetime
from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from data_manager.manager import DataManager

class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        """Handles calculator's post route.
        """
        if request.form["value1"] == "" or request.form["value2"] == "":
            flash("You must enter a value for value 1 and or value 2", "error")
        else:
            flash("Your calculation was successful!", "success")

            # Get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            calc_tuple = (value1, value2)
            
            # Call correct calculation
            getattr(Calculator, operation)(*calc_tuple)
            result = str(Calculator.get_last_result_value())
            results_history = DataManager.get_results_csv()
            results_history_formatted = list(map((lambda row: row[:1] + [datetime.utcfromtimestamp(int(row[1]))] + row[2:]), results_history))
            
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result, results_history=results_history_formatted)
        return render_template("calculator.html")

    @staticmethod
    def get():
        """Handles calculator's get route.
        """
        return render_template('calculator.html')
