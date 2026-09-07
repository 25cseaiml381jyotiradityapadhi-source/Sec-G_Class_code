# Prompt the user for input
date = input("Enter the date (YYYY-MM-DD): ").strip()
item = input("Enter the item name: ").strip()
cost = input("Enter the cost: ").strip()

data_row = f"{date}\n{item}\n{cost}\n"


with open("expenses.csv", mode="w") as file:
    file.write(data_row)

print("Expense logged successfully!")