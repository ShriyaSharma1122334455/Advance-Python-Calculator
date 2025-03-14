"""
Module for the MultiplyCommand class.

This module provides the MultiplyCommand class, which performs the multiplication 
of two numerical arguments while handling invalid input errors.
"""

import logging
from decimal import Decimal, InvalidOperation
from calculator.commands import Command

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MultiplyCommand(Command):
    """
    MultiplyCommand class to perform multiplication of two numbers.

    This command class inherits from the Command class and implements the
    execute method to multiply two decimal numbers and display the result.
    """

    def execute(self, *args):
        """
        Executes the multiplication command.

        This method takes two arguments, attempts to convert them to decimals,
        and performs the multiplication. If the input is invalid, it handles the
        error and displays an appropriate message.

        Args:
            *args: Two numerical arguments to be multiplied.

        Prints:
            The product of the two numbers if valid inputs are provided.
            Error message if invalid inputs are encountered.
        """
        logger.info("Executing MultiplyCommand with arguments: %s", args)
        
        try:
            a, b = map(Decimal, args)
            product = a * b
            print(f"The solution of multiplication is {product}")
            logger.info("Multiplication successful: %s * %s = %s", a, b, product)
        except InvalidOperation:
            print("Error: Invalid input. Please enter valid numbers.")
            logger.error("Error: Invalid input. Unable to convert arguments to Decimal: %s", args)

# Expose the MultiplyCommand class for external use
__all__ = ["MultiplyCommand"]
