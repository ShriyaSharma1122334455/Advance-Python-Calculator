"""
Commands related to calculation history management.
"""

from calculator.commands import Command

# Command to add a record
class AddRecordCommand(Command):
    """
    Command to add a calculation record to the history.
    """

    def __init__(self, calculation_history):
        """
        Initializes the AddRecordCommand with a CalculationHistory instance.
        
        Args:
            calculation_history (CalculationHistory): The history of calculations.
        """
        self.calculation_history = calculation_history

    def execute(self, *args):
        """
        Executes the command to add a record to the calculation history.
        
        Args:
            args (tuple): Expected to contain (operation, result).
        
        Returns:
            str: Confirmation message.
        """
        if len(args) != 2:
            return "Invalid arguments. Usage: AddRecordCommand(operation, result)."
        
        operation, result = args
        self.calculation_history.add_record(operation, result)
        return "Record added."

# Command to clear history
class ClearHistoryCommand(Command):
    """
    Command to clear the entire calculation history.
    """

    def __init__(self, calculation_history):
        """
        Initializes the ClearHistoryCommand with a CalculationHistory instance.
        
        Args:
            calculation_history (CalculationHistory): The history of calculations.
        """
        self.calculation_history = calculation_history

    def execute(self, *args):
        """
        Executes the command to clear the calculation history.
        
        Returns:
            str: Confirmation message.
        """
        self.calculation_history.clear_history()
        return "History cleared."

# Command to delete a specific history record
class DeleteHistoryCommand(Command):
    """
    Command to delete a specific calculation record from the history.
    """

    def __init__(self, calculation_history):
        """
        Initializes the DeleteHistoryCommand with a CalculationHistory instance.
        
        Args:
            calculation_history (CalculationHistory): The history of calculations.
        """
        self.calculation_history = calculation_history

    def execute(self, *args):
        """
        Executes the command to delete a specific history record by its index.
        
        Args:
            args (tuple): Expected to contain (index,).
        
        Returns:
            str: Confirmation message.
        """
        if len(args) != 1:
            return "Invalid arguments. Usage: DeleteHistoryCommand(index)."

        try:
            index = int(args[0])  # Ensure index is an integer
            success = self.calculation_history.delete_history(index)
            if success:
                return f"Record at index {index} deleted."
            return "Failed to delete record."
        except ValueError:
            return "Invalid index provided. Please use a valid integer."

# Command to load history
class LoadHistoryCommand(Command):
    """
    Command to load the calculation history.
    """

    def __init__(self, calculation_history):
        """
        Initializes the LoadHistoryCommand with a CalculationHistory instance.
        
        Args:
            calculation_history (CalculationHistory): The history of calculations.
        """
        self.calculation_history = calculation_history

    def execute(self, *args):
        """
        Executes the command to load the calculation history.
        
        Returns:
            str: Confirmation message.
        """
        success = self.calculation_history.load_history()
        if success:
            return "History loaded."
        return "No history to load."
