# Calculator Project Setup
[![Build Status](https://app.travis-ci.com/jameson-m/njit-is601-calc1.svg?branch=main)](https://app.travis-ci.com/jameson-m/njit-is601-calc1)

Run Pip Install
pip install -r requirements.txt

To run tests, Lint, and Coverage report use this command:

pytest  --pylint --cov

.pylintrc is the config for pylint
.coveragerc is the config for coverage
setup.py is a config file for pytest

## CSV and File Handling Assignment
Here is a screenshot of the local test coverage. I am using a python 3.8.12 local virtual environment to run the code and tests.
![csv assignment pytest coverage screenshot](assets/csv_assignment_pytest_screenshot.png "CSV Assignment Pytest Coverage Screenshot")