from expense import Expense
import datetime
import calendar
import emoji

def main():
    print(emoji.emojize(":rocket: Running Expense Tracker!"))
    
    expense_file_path = "expenses.csv"
    budget = 2000
    
    while True:
        # Get user input for expense.
        expense = get_user_expense()
        
        # Write their expense to a file.
        save_expense_to_file(expense, expense_file_path)
        
        # Ask the user if they want to continue or quit
        continue_input = input(emoji.emojize(":thinking_face: Do you want to add another expense? (yes/no): ")).lower()
        if continue_input == "no":
            break
    
    # Summarize expenses at the end
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    print(emoji.emojize(":money_with_wings: Getting User Expense"))
    expense_name = input("Enter expense name: ")
    expense_amount = float(input(emoji.emojize(":money_with_wings: Enter expense amount: ")))

    print(emoji.emojize(f":white_check_mark: You've entered {expense_name}, {expense_amount}"))

    expense_categories = [
        "Food", 
        "Home", 
        "Work", 
        "Fun", 
        "Other",
    ]
    
    while True:
        print(emoji.emojize(":clipboard: Select a category: "))
        for i, category_name in enumerate(expense_categories):
            print(emoji.emojize(f" {i+1}. {category_name}"))
            
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
        
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print(emoji.emojize(":warning: Invalid category. Please try again!"))
        

def save_expense_to_file(expense: Expense, expense_file_path):
    print(emoji.emojize(f":floppy_disk: Saving User Expense: {expense} to {expense_file_path}"))
    
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
    

def summarize_expenses(expense_file_path, budget):
    print(emoji.emojize(":bar_chart: Summarizing User Expenses"))
    
    expenses: list[Expense] = []
    
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(",")   
                     
            line_expense = Expense(
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
            expenses.append(line_expense)
    
    # Emoji mapping for categories
    category_emoji_map = {
        "Food": ":hamburger:",
        "Home": ":house:",
        "Work": ":briefcase:",
        "Fun": ":video_game:",
        "Other": ":pushpin:"
    }
    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
            
    print(emoji.emojize(":ledger: Expenses By Category:"))
    for key, amount in amount_by_category.items():
        emoji_icon = emoji.emojize(category_emoji_map.get(key, ":moneybag:"))
        print(f"  {emoji_icon} {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(emoji.emojize(f":money_with_wings: Total spent: ${total_spent:.2f}"))
    
    remaining_budget = budget - total_spent
    print(emoji.emojize(f":money_with_wings: Budget Remaining: ${remaining_budget:.2f} "))
    
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    
    daily_budget = remaining_budget / remaining_days
    print(green(emoji.emojize(f":calendar: Budget Per Day: ${daily_budget:.2f}")))


def green(text):
    return f"\033[92m{text}\033[0m"

    

if __name__ == "__main__":
    main()
