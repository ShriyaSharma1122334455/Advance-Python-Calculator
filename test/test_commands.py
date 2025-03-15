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

def test_calculator_start_exit_command(monkeypatch):
    """Test that the calculator exits correctly on 'quit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'quit')
    calculator = Calculator()

    with pytest.raises(SystemExit):
        calculator.start()

def test_calculator_start_unknown_command(monkeypatch):
    """Test how the calculator handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator = Calculator()

    with pytest.raises(SystemExit):
        calculator.start()

def test_calculator_add_command(capfd, monkeypatch):
    """Test that the calculator correctly handles an 'add' command."""
    inputs = iter(['add 2 3', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator = Calculator()

    with pytest.raises(SystemExit):
        calculator.start()

    # Capture the output of the command
    captured = capfd.readouterr()

    # Check if the result is in the captured output
    assert "Result: 5.0" in captured.out
