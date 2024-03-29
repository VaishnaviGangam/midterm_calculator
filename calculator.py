# calculator.py
import os
import logging
from commandManager import OperationManager
from calculation_history import CalculationHistory

# Retrieve the value of the LOG_LEVEL environment variable
# Configure logging to output to a file
log_level = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(filename='calculator.log',
                    level=logging.getLevelName(log_level),
                    format='%(asctime)s - %(levelname)s - %(message)s')


# ... (logging configuration unchanged)

# Initialize History object
calculation_record = CalculationHistory()


def request_valid_float(prompt_message):
    """Prompt user for a valid float input."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def save_calculation_result(a, op, b, result, operator):
        calculation_record.save_to_csv(a, op, b, result, operator)
        print("Calculation saved successfully.")


def view_past_calculations():
    """View the history of saved calculations."""
    calculation_record.show_history()



import re

def display_calculation_options():
    """Display calculator menu and handle user input."""
    while True:
        print("Enter an expression (e.g., 2 + 3), or select an option:")
        print("1. View History")
        print("2. Exit")

        user_input = input("Enter your choice or expression: ")

        if user_input.lower() == 'exit' or user_input == '2':
            break  # Exit the calculator
        elif user_input.lower() == 'view history' or user_input == '1':
            view_past_calculations()
        else:
            # Try to parse the input as an expression
            try:
                num1, operator, num2 = re.findall(r'(\d+|\W+)', user_input)
                num1 = float(num1)
                num2 = float(num2)
                if operator == '+':
                    operation = lambda x, y: OperationManager.compute_sum(x, y)
                elif operator == '-':
                    operation = lambda x, y: OperationManager.compute_difference(x, y)
                elif operator == '*':
                    operation = lambda x, y: OperationManager.compute_product(x, y)
                elif operator == '/':
                    operation = lambda x, y: OperationManager.compute_quotient(x, y)
                else:
                    print("Invalid operator!")
                    continue
                result = operation(num1, num2)
                print("Result:", result)
            except Exception as e:
                print("Invalid input or expression:", e)

# Define view_past_calculations() function here
def view_past_calculations():
    pass  # Placeholder for viewing past calculations

if __name__ == "__main__":
    display_calculation_options()
