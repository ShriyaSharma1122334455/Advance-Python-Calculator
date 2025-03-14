# calculator/plugins/__init__.py
from .plugin_manager import PluginManager

class CalculatorREPL:
    def __init__(self):
        self.plugin_manager = PluginManager()

    def run(self):
        while True:
            user_input = input(">>> ")
            if user_input == "quit":
                break
            self.evaluate_input(user_input)

    def evaluate_input(self, user_input):
        # ... (rest of the method remains the same)

        # check if input is a plugin command
        plugin_name, *args = user_input.split()
        if plugin_name in self.plugin_manager.plugins:
            self.plugin_manager.plugins[plugin_name](*args)
        else:
            print("Unknown command")
    # calculator/plugins/__init__.py
    def load_plugins():
        plugin_manager = PluginManager()
        plugin_manager.load_plugin("calculator.plugins.add")
        plugin_manager.load_plugin("calculator.plugins.subtract")
        plugin_manager.load_plugin("calculator.plugins.multiply")
        plugin_manager.load_plugin("calculator.plugins.divide")
        return plugin_manager

# calculator/plugins/__init__.py
def repl():
    calculator_repl = CalculatorREPL()
    calculator_repl.plugin_manager = load_plugins()
    calculator_repl.run()

class CalculatorREPL:
    def __init__(self):
        self.plugins = {}  # dictionary to store loaded plugins
        self.history = None  # calculation history object

    def evaluate_input(self, user_input):
        # ... (rest of the method remains the same)

        # check if input is a plugin command
        plugin_name, *args = user_input.split()
        if plugin_name in self.plugins:
            result = self.plugins[plugin_name](*args)
            self.history.add_record(plugin_name, user_input, result)
        else:
            print("Unknown command")

    def run(self):
        while True:
            user_input = input(">>> ")
            if user_input == "quit":
                break
            elif user_input == "history":
                self.history.print_history()
            elif user_input == "clear history":
                self.history.clear_history()
            elif user_input == "delete record":
                index = int(input("Enter record index to delete: "))
                self.history.delete_record(index)
            else:
                self.evaluate_input(user_input)