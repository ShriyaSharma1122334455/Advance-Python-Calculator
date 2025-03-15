"""
This module defines the CalculationHistory class, which is a singleton class
for managing the calculation history in the calculator application."""
import os
import logging
import pandas as pd
from dotenv import load_dotenv

# Initialize logger for the module
logger = logging.getLogger('calculator')

class CalculationHistory:
    """
    Singleton class to manage the calculation history.

    This class maintains a log of all operations, inputs, and results.
    It ensures that there is only one instance of the history, and it provides 
    methods to load, add, delete, and clear records in the calculation history.
    It also handles saving the history to a CSV file and loading from it.
    """

    _instance = None  # Singleton instance

    def __new__(cls):
        """Ensures only one instance of the CalculationHistory class exists."""
        if cls._instance is None:
            cls._instance = super(CalculationHistory, cls).__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        """Initializes the history file path and loads the history data."""
        # Check if already initialized
        if hasattr(self, 'history'):
            return
            
        load_dotenv()
        self.history_file = os.getenv('HISTORY_FILE_PATH', 'calculation_history.csv')
        self.history_file = os.path.abspath(self.history_file)
        self.history = self.load_history()

    def load_history(self):
        """
        Loads history from a CSV file or initializes an empty DataFrame if the file is missing.

        Returns:
            pd.DataFrame: The calculation history, or an empty DataFrame if no history file exists.
        """
        if os.path.exists(self.history_file):
            try:
                logger.info("Loading history from %s", self.history_file)
                return pd.read_csv(self.history_file)
            except (FileNotFoundError, pd.errors.EmptyDataError) as e:
                logger.error("Failed to load history: %s", e)
                return pd.DataFrame(columns=['Operation', 'Input', 'Result'])
        else:
            logger.info("No existing history found. Initializing empty history.")
            return pd.DataFrame(columns=['Operation', 'Input', 'Result'])

    def save_history(self):
        """Saves the current history to a CSV file."""
        try:
            os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
            self.history.to_csv(self.history_file, index=False)
            logger.info("History saved successfully.")
        except PermissionError as e:
            logger.error("Failed to save history due to permission error: %s", e)
        except pd.errors.EmptyDataError as e:
            logger.error("Failed to save history due to empty data error: %s", e)
        except IOError as e:
            logger.error("Failed to save history due to I/O error: %s", e)

    def clear_history(self):
        """Clears all records from history and saves an empty file."""
        self.history = pd.DataFrame(columns=['Operation', 'Input', 'Result'])
        self.save_history()
        logger.info("History cleared.")

    def delete_record(self, index):
        """
        Deletes a specific record from history based on index.

        Args:
            index (int): The index of the record to delete.

        Returns:
            bool: True if the record was successfully deleted, False if the index was invalid.
        """
        if self.history.empty or index < 0 or index >= len(self.history):
            logger.warning("Invalid index: %d. Cannot delete record.", index)
            return False
        logger.info("Deleting record at index %d: %s", index, self.history.iloc[index])
        self.history = self.history.drop(index).reset_index(drop=True)
        self.save_history()
        logger.info("Record %d deleted. Updated history length: %d", index, len(self.history))
        return True

    def add_record(self, operation, input_str, result):
        """
        Adds a new calculation record to history.

        Args:
            operation (str): The operation performed (e.g., "subtraction").
            input_str (str): The input string representing the calculation.
            result (float): The result of the operation.
        """
        logger.info("Adding record: %s %s = %s", operation, input_str, result)
        new_record = pd.DataFrame({'Operation': [operation], 'Input': [input_str], 'Result': [result]})
        self.history = pd.concat([self.history, new_record], ignore_index=True)
        self.save_history()
        logger.info("Record added. Updated history length: %d", len(self.history))
    
    def print_history(self):
        """Prints the calculation history."""
        logger.info("Printing history:")
        print(self.history)
