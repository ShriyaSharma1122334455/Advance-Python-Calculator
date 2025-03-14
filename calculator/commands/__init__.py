"""
Module defining the Command pattern for managing operations.

This module provides an abstract base class Command for creating specific
commands and a CommandHandler class to register and execute those commands.
"""

from abc import ABC, abstractmethod
from app.calculation_history import CalculationHistory  # Assuming CalculationHistory is available

class Command(ABC):
    """
    Abstract base class for defining command execution.

    This class serves as a blueprint for creating concrete command classes 
    that will implement the `execute` method.
    """

    @abstractmethod
    def execute(self, *args):
        """
        Abstract method that should be implemented by subclasses to execute a specific command.
        """
        pass

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
        print(f"Command '{command_name}' registered.")  # Debugging feedback

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
            print(f"Command '{command_name}' executed with args {args}.")  # Debugging feedback
        except KeyError:
            print(f"No such command: {command_name}")
        except Exception as e:
            print(f"Error executing command '{command_name}': {e}")

# Command to add a record
class AddRecordCommand(Command):
    def __init__(self, calculation_history):
        self.calculation_history = calculation_history

    def execute(self, operation, result):
        self.calculation_history.add_record(operation, result)
        print("Record added.")

# Command to clear history
class ClearHistoryCommand(Command):
    def __init__(self, calculation_history):
        self.calculation_history = calculation_history

    def execute(self):
        self.calculation_history.clear_history()
        print("History cleared.")

# Command to delete a specific history record
class DeleteHistoryCommand(Command):
    def __init__(self, calculation_history):
        self.calculation_history = calculation_history

    def execute(self, index):
        try:
            index = int(index)  # Ensure index is an integer
            success = self.calculation_history.delete_history(index)
            if success:
                print(f"Record at index {index} deleted.")
            else:
                print("Failed to delete record.")
        except ValueError:
            print("Invalid index provided. Please use a valid integer.")

# Command to load history
class LoadHistoryCommand(Command):
    def __init__(self, calculation_history):
        self.calculation_history = calculation_history

    def execute(self):
        success = self.calculation_history.load_history()
        if success:
            print("History loaded.")
        else:
            print("No history to load.")

if __name__ == "__main__":
    calculation_history = CalculationHistory()
    command_handler = CommandHandler()

    # Register commands
    command_handler.register_command("clear", ClearHistoryCommand(calculation_history))
    command_handler.register_command("delete", DeleteHistoryCommand(calculation_history))
    command_handler.register_command("load", LoadHistoryCommand(calculation_history))

    # Example usage
    command_handler.execute_command("load")  # Load history
    command_handler.execute_command("clear")  # Clear history
    command_handler.execute_command("delete", "0")  # Delete the first record
