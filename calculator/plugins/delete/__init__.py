"""
DeleteCommand module.

This module provides the DeleteCommand class, which is responsible for
executing the delete operation on the history records. It uses the 
CalculationHistory class to manage the history records.
"""

from calculator.plugins.logging_utility import LoggingUtility
from calculator.plugins.manage_history import CalculationHistory
from calculator.commands import Command

class DeleteCommand(Command):
    """
    DeleteCommand class to delete a specific history record.

    This class inherits from the Command class and implements the execute method
    to delete a history record based on a provided index. The command ensures
    that the correct index is provided and logs relevant information during the
    process.
    """

    def execute(self, *args):
        """Executes the command to delete a specific history record."""
        if len(args) != 1:
            print("Error: The delete command requires exactly one argument (index).")
            LoggingUtility.warning("The delete command requires exactly one argument (index).")
            return

        try:
            index = int(args[0])  # Convert input to integer
        except ValueError:
            print("Error: Index must be a valid integer.")
            LoggingUtility.error("Invalid index provided for deletion.")
            return

        # Obtain the singleton instance of CalculationHistory
        history_manager = CalculationHistory()

        try:
            if history_manager.delete_record(index):
                print(f"Record at index {index} deleted successfully.")
                LoggingUtility.info(f"Record at index {index} deleted successfully.")
            else:
                print(f"Error: No record found at index {index}.")
                LoggingUtility.warning(f"Attempted to delete non-existent record at index {index}.")
        except KeyError as e:
            print(f"Error: {str(e)}")
            LoggingUtility.error(f"KeyError while deleting record - {str(e)}")
        except ValueError as e:
            print(f"Error: {str(e)}")
            LoggingUtility.error(f"ValueError while deleting record - {str(e)}")
        
# This allows the command to be imported directly from its package
__all__ = ['DeleteCommand']
