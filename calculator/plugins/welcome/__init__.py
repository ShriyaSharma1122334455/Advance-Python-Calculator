"""
Module for the WelcomeCommand class.

This module provides the WelcomeCommand class, which displays a welcome 
message when executed.
"""

import logging
from calculator.commands import Command

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WelcomeCommand(Command):
    """
    WelcomeCommand class for printing a welcome message.

    This class inherits from the Command class and implements the execute method
    to display a welcome message when executed.
    """

    def execute(self):
        """
        Executes the welcome command.

        This method prints a welcome message to the user.
        """
        print("Hello, Welcome to Calculator")
        logger.info("Welcome message displayed to the user.")

# Expose the WelcomeCommand class for external use
__all__ = ["WelcomeCommand"]
