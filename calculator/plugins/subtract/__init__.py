"""
Plugin that provides subtraction functionality to the calculator.
"""

from calculator.base import Command
from calculator.plugins.logging_utility import LoggingUtility

class SubtractCommand(Command):
    """Command that performs subtraction of numbers."""
    
    def __init__(self, history_manager=None):
        """Initialize with optional history manager."""
        self.history_manager = history_manager
    
    def execute(self, *args):  # Use *args to accept variadic arguments, matching the base class
        """Execute the subtract command with the given arguments."""
        try:
            numbers = [float(arg) for arg in args]
            if len(numbers) < 2:
                message = "Error: Subtraction requires at least two numbers"
                print(message)
                LoggingUtility.error("Subtract command failed: not enough arguments")
                return message
                
            result = numbers[0]
            for number in numbers[1:]:
                result -= number
            print(f"Result: {result}")
            
            # Record in history if available
            if self.history_manager:
                expression = f"{numbers[0]} - {' - '.join(str(n) for n in numbers[1:])} = {result}"
                self.history_manager.add_record(expression, result)
                
            return result
        except ValueError:
            message = "Error: All arguments must be numbers"
            print(message)
            LoggingUtility.error("Subtract command failed: arguments must be numbers")
            return message

# Export a function called "subtract" that plugins/__init__.py is trying to import
def subtract(num1, num2):
    """Simple subtract function that subtracts num2 from num1."""
    return num1 - num2
