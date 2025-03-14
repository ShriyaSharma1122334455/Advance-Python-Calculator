"""
Module for the MenuCommand class.

This module provides the MenuCommand class, which dynamically displays 
all available commands registered in the command handler. It helps users 
view available commands and navigate the command-line interface.
"""

import logging
from calculator.commands import Command

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MenuCommand(Command):
    """
    MenuCommand class to display all available commands dynamically.

    This command class inherits from the Command class and implements the
    execute method to fetch and display all registered commands from the
    command handler.
    """

    def __init__(self, command_handler):
        """
        Initializes the MenuCommand with a reference to the command handler.

        This allows dynamic retrieval of the list of commands that have been
        registered in the command handler.

        Args:
            command_handler: The handler responsible for managing registered commands.
        """
        self.command_handler = command_handler
        logger.info("MenuCommand initialized with command handler: %s", command_handler)

    def execute(self):
        """
        Displays all available commands dynamically.

        This method retrieves the registered commands from the command handler
        and prints them in a sorted order. Also, displays a prompt to quit the application.
        """
        logger.info("Executing MenuCommand to display available commands.")
        
        print("\nAvailable Commands:\n" + "-" * 20)
        print("Type the operation along with 2 integers to perform on separated by space")
        
        # Log the available commands
        for command in sorted(self.command_handler.commands.keys()):
            logger.info("Available command: %s", command)
            print(f" - {command} ")
        
        print("\nType 'quit' to exit.\n")
        logger.info("MenuCommand execution completed.")
        
# Expose the MenuCommand class for external use
__all__ = ["MenuCommand"]
