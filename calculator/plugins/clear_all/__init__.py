"""
ClearCommand module.

This module provides the ClearCommand class, which allows users to clear
the calculation history. It uses the CalculationHistory class to manage the 
history records and ensures the process is logged and any errors are handled.
"""

from calculator.plugins.logging_utility import LoggingUtility
from calculator.plugins.manage_history import CalculationHistory
from calculator.commands import Command

class ClearCommand(Command):
    """
    ClearCommand class to clear the calculation history.

    This class inherits from the Command class and implements the execute method
    to clear all history records. The command ensures that no arguments are passed
    and logs relevant information during the process.
    """

    def execute(self, *args):
        """Executes the command to clear calculation history."""
        if len(args) > 0:
            print("Error: The clear command does not require any arguments.")
            LoggingUtility.warning("The clear command does not require any arguments.")
            return

        # Obtain the singleton instance of CalculationHistory
        history_manager = CalculationHistory()

        try:
            history_manager.clear_history()
            print("History cleared successfully.")
            LoggingUtility.info("History cleared successfully.")
        except KeyError as e:
            print(f"Error: {str(e)}")
            LoggingUtility.error(f"KeyError while clearing history - {str(e)}")
        except ValueError as e:
            print(f"Error: {str(e)}")
            LoggingUtility.error(f"ValueError while clearing history - {str(e)}")
        
# This allows the command to be imported directly from its package
__all__ = ['ClearCommand']
