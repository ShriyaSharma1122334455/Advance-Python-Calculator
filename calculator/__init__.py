"""
Calculator module for managing the command-line interface (CLI) calculator.
Supports dynamically loading plugins that extend functionality.
"""

import os
import logging
import logging.config
import sys
from dotenv import load_dotenv
from calculator.commands import CommandHandler
from calculator.plugins.logging_utility import LoggingUtility

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

    def load_environment_variables(self):
        """
        Loads environment variables into a dictionary and logs the process.

        Returns:
            dict: A dictionary containing environment variables.
        """
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings
        
    def load_plugins(self):
        """
        Loads plugins from the plugins directory.
        Register commands from plugins with the command handler.
        """
        # Import plugins here, not at the module level
        try:
            from calculator.plugins.add import AddCommand
            from calculator.plugins.manage_history import CalculationHistory
            
            # Register commands from plugins
            calculation_history = CalculationHistory()
            self.command_handler.register_command("add", AddCommand(calculation_history))
            
            # Add more commands as needed
            
            logging.info("Plugins loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading plugins: {str(e)}")
            
    def start(self):
        """
        Starts the calculator CLI, prompting for user input and executing commands.
        Exits on 'quit' command with exit code 0.
        """
        logging.info("Application started")
        
        # Print the welcome message
        print("Calculator CLI - Type 'quit' to exit OR Menu to Continue")
        
        while True:
            user_input = input("> ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                sys.exit(0)
            
            # Split the input into command name and arguments
            parts = user_input.split()
            if not parts:
                continue
                
            command_name = parts[0].lower()
            args = parts[1:] if len(parts) > 1 else []
            
            # Check if the command exists and execute it
            if command_name in self.command_handler.commands:
                try:
                    result = self.command_handler.execute_command(command_name, args)
                    if result:
                        print(f"Result: {result}")
                except Exception as e:
                    logging.error(f"Error executing command {command_name}: {str(e)}")
                    print(f"Error: {str(e)}")
            else:
                print(f"No such command: {command_name}")
                logging.warning(f"Unknown command attempted: {command_name}")
