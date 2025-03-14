"""
Test suite for the Calculator class with logging and environment variables.
"""

import os
import logging
from calculator import Calculator


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variable for test mode
os.environ["TEST_MODE"] = "true"

def test_calculator_start_exit_command(capfd, monkeypatch):
    """Test that the calculator exits correctly on 'quit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'quit')
    calculator = Calculator()
    
    logger.info("Starting calculator with 'quit' command")
    calculator.start()
    
    # Capture the output and check that 'Goodbye!' is printed
    captured = capfd.readouterr()
    assert "Calculator CLI - Type 'quit' to exit OR Menu to Continue" in captured.out
    assert "Goodbye!" in captured.out  # Adjusted to match actual output
    logger.info("Exit command test passed.")

def test_calculator_start_unknown_command(capfd, monkeypatch):
    """Test how the calculator handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    calculator = Calculator()
    
    logger.info("Starting calculator with an unknown command followed by 'quit'.")
    calculator.start()
    
    # Capture the output and check that 'Goodbye!' is printed, and 'No such command' is handled
    captured = capfd.readouterr()
    assert "Calculator CLI - Type 'quit' to exit OR Menu to Continue" in captured.out
    assert "No such command: unknown_command" in captured.out  # Check the unknown command message
    assert "Goodbye!" in captured.out  # Adjusted to match actual output
    logger.info("Unknown command handling test passed.")
    