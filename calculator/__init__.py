"""
Calculator module for managing the command-line interface (CLI) calculator.
Supports dynamically loading plugins that extend functionality.
"""

import os
import pkgutil
import importlib
import logging
import logging.config
from dotenv import load_dotenv
from calculator.commands import CommandHandler, Command
from calculator.plugins.logging_utility import LoggingUtility  # Assuming a logging utility module exists

# Initialize logging at the start of your application
LoggingUtility.initialize_logging()

class Calculator:
    """
    Calculator class for managing the command-line interface (CLI) calculator.
    Supports dynamically loading plugins that extend functionality.

    Attributes:
        command_handler (CommandHandler): Manages and executes commands in the calculator CLI.
        settings (dict): Stores environment variables.
    """

    def __init__(self):
        """
        Initializes the Calculator with a CommandHandler instance.
        Loads environment variables and configures logging.
        """
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'TESTING')
        self.command_handler = CommandHandler()
        self.load_plugins()

    def configure_logging(self):
        """
        Configures logging settings, creating a 'logs' directory if it doesn't exist.
        Loads logging configuration from 'logging.conf' or sets basic logging configuration.
        """
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")
        logging.error("Errors need to be checked")
        logging.debug("Need to fix")
        logging.warning("Run tests again")
        logging.critical("Prioritize these tests")

    def load_environment_variables(self):
        """
        Loads environment variables into a dictionary and logs the process.

        Returns:
            dict: A dictionary containing environment variables.
        """
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        """
        Retrieves the specified environment variable.

        Args:
            env_var (str): The name of the environment variable to fetch.

        Returns:
            str or None: The value of the environment variable, or None if not found.
        """
        return self.settings.get(env_var, None)

    def load_plugins(self):
        """
        Dynamically loads all plugins from the `calculator.plugins` package and registers commands.
        Logs each plugin load and command registration.
        """
        plugins_package = 'calculator.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    logging.info(f"Loaded plugin module: {plugin_name}")
                except ImportError as e:
                    logging.error(f"Error loading plugin {plugin_name}: {e}")
                    continue

                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    if isinstance(item, type) and issubclass(item, Command):
                        try:
                            # Check if special initialization is required
                            if hasattr(item, 'requires_command_handler') and item.requires_command_handler:
                                instance = item(self.command_handler)
                            else:
                                instance = item()

                            # Register the command
                            command_name = getattr(instance, 'command_name', plugin_name)
                            self.command_handler.register_command(command_name, instance)
                            logging.info(f"Registered command: {command_name}")
                        except TypeError:
                            continue  # Skip if it's not a valid command class

    def start(self):
        """
        Starts the CLI loop for the calculator, accepting user commands until 'exit' is entered.
        Handles invalid inputs and logs errors.
        """
        logging.info("Calculator CLI started. Type 'exit' to exit.")
        print("Menu command provides a list of commands. Type command then number space number to execute command.")
        print("Type 'exit' to exit.")

        while True:
            try:
                user_input = input(">>> ").strip()
                if user_input.lower() == "exit":
                    logging.info("Exiting calculator.")
                    print("Goodbye!")
                    break

                parts = user_input.split(maxsplit=1)
                command_name = parts[0] if parts else ''
                args = parts[1].split() if len(parts) > 1 else []

                if command_name:
                    self.command_handler.execute_command(command_name, *args)
                else:
                    logging.warning("Invalid command entered.")
                    print("Please enter a valid command.")

            except KeyboardInterrupt:
                logging.info("Calculator interrupted by user.")
                print("\nExiting calculator. Goodbye!")
                break
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                print("An unexpected error occurred. Check logs for details.")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.start()
