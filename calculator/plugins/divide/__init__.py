"""
Plugin that provides division functionality to the calculator.
"""

from calculator.base import Command
from calculator.plugins.logging_utility import LoggingUtility

class DivideCommand(Command):
    """Command that performs division of numbers."""
    
    def __init__(self, history_manager=None):
        """Initialize with optional history manager."""
        self.history_manager = history_manager
    
    def execute(self, args):
        """Execute the divide command with the given arguments."""
        try:
            numbers = [float(arg) for arg in args]
            if len(numbers) < 2:
                message = "Error: Division requires at least two numbers"
                print(message)
                LoggingUtility.error("Divide command failed: not enough arguments")
                return message
                
            result = numbers[0]
            for number in numbers[1:]:
                if number == 0:
                    message = "Error: Division by zero"
                    print(message)
                    LoggingUtility.error("Divide command failed: division by zero")
                    return message
                result /= number
            print(f"Result: {result}")
            
            # Record in history if available
            if self.history_manager:
                expression = f"{numbers[0]} / {' / '.join(str(n) for n in numbers[1:])} = {result}"
                self.history_manager.add_record(expression, result)
                
            return result
        except ValueError:
            message = "Error: All arguments must be numbers"
            print(message)
            LoggingUtility.error("Divide command failed: arguments must be numbers")
            return message

# Export a function called "divide" that plugins/__init__.py is trying to import
def divide(a, b):
    """Simple divide function that divides a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b