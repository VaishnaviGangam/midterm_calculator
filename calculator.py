import re
import os
import logging
from commandManager import OperationManager
from calculation_history import CalculationHistoryManager

# Retrieve the value of the LOG_LEVEL environment variable
# Configure logging to output to a file
log_level = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(filename='log_history.log',
                    level=logging.getLevelName(log_level),
                    format='%(asctime)s - %(levelname)s - %(message)s')



def squareRoot():
    """Calculate the square root of a number."""
    num = request_valid_float("Enter a number to calculate its square root: ")
    if num < 0:
        logging.error("Cannot calculate the square root of a negative number.")
        raise ValueError("Cannot calculate the square root of a negative number.")
    result = OperationManager.compute_square_root(num)
    print(f"The square root of {num} is {result}")

def binary():
    """Convert a number to binary."""
    num = int(request_valid_float("Enter a number to convert to binary: "))
    result = OperationManager.convert_to_binary(num)
    print(f"The binary representation of {num} is {result}")


def request_valid_float(prompt_message):
    """Prompt user for a valid float input."""
    while True:
        try:
            value = float(input(prompt_message))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")



def view_past_calculations():
    """View the history of saved calculations."""
    CalculationHistoryManager.display_calculation_history()




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
                save = input("Do you want to save this calculation? (yes/no): ")
                if save.lower() == 'yes':
                    CalculationHistoryManager.save_calculation_result(num1, operator, num2, result)
            except Exception as e:
                print("Invalid input or expression:", e)


if __name__ == "__main__":
    display_calculation_options()
