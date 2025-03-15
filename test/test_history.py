"""
Module for managing calculation history.

This module provides the CalculationHistory class for storing, retrieving, and
managing the history of calculator operations.
"""

import os
import logging
from dotenv import load_dotenv
import pandas as pd


class CalculationHistory:
    """
    Singleton class to manage calculation history.
    
    This class handles storing calculations, loading/saving from file,
    and managing the history of operations.
    """
    _instance = None

    def __new__(cls):
        """Implement singleton pattern to ensure only one history instance exists."""
        if cls._instance is None:
            instance = super(CalculationHistory, cls).__new__(cls)
            # Call __init__ explicitly to initialize attributes
            instance.__init__()
            cls._instance = instance
        return cls._instance

    def __init__(self):
        """Initialize instance attributes and load history."""
        # Only initialize if this hasn't been done before
        if not hasattr(self, 'history'):
            load_dotenv()
            self.history_file = os.getenv("HISTORY_FILE_PATH", "calculation_history.csv")
            self.history = pd.DataFrame(columns=['Operation', 'Input', 'Result'])
            self.load_history()

    def load_history(self):
        """
        Load history from file or initialize a new empty DataFrame.
        
        Returns:
            pandas.DataFrame: The loaded history DataFrame.
        """
        # Try to load from file if it exists
        if os.path.exists(self.history_file):
            try:
                self.history = pd.read_csv(self.history_file)
                return self.history
            except (IOError, pd.errors.EmptyDataError, pd.errors.ParserError) as e:
                # Handle the error gracefully - initialize empty DataFrame
                logging.error("Error loading history file: %s", str(e))
                return self.history
        return self.history

    def save_history(self):
        """Save the history DataFrame to file."""
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(os.path.abspath(self.history_file)), exist_ok=True)
            self.history.to_csv(self.history_file, index=False)
        except (IOError, PermissionError, OSError) as e:
            logging.error("Error saving history: %s", str(e))

    def add_record(self, operation, input_str, result):
        """
        Add a record to history.

        Args:
            operation (str): The operation performed
            input_str (str): The input expression
            result: The calculation result
        """
        new_record = pd.DataFrame({
            'Operation': [operation],
            'Input': [input_str],
            'Result': [result]
        })
        
        self.history = pd.concat([self.history, new_record], ignore_index=True)
        self.save_history()

    def delete_record(self, index):
        """
        Delete a record from history.

        Args:
            index (int): The index of the record to delete

        Returns:
            bool: True if successful, False otherwise
        """
        if 0 <= index < len(self.history):
            self.history = self.history.drop(index).reset_index(drop=True)
            self.save_history()
            return True
        return False

    def print_history(self):
        """Print the history to the console."""
        print(self.history.to_string(index=True))

    def get_all_history(self):
        """
        Get the complete history DataFrame.

        Returns:
            pandas.DataFrame: The complete history DataFrame
        """
        return self.history
