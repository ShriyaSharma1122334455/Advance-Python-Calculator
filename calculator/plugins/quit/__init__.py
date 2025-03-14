"""
Module for the QuitCommand class.

This module provides the QuitCommand class, which allows users to exit 
the program gracefully with a farewell message.
"""

import sys
import logging
from calculator.commands import Command

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QuitCommand(Command):
    """
    QuitCommand class to exit the program.

    This command class inherits from the Command class and implements the
    execute method to terminate the program with a farewell message.
    """

    def execute(self):
        """
        Executes the quit command.

        This method terminates the program and displays a farewell message.
        """
        logger.info("QuitCommand executed. Exiting the program.")
        sys.exit("Bye Bye")

# Expose the QuitCommand class for external use
__all__ = ["QuitCommand"]
