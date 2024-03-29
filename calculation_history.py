import os
import pandas as pd

class CalculationHistoryManager:
    @staticmethod
    def save_calculation_result(a, op, b, result):
        """Static method to save a calculation to a CSV file."""
        file_n = os.getenv("HISTORY_CSV_FILE", "calculator_history.csv")
        data = {'Operand1': [a], 'Operator': [op], 'Operand2': [b], 'Result': [result]}
        df = pd.DataFrame(data)
        try:
            if os.path.exists(file_n):
                # Read existing history
                history_df = pd.read_csv(file_n)
                # Concatenate existing history with new calculation
                history_df = pd.concat([history_df, df], ignore_index=True)
                # Keep only the most recent 5 calculations
                history_df = history_df.tail(5)
                # Save to CSV
                history_df.to_csv(file_n, index=False)
            else:
                df.to_csv(file_n, index=False)
        except pd.errors.EmptyDataError:
            print("No saved calculations.")

    @staticmethod
    def display_calculation_history():
        """Static method to display the history of saved calculations."""
        file_n = os.getenv("HISTORY_CSV_FILE", "calculator_history.csv")
        if not os.path.exists(file_n):
            print("No saved calculations.")
            return
        try:
            df = pd.read_csv(file_n)
            if df.empty:
                print("No saved calculations.")
                return
            print("Saved calculations:")
            for i, row in df.iterrows():
                print(f"Saved calculation {i+1}: {row['Operand1']} {row['Operator']} {row['Operand2']} = {row['Result']}")
        except pd.errors.EmptyDataError:
            print("No saved calculations.")

