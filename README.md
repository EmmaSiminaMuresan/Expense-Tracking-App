# Expense Tracker

This project is a simple **Expense Tracker** built using Python. It allows users to log their daily expenses, categorize them, and track how much they have spent relative to a preset budget. The program provides a summary of expenses by category and calculates the remaining budget for the month.

## Features

- **Expense Logging**: Users can input the name, amount, and category of their expenses.
- **Expense Categorization**: Expenses are categorized into predefined categories such as Food, Home, Work, Fun, and Other.
- **File Storage**: All expense records are saved in a CSV file for persistence.
- **Expense Summary**: A detailed summary of expenses by category is provided, including total expenditure and remaining budget.
- **Emoji Integration**: Visual appeal is added using emojis for each expense category and actions.

## Project Structure

- **`expense.py`**: Defines the `Expense` class that represents an expense with a name, category, and amount.
- **`expense_tracker.py`**: The main script that handles user input, saving expenses to a CSV file, and summarizing expenses.

## How It Works

1. **User Input**: The user is prompted to enter the expense name, amount, and select a category.
2. **Saving to CSV**: Each expense is saved to a CSV file (`expenses.csv`) in the format: `name, amount, category`.
3. **Expense Summary**: The system reads all expenses from the file and provides a summary of total expenditure by category and remaining budget for the month.


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/expense-tracker.git
    cd expense-tracker
    ```

2. Install dependencies (if any):
    ```bash
    pip install emoji
    ```

3. Run the Expense Tracker:
    ```bash
    python expense_tracker.py
    ```

## Usage

Once you run the tracker, follow these steps:

1. **Enter Expenses**:
   - The program will prompt you to enter the name, amount, and category for each expense.
   - After each entry, the expense will be saved to the `expenses.csv` file.

2. **Add More Expenses or Exit**:
   - The program will ask if you want to add another expense or exit. Type `yes` to continue or `no` to exit.

3. **Summary of Expenses**:
   - Once you choose to exit, the program will summarize your expenses.
   - It will display the total expenses for each category, total spending, and how much budget remains for the month.


## File Structure

- **`expense_tracker.py`**: Main script to run the tracker.
- **`expense.py`**: Contains the `Expense` class definition.
- **`expenses.csv`**: File where all expense records are stored.

## Customization

You can adjust the preset **monthly budget** by modifying the value in the `expense_tracker.py` script:

```python
budget = 2000  # Set your budget here

