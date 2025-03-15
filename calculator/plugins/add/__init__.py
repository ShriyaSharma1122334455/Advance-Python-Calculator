"""
Plugin that provides addition functionality to the calculator.
"""

from calculator.base import Command
from calculator.plugins.logging_utility import LoggingUtility

class AddCommand(Command):
    """Command that performs addition of numbers."""
    
    def __init__(self, history_manager=None):
        """Initialize with optional history manager."""
        self.history_manager = history_manager
    
    def execute(self, *args):
        """Execute the add command with the given arguments."""
        try:
            numbers = [float(arg) for arg in args]
            result = sum(numbers)
            print(f"Result: {result}")
            
            # Record in history if available
            if self.history_manager:
                expression = f"{' + '.join(str(n) for n in numbers)} = {result}"
                self.history_manager.add_record(expression, result)
                
            return result
        except ValueError:
            message = "Error: All arguments must be numbers"
            print(message)
            LoggingUtility.error("Add command failed: arguments must be numbers")
            return message

# Export a function called "add" that your plugins/__init__.py is trying to import
def add(num1, num2):
    """Simple add function that adds two numbers."""
    return num1 + num2
