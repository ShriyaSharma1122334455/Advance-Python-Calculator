"""
Module for the DivideCommand class.

This module provides the DivideCommand class, which performs the division 
of two numerical arguments while handling errors such as invalid input and 
division by zero.
"""

import logging
from decimal import Decimal, InvalidOperation, DivisionByZero
from calculator.commands import Command

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DivideCommand(Command):
    """
    DivideCommand class to perform the division of two numerical arguments.

    This command class inherits from the Command class and implements the
    execute method to perform division of two numbers passed as arguments.
    """

    def execute(self, *args):
        """
        Executes the division command with the given arguments.

        Args:
            *args: Two numerical arguments to be divided.

        Raises:
            InvalidOperation: If the arguments cannot be converted to Decimal.
            DivisionByZero: If division by zero is attempted.
        """
        logger.info("Executing division command with arguments: %s", args)

        try:
            # Convert arguments to Decimal and perform division
            a, b = map(Decimal, args)
            if b == 0:
                logger.error("Division by zero attempted with arguments: %s", args)
                print("Error: Division by zero is not allowed.")
                return
            quotient = a / b
            logger.info("Division result: %s / %s = %s", a, b, quotient)
            print(f"The solution of division is {quotient}")
        except InvalidOperation:
            logger.error("Invalid input: Unable to convert arguments to Decimal. Arguments: %s", args)
            print("Error: Invalid input. Please enter valid numbers.")
        except DivisionByZero:
            logger.error("Attempted division by zero with arguments: %s", args)
            print("Error: Cannot divide by zero.")

# Expose the DivideCommand class for external use
__all__ = ["DivideCommand"]
