"""
Module for the QuitCommand class.

This module provides the QuitCommand class, which allows users to exit 
the program gracefully with a farewell message.
"""

import sys
import logging
import os
from calculator.commands import Command

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Suppress logging in test mode
if os.getenv("TEST_MODE") == "true":
    logging.disable(logging.CRITICAL)

class QuitCommand(Command):
    """
    QuitCommand class to exit the program.

    This command class inherits from the Command class and implements the
    execute method to terminate the program with a farewell message.
    """

    def execute(self, *args):
        """
        Executes the quit command.

        This method terminates the program and displays a farewell message.
        """
        logger.info("QuitCommand executed. Exiting the program.")
        print("Goodbye!")  # Ensure expected output for tests
        sys.exit(0)  # Ensure exit code is 0

# Expose the QuitCommand class for external use
__all__ = ["QuitCommand"]
