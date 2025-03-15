"""
Base classes for the calculator application.
"""

from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract base class for defining command execution.
    """

    @abstractmethod
    def execute(self, *args):
        """
        Abstract method that should be implemented by subclasses to execute a specific command.

                """
