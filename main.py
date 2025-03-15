"""
Module for running the Calculator CLI.

This module initializes and runs the Calculator CLI, allowing the user to 
interact with the command-line calculator.
"""

from calculator import Calculator

if __name__ == "__main__":
    # Initialize and start the calculator
    calculator = Calculator()
    calculator.start()
