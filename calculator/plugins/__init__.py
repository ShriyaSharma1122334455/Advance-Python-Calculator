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