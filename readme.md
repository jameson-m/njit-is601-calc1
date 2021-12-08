# Calculator Project Setup
[![Build Status](https://app.travis-ci.com/jameson-m/njit-is601-calc1.svg?branch=main)](https://app.travis-ci.com/jameson-m/njit-is601-calc1)

Run Pip Install
pip install -r requirements.txt

To run tests, Lint, and Coverage report use this command:

pytest  --pylint --cov

.pylintrc is the config for pylint
.coveragerc is the config for coverage
setup.py is a config file for pytest

## Flash Messages and Validation Assignment
Below are three screenshots showing:
1. Calculator app's form on initial load.
2. Calculator app's error flash messages.
3. Calculator app's success flash messages.

![form initial load](assets/flash_messages_assignment/calculator-page.png "Calculator Page")
![error flash messages](assets/flash_messages_assignment/calculator-page-error.png "Error Flash Messages")
![success flash messages](assets/flash_messages_assignment/calculator-page-success.png "Success Flash Messages")