
"""
Plugin that provides multiplication functionality to the calculator.
"""

from calculator.base import Command
from calculator.plugins.logging_utility import LoggingUtility

class MultiplyCommand(Command):
    """Command that performs multiplication of numbers."""
    
    def __init__(self, history_manager=None):
        """Initialize with optional history manager."""
        self.history_manager = history_manager
    
    def execute(self, args):
        """Execute the multiply command with the given arguments."""
        try:
            numbers = [float(arg) for arg in args]
            if not numbers:
                message = "Error: No numbers provided for multiplication"
                print(message)
                LoggingUtility.error("Multiply command failed: no arguments")
                return message
                
            result = 1
            for number in numbers:
                result *= number
            print(f"Result: {result}")
            
            # Record in history if available
            if self.history_manager:
                expression = f"{' * '.join(str(n) for n in numbers)} = {result}"
                self.history_manager.add_record(expression, result)
                
            return result
        except ValueError:
            message = "Error: All arguments must be numbers"
            print(message)
            LoggingUtility.error("Multiply command failed: arguments must be numbers")
            return message

# Export a function called "multiply" that plugins/__init__.py is trying to import
def multiply(a, b):
    """Simple multiply function that multiplies two numbers."""
    return a * b