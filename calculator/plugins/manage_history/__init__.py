import os
import logging
import pandas as pd
from dotenv import load_dotenv

logger = logging.getLogger('calculator')

class CalculationHistory:
    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculationHistory, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        """Initializes the history file path and loads the history data."""
        load_dotenv()
        self.history_file = os.getenv('HISTORY_FILE_PATH', 'calculation_history.csv')
        self.history_file = os.path.abspath(self.history_file)
        self.history = self.load_history()

    def load_history(self):
        """Loads history from a CSV file or initializes an empty DataFrame if the file is missing."""
        if os.path.exists(self.history_file):
            try:
                logger.info(f"Loading history from {self.history_file}")
                return pd.read_csv(self.history_file)
            except Exception as e:
                logger.error(f"Failed to load history: {e}")
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
        except Exception as e:
            logger.error(f"Failed to save history: {e}")

    def clear_history(self):
        """Clears all records from history and saves an empty file."""
        self.history = pd.DataFrame(columns=['Operation', 'Input', 'Result'])
        self.save_history()
        logger.info("History cleared.")

    def delete_record(self, index):
        """Deletes a specific record from history based on index."""
        if self.history.empty or index < 0 or index >= len(self.history):
            logger.warning(f"Invalid index: {index}. Cannot delete record.")
            return False
        self.history = self.history.drop(index).reset_index(drop=True)
        self.save_history()
        logger.info(f"Record {index} deleted.")
        return True

    def add_record(self, operation, input_str, result):
        """Adds a new calculation record to history."""
        new_record = pd.DataFrame({'Operation': [operation], 'Input': [input_str], 'Result': [result]})
        self.history = pd.concat([self.history, new_record], ignore_index=True)
        self.save_history()
        logger.info(f"Record added: {operation} {input_str} = {result}")

    def print_history(self):
        """Prints the calculation history."""
        logger.info("Printing history:")
        print(self.history)
