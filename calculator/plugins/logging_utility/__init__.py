# calculator/logging_utility.py
import os
import logging
from logging.handlers import RotatingFileHandler

class LoggingUtility:
    @staticmethod
    def initialize_logging():
        """Initializes the application-wide logging configuration."""
        # Only initialize logging if it's not in TEST_MODE
        if os.getenv("TEST_MODE") != "true":
            log_directory = "logs"
            log_filename = "application.log"
            max_log_size = 10 * 1024 * 1024  # 10 MB
            backup_count = 3  # Keep at most 3 log files

            os.makedirs(log_directory, exist_ok=True)
            log_file_path = os.path.join(log_directory, log_filename)

            # Create a rotating file handler
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
        logging.info(message)

    @staticmethod
    def warning(message):
        logging.warning(message)

    @staticmethod
    def error(message):
        logging.error(message)

    @staticmethod
    def debug(message):
        logging.debug(message)

    @staticmethod
    def critical(message):
        logging.critical(message)
        