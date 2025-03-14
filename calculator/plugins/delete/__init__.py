from app.plugins.logging_utility import LoggingUtility
from app.plugins.history_manager import CalculationHistory
from app.commands import Command

class DeleteCommand(Command):
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
        except Exception as e:
            print(f"Error: An unexpected error occurred - {str(e)}")
            LoggingUtility.error(f"An unexpected error occurred - {str(e)}")

# This allows the command to be imported directly from its package
__all__ = ['DeleteCommand']
