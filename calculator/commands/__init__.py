"""
This module defines commands for the calculator, including managing calculation history.
Each command inherits from the Command abstract base class and implements the execute method.
"""

from calculator.base import Command
from calculator.plugins.logging_utility import LoggingUtility

class CommandHandler:
    """
    CommandHandler class to manage and execute commands.
    """

    def __init__(self):
        """
        Initializes the CommandHandler with an empty dictionary to store commands.
        """
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """
        Registers a command with the given name.

        Args:
            command_name (str): The name of the command to register.
            command (Command): The command object to be registered.
        """
        self.commands[command_name] = command
        LoggingUtility.info(f"Command '{command_name}' registered.")

    def execute_command(self, command_name: str, *args):
        """
        Executes the command registered under the given command name.

        Args:
            command_name (str): The name of the command to execute.
            *args: Any additional arguments to be passed to the command's execute method.
        """
        if command_name in self.commands:
            try:
                result = self.commands[command_name].execute(*args)
                LoggingUtility.info(f"Command '{command_name}' executed with args {args}.")
                return result
            except Exception as e:
                LoggingUtility.error(f"Error executing command '{command_name}': {e}")
                return f"Error: {e}"
        else:
            LoggingUtility.warning(f"No such command: {command_name}")
            return "Unknown command. Type 'menu' for a list of commands."