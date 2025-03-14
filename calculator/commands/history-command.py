from calculator.calculator_history import CalculationHistory
class BaseCommand:
    def __init__(self):
        self.history_instance = CalculationHistory()