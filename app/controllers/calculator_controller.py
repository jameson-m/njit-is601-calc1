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
        # Get the values out of the form
        values = request.form.getlist("value")
        print("V A L U E S :")
        print(values)
        has_missing_values = "" in values
        if has_missing_values:
            flash("One or more values are missing. Please enter a value for each input.", "error")
        else:
            flash("Your calculation was successful!", "success")

            operation = request.form['operation']
            calc_tuple = tuple(values)
            
            # Call correct calculation
            getattr(Calculator, operation)(*calc_tuple)
            result = str(Calculator.get_last_result_value())
            results_history = DataManager.get_results_csv()
            results_history_formatted = list(map((lambda row: row[:1] + [datetime.utcfromtimestamp(int(row[1]))] + row[2:]), results_history))
            
            # return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result, results_history=results_history_formatted)
            return render_template('result.html', values=values, operation=operation, result=result, results_history=results_history_formatted)

        return render_template("calculator.html")

    @staticmethod
    def get():
        """Handles calculator's get route.
        """
        return render_template('calculator.html')
