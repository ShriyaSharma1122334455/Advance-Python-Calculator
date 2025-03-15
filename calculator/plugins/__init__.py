"""
Plugin Manager and REPL for the Calculator application.

This module allows the management of plugins and provides a REPL (Read-Eval-Print Loop)
for the calculator, where users can input commands to perform various operations.
"""

from calculator.plugins.add import AddCommand  # Import only what's needed
from calculator.plugins.subtract import subtract
from calculator.plugins.multiply import multiply
from calculator.plugins.divide import divide
from .plugin_manager import PluginManager  # Local import should be after first-party imports

class CalculatorREPL:
    """
    CalculatorREPL class to handle the interactive calculator shell.

    This class is responsible for running a REPL where users can input commands
    to interact with the calculator, including using plugins and managing history.
    """

    def __init__(self):
        """Initializes the CalculatorREPL with a plugin manager and an empty history."""
        self.plugin_manager = PluginManager()
        self.history = None  # Will be set later if needed

    def load_plugins(self):
        """
        Loads essential plugins for the calculator.

        This method loads the basic arithmetic plugins such as add, subtract, multiply, and divide
        into the plugin manager.
        """
        self.plugin_manager.load_plugin("calculator.plugins.add")
        self.plugin_manager.load_plugin("calculator.plugins.subtract")
        self.plugin_manager.load_plugin("calculator.plugins.multiply")
        self.plugin_manager.load_plugin("calculator.plugins.divide")

    def evaluate_input(self, user_input):
        """
        Evaluates the user input and checks for plugin commands.

        If the input corresponds to a loaded plugin, it will execute that plugin and store the result in history.
        """
        plugin_name, *args = user_input.split()
        if plugin_name in self.plugin_manager.plugins:
            result = self.plugin_manager.plugins[plugin_name](*args)
            self.history.add_record(plugin_name, user_input, result)  # Assuming history is managed elsewhere
        else:
            print("Unknown command")

    def run(self):
        """Runs the REPL, accepting user input and executing commands."""
        while True:
            user_input = input(">>> ")
            if user_input == "quit":
                break
            if user_input == "history":
                self.history.print_history()
            elif user_input == "clear history":
                self.history.clear_history()
            elif user_input == "delete record":
                index = int(input("Enter record index to delete: "))
                self.history.delete_record(index)
            else:
                self.evaluate_input(user_input)

# Function to initialize and run the calculator REPL with loaded plugins
def repl():
    """
    Initializes the CalculatorREPL, loads plugins, and starts the REPL loop.
    """
    calculator_repl = CalculatorREPL()
    calculator_repl.load_plugins()  # Load the necessary plugins
    calculator_repl.run()
