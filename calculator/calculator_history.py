import logging
import pandas as pd

logger = logging.getLogger('calculator')

class CalculationHistory:
    def __init__(self, filename='calculation_history.csv'):
        self.filename = filename
        self.history = self.load_history()

    def load_history(self):
        try:
            return pd.read_csv(self.filename)
        except FileNotFoundError:
            logger.info('No existing history found')
            return pd.DataFrame(columns=['Operation', 'Input', 'Result'])

    def save_history(self):
        self.history.to_csv(self.filename, index=False)
        logger.info('History saved')

    def clear_history(self):
        self.history = pd.DataFrame(columns=['Operation', 'Input', 'Result'])
        self.save_history()
        logger.info('History cleared')

    def delete_record(self, index):
        self.history.drop(index, inplace=True)
        self.save_history()
        logger.info(f'Record {index} deleted')

    def add_record(self, operation, input_str, result):
        new_record = pd.DataFrame({'Operation': [operation], 'Input': [input_str], 'Result': [result]})
        self.history = pd.concat([self.history, new_record])
        self.save_history()
        logger.info(f'Record added: {operation} {input_str} = {result}')

    def print_history(self):
        logger.info('Printing history')
        print(self.history)