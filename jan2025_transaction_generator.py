import csv
import random
from datetime import datetime

# Data for transactions
products = {"Mild": 3.00, "Hot": 3.00, "Honey Mustard": 3.00}
HST_RATE = 0.13  # 13% HST
initial_investments = [
    ["CAP001", "2025-01-01", "Owner Capital Contribution", 50000.00, "Cash", "Initial capital"],
    ["CAP002", "2025-01-02", "Equipment Purchase", -5000.00, "Equipment", "Bottling machine"],
    ["CAP003", "2025-01-03", "Kitchen Lease Agreement", -12000.00, "Prepaid Rent", "1-year commercial kitchen rental"]
]
expenses = [
    ["EXP001", "2025-01-04", "Business Registration", -250.00, "Fees", "LLC formation"],
    ["EXP002", "2025-01-05", "Food Production Permit", -150.00, "Fees", "Health department"],
    ["EXP003", "2025-01-06", "Bottles Purchase", -282.50, "Inventory - Bottles", "Net 30, due 2025-02-06, 1000 bottles, pre-tax $250.00, HST $32.50"],
    ["EXP004", "2025-01-06", "Packaging Purchase", -226.00, "Inventory - Packaging", "Net 30, due 2025-02-06, 1000 units, pre-tax $200.00, HST $26.00"],
    ["EXP005", "2025-01-07", "Website Setup", -339.00, "Marketing", "Net 30, due 2025-02-07, pre-tax $300.00, HST $39.00"]
]

# Utility expenses (monthly, net 30 terms, due Feb 15, 2025, with HST)
utilities = [
    ["UTL001", "2025-01-15", "Electricity Bill", -226.00, "Utilities Expense", "Net 30, due 2025-02-15, pre-tax $200.00, HST $26.00"],
    ["UTL002", "2025-01-15", "Water Bill", -113.00, "Utilities Expense", "Net 30, due 2025-02-15, pre-tax $100.00, HST $13.00"],
    ["UTL003", "2025-01-15", "Gas Bill", -169.50, "Utilities Expense", "Net 30, due 2025-02-15, pre-tax $150.00, HST $19.50"],
    ["UTL004", "2025-01-15", "Internet Bill", -90.40, "Utilities Expense", "Net 30, due 2025-02-15, pre-tax $80.00, HST $10.40"]
]

# Wage expenses
wages = []
# Fixed salary: $50,000/year, biweekly payments ($50,000 / 26 ≈ $1,923.08)
biweekly_salary = round(50000.00 / 26, 2)  # $1,923.08
salary_hst = round(biweekly_salary * HST_RATE, 2)  # $250.00
wages.extend([
    ["WAG001", "2025-01-10", "Salary Payment", -biweekly_salary, "Wages Expense", f"Biweekly salary, HST ${salary_hst:.2f}"],
    ["WAG002", "2025-01-24", "Salary Payment", -biweekly_salary, "Wages Expense", f"Biweekly salary, HST ${salary_hst:.2f}"]
])
# Variable hourly wages: 10-30 hours/week, $20/hour, paid weekly
hourly_rate = 20.00
for i, date in enumerate(["2025-01-03", "2025-01-10", "2025-01-17", "2025-01-24"], start=3):
    hours = random.randint(10, 30)
    base_amount = round(hours * hourly_rate, 2)  # Base wage
    hst_amount = round(base_amount * HST_RATE, 2)  # HST on wage
    wages.append([f"WAG{i:03d}", date, "Hourly Wage Payment", -base_amount, "Wages Expense", f"{hours} hours at ${hourly_rate:.2f}/hour, HST ${hst_amount:.2f}"])

# Generate 20 sales transactions with HST and track bottles sold
sales = []
total_bottles_sold = 0
for i in range(20):
    transaction_id = f"SAL{i+1:04d}"
    date = f"2025-01-{8+i:02d}"
    product = random.choice(list(products.keys()))
    quantity = random.randint(1, 5)
    total_bottles_sold += quantity
    price = products[product]  # $3.00 (pre-tax)
    pre_tax_amount = round(quantity * price, 2)  # Pre-tax total
    hst_amount = round(pre_tax_amount * HST_RATE, 2)  # HST
    total_amount = round(pre_tax_amount + hst_amount, 2)  # Total with HST
    sales.append([transaction_id, date, f"Sale - {product}", total_amount, "Revenue", f"{quantity} bottles, pre-tax ${pre_tax_amount:.2f}, HST ${hst_amount:.2f}"])

# Ingredients expense: $0.60/bottle ±5%, based on total bottles sold, with HST, net 30
ingredient_cost_per_bottle = round(random.uniform(0.57, 0.63), 2)  # $0.57 to $0.63
pre_tax_ingredients = round(total_bottles_sold * ingredient_cost_per_bottle, 2)
ingredients_hst = round(pre_tax_ingredients * HST_RATE, 2)
ingredients_total = round(pre_tax_ingredients + ingredients_hst, 2)
expenses.append([
    "EXP006", "2025-01-06", "Ingredients Purchase", -ingredients_total, "Ingredients Expense",
    f"Net 30, due 2025-02-06, {total_bottles_sold} bottles, pre-tax ${pre_tax_ingredients:.2f}, HST ${ingredients_hst:.2f}"
])

# Combine all transactions
transactions = initial_investments + expenses + utilities + wages + sales

# Write to CSV with month in filename
with open("hot_sauce_financials_january_2025.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Transaction_ID", "Date", "Description", "Amount", "Category", "Notes"])
    for transaction in transactions:
        writer.writerow(transaction)

# Calculate and print inventory status
initial_bottles = 1000
initial_packaging = 1000
bottles_remaining = initial_bottles - total_bottles_sold
packaging_remaining = initial_packaging - total_bottles_sold
print(f"Inventory Status (January 2025):")
print(f"  Bottles - Initial: {initial_bottles}, Sold: {total_bottles_sold}, Remaining: {bottles_remaining}")
print(f"  Packaging - Initial: {initial_packaging}, Sold: {total_bottles_sold}, Remaining: {packaging_remaining}")
