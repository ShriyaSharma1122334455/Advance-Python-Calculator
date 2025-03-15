"""
This module provides logging utilities for the application.

The `LoggingUtility` class initializes and configures the logging system, allowing 
for logging messages at different levels (INFO, WARNING, ERROR, DEBUG, CRITICAL).
It also handles logging to both a rotating log file and the console, with 
different log levels for each.
"""

import os
import logging
from logging.handlers import RotatingFileHandler

class LoggingUtility:
    """
    A utility class for managing logging within the application.

    This class sets up and manages the logging system, including configuration
    of a rotating log file and console logging. It provides static methods for 
    logging messages at different levels: info, warning, error, debug, and critical.
    """

    @staticmethod
    def initialize_logging():
        """
        Initializes the application-wide logging configuration.

        This method sets up a rotating file handler for logging to a file with a 
        maximum size and a specified number of backups. It also configures a 
        console handler to display warning and higher-level messages in the terminal.

        Logs are stored in the "logs" directory with the filename "application.log".
        Logging will only be initialized if the `TEST_MODE` environment variable 
        is not set to "true".
        """
        if os.getenv("TEST_MODE") != "true":
            log_directory = "logs"
            log_filename = "application.log"
            max_log_size = 10 * 1024 * 1024  # 10 MB
            backup_count = 3  # Keep at most 3 log files

            os.makedirs(log_directory, exist_ok=True)
            log_file_path = os.path.join(log_directory, log_filename)

            rotating_file_handler = RotatingFileHandler(
                log_file_path, maxBytes=max_log_size, backupCount=backup_count
            )
            rotating_file_handler.setLevel(logging.DEBUG)

            log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            rotating_file_handler.setFormatter(log_format)

            logging.basicConfig(level=logging.DEBUG, handlers=[rotating_file_handler])

            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.WARNING)  # Show only warnings in CLI
            console_handler.setFormatter(log_format)

            logger = logging.getLogger()
            logger.addHandler(console_handler)

            logging.info("Logging system initialized.")

    @staticmethod
    def info(message):
        """Logs an informational message."""
        logging.info(message)

    @staticmethod
    def warning(message):
        """Logs a warning message."""
        logging.warning(message)

    @staticmethod
    def error(message):
        """Logs an error message."""
        logging.error(message)

    @staticmethod
    def debug(message):
        """Logs a debug message."""
        logging.debug(message)

    @staticmethod
    def critical(message):
        """Logs a critical message."""
        logging.critical(message)
