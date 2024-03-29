def display_menu():
  """Displays the main menu options."""
  print("Welcome to the Calculator!")
  print("1. Launch Calculator")
  print("2. Run Automated Tests using unittest and faker")
  print("3. Exit")

def get_user_choice():
  """Prompts the user for a choice and validates input."""
  while True:
    choice = input("Enter your choice (1/2/3): ")
    if choice in ("1", "2", "3"):
      return choice
    else:
      print("Invalid choice. Please try again.")

def handle_choice(choice):
  """Executes the selected functionality based on user input."""
  if choice == "1":
    launch_calculation_tool()
  elif choice == "2":
    run_autotest()
  else:
    print("Exiting the program.")

def launch_calculation_tool():
  """Placeholder function for launching the calculator."""
  # Replace this with your actual calculator implementation
  print("Calculator functionality coming soon!")

def run_autotest():
  """Placeholder function for running autotests."""
  # Replace this with your actual autotest module integration
  print("Autotest functionality under development!")

def main():
  """Main function to run the program."""
  while True:
    display_menu()
    choice = get_user_choice()
    handle_choice(choice)
    if choice == "3":
      break

if __name__ == "__main__":
  main()
