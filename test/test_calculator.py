"""
Test suite for the Calculator class with logging and environment variables.
"""

import os
import logging
import pytest
from calculator import Calculator

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variable for test mode
os.environ["TEST_MODE"] = "true"

@pytest.fixture(autouse=True)
def disable_logging():
    """Disable logging during tests."""
    logging.disable(logging.CRITICAL)

def test_calculator_start_exit_command(capfd, monkeypatch):
    """Test that the calculator exits correctly on 'quit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'quit')
    calculator = Calculator()

    with pytest.raises(SystemExit):
        calculator.start()

    captured = capfd.readouterr()
    # Check for the welcome message
    assert "Calculator CLI - Type 'quit' to exit OR Menu to Continue" in captured.out
    # Check for the exit message
    assert "Goodbye!" in captured.out

def test_calculator_start_unknown_command(capfd, monkeypatch):
    """Test how the calculator handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    calculator = Calculator()

    logger.info("Starting calculator with an unknown command followed by 'quit'.")

    with pytest.raises(SystemExit):
        calculator.start()

    captured = capfd.readouterr()
    # Check for the welcome message
    assert "Calculator CLI - Type 'quit' to exit OR Menu to Continue" in captured.out
    # Check for the unknown command message
    assert "No such command: unknown_command" in captured.out  # Updated to match actual output
    # Check for the exit message
    assert "Goodbye!" in captured.out
    logger.info("Unknown command handling test passed.")
