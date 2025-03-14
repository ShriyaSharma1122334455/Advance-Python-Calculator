from calculator.plugins.logging_utility import LoggingUtility
from calculator.plugins.manage_history import CalculationHistory
from calculator.commands import Command

class ClearCommand(Command):
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
        except Exception as e:
            print(f"Error: An unexpected error occurred - {str(e)}")
            LoggingUtility.error(f"An unexpected error occurred - {str(e)}")

# This allows the command to be imported directly from its package
__all__ = ['ClearCommand']
