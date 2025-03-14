"""
Module defining the Command pattern for managing operations.

This module provides an abstract base class Command for creating specific
commands and a CommandHandler class to register and execute those commands.
"""

from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract base class for defining command execution.

    This class serves as a blueprint for creating concrete command classes 
    that will implement the `execute` method.
    """

    @abstractmethod
    def execute(self):
        """
        Abstract method that should be implemented by subclasses to execute a specific command.
        """

class CommandHandler:
    """
    CommandHandler class to manage and execute commands.

    This class allows you to register and execute commands by name. It uses a dictionary
    to store registered commands, and executes the corresponding command when requested.
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

    def execute_command(self, command_name: str, *args):
        """
        Executes the command registered under the given command name.

        Args:
            command_name (str): The name of the command to execute.
            *args: Any additional arguments to be passed to the command's execute method.

        Raises:
            KeyError: If the given command name is not found.
        
        This method uses the "Easier to ask for forgiveness than permission (EAFP)" approach:
        it tries to execute the command and handles the exception if the command is not found.
        """
        try:
            self.commands[command_name].execute(*args)
        except KeyError:
            print(f"No such command: {command_name}")
