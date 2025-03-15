"""
Test suite for the CalculationHistory class.

This module contains tests for the CalculationHistory class, including its methods for managing history,
such as adding, deleting, saving, and loading history records.
"""

import os
from unittest.mock import patch  # Standard import should be placed first
import tempfile
import shutil

import pytest
import pandas as pd  # Third-party imports after standard imports
from calculator.plugins.manage_history import CalculationHistory

class TestCalculationHistory:
    """Tests for the CalculationHistory class."""

    @pytest.fixture
    def setup_temp_dir(self):
        """Create a temporary directory for test files."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def reset_singleton(self):
        """Reset the singleton instance between tests."""
        CalculationHistory._instance = None
        yield
        CalculationHistory._instance = None

    @pytest.fixture
    def history_instance(self, reset_singleton):
        """Create a fresh CalculationHistory instance for each test."""
        return CalculationHistory()

    def test_singleton_pattern(self, reset_singleton):
        """Test that CalculationHistory follows the singleton pattern."""
        instance1 = CalculationHistory()
        instance2 = CalculationHistory()
        assert instance1 is instance2

    @patch.dict(os.environ, {"HISTORY_FILE_PATH": "test_history.csv"})
    def test_initialize_with_env_var(self, reset_singleton):
        """Test initialization with environment variables."""
        history = CalculationHistory()
        assert history.history_file.endswith("test_history.csv")

    @patch('os.path.exists')
    @patch('pandas.read_csv')
    def test_load_history_existing_file(self, mock_read_csv, mock_exists, reset_singleton):
        """Test loading history from an existing file."""
        mock_exists.return_value = True
        mock_df = pd.DataFrame({'Operation': ['add'], 'Input': ['1 2'], 'Result': [3]})
        mock_read_csv.return_value = mock_df

        history = CalculationHistory()
        assert history.history.equals(mock_df)
        mock_read_csv.assert_called_once()

    @patch('calculator.plugins.manage_history.load_dotenv')
    @patch('os.path.exists')
    def test_load_history_missing_file(self, mock_exists, mock_load_dotenv, reset_singleton):
        """Test initializing history when file is missing."""
        mock_exists.return_value = False

        history = CalculationHistory()
        assert list(history.history.columns) == ['Operation', 'Input', 'Result']
        assert len(history.history) == 0

    @patch('os.path.exists')
    @patch('pandas.read_csv')
    def test_load_history_error_handling(self, mock_read_csv, mock_exists, reset_singleton):
        """Test error handling when loading history."""
        mock_exists.return_value = True
        mock_read_csv.side_effect = Exception("Test error")

        history = CalculationHistory()
        assert list(history.history.columns) == ['Operation', 'Input', 'Result']
        assert len(history.history) == 0

    @patch('os.makedirs')
    @patch('pandas.DataFrame.to_csv')
    def test_save_history(self, mock_to_csv, mock_makedirs, history_instance):
        """Test saving history to file."""
        history_instance.save_history()
        mock_makedirs.assert_called_once()
        mock_to_csv.assert_called_once()

    @patch('os.makedirs')
    @patch('pandas.DataFrame.to_csv')
    def test_save_history_error_handling(self, mock_to_csv, mock_makedirs, history_instance):
        """Test error handling when saving history."""
        mock_to_csv.side_effect = Exception("Test error")

        # Should not raise exception
        history_instance.save_history()
        mock_makedirs.assert_called_once()

    def test_delete_record_valid_index(self, reset_singleton):
        """Test deleting a record with a valid index."""
        # Create a fresh instance with completely mocked history
        with patch('calculator.plugins.manage_history.CalculationHistory.load_history') as mock_load:
            # Set up a controlled test dataframe
            test_df = pd.DataFrame({
                'Operation': ['add', 'subtract'],
                'Input': ['1 2', '5 2'],
                'Result': [3, 3]
            })
            mock_load.return_value = test_df.copy()

            # Get a fresh instance with our mocked data
            history = CalculationHistory()

            # Mock save_history to prevent file operations
            with patch.object(history, 'save_history'):
                # Verify initial state
                assert len(history.history) == 2

                # Test the delete operation
                result = history.delete_record(0)

                # Verify results
                assert result is True
                assert len(history.history) == 1
                assert history.history.iloc[0]['Operation'] == 'subtract'

    def test_delete_record_invalid_index(self, history_instance):
        """Test deleting a record with an invalid index."""
        with patch.object(history_instance, 'save_history') as mock_save:
            result = history_instance.delete_record(99)
            assert result is False
            mock_save.assert_not_called()

    def test_add_record(self, history_instance):
        """Test adding a record to the history."""
        # Reset the history first
        history_instance.history = pd.DataFrame(columns=['Operation', 'Input', 'Result'])

        with patch.object(history_instance, 'save_history') as mock_save:
            history_instance.add_record('add', '1 2', 3)
            assert len(history_instance.history) == 1
            record = history_instance.history.iloc[0]
            assert record['Operation'] == 'add'
            assert record['Input'] == '1 2'
            assert record['Result'] == 3
            mock_save.assert_called_once()

    def test_print_history(self, history_instance, capfd):
        """Test printing the history."""
        history_instance.add_record('add', '1 2', 3)
        history_instance.print_history()

        captured = capfd.readouterr()
        assert 'Operation' in captured.out
        assert 'Input' in captured.out
        assert 'Result' in captured.out
        assert 'add' in captured.out

    @patch('calculator.plugins.manage_history.os.getenv')
    def test_default_history_path(self, mock_getenv, reset_singleton):
        """Test default history path when environment variable is not set."""
        # Return the default value instead of None
        mock_getenv.return_value = 'calculation_history.csv'

        history = CalculationHistory()
        assert "calculation_history.csv" in history.history_file  

    def test_integration_with_temp_file(self, setup_temp_dir, reset_singleton):
        """Integration test with an actual temporary file."""
        test_file = os.path.join(setup_temp_dir, "test_history.csv")

        with patch.dict(os.environ, {"HISTORY_FILE_PATH": test_file}):
            # Create and populate history
            history1 = CalculationHistory()
            history1.add_record('add', '1 2', 3)
            history1.add_record('multiply', '3 4', 12)

            # Reset singleton and load from file
            CalculationHistory._instance = None
            history2 = CalculationHistory()

            # Verify data was persisted
            assert len(history2.history) == 2
            assert history2.history.iloc[0]['Operation'] == 'add'
            assert history2.history.iloc[1]['Operation'] == 'multiply'
