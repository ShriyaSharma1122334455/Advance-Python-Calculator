"""
Module for the AddCommand class that performs addition of two numerical arguments.

This module defines the AddCommand class, which is used to add two numerical
values provided as arguments. The command inherits from the base Command class 
and implements the execute method to carry out the addition. It includes error 
handling for invalid input and ensures exactly two arguments are provided.
"""

import logging
from decimal import Decimal, InvalidOperation
from calculator.commands import Command

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AddCommand(Command):
    """
    AddCommand class to perform the addition of two numerical arguments.

    This command class inherits from the Command class and implements the
    execute method to perform addition of two numbers passed as arguments.
    """

    def execute(self, *args):
        """
        Executes the addition command with the given arguments.

        Args:
            *args: Two numerical arguments to be added.

        Raises:
            ValueError: If the number of arguments is not exactly two.
            InvalidOperation: If the arguments cannot be converted to Decimal.
        """
        logger.info("Executing addition command with arguments: %s", args)

        if not self.validate_args(args):
            return

        try:
            # Convert arguments to Decimal and perform addition
            a, b = map(Decimal, args)
            result = a + b
            logger.info("Addition result: %s + %s = %s", a, b, result)
            print(f"The Solution of addition is {result}")
        except InvalidOperation:
            logger.error("Invalid input: Unable to convert arguments to Decimal.")
            print("Error: Invalid input")

    def validate_args(self, args):
        """
        Validates the arguments for the addition operation.

        Args:
            args: A tuple of arguments to be validated.

        Returns:
            bool: True if the arguments are valid (exactly two numbers), 
                  False otherwise.
        """
        if len(args) != 2:
            logger.warning("Error: Addition requires exactly two numerical arguments, received %d", len(args))
            print("Error: Addition requires exactly two numerical arguments")
            return False
        logger.info("Arguments validated successfully: %s", args)
        return True

# Expose the AddCommand class for external use
__all__ = ["AddCommand"]
