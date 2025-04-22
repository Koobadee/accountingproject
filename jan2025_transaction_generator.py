import csv
import random
from datetime import datetime

# Data for transactions
products = {"Mild": 3.00, "Hot": 3.00, "Honey Mustard": 3.00}
initial_investments = [
    ["CAP001", "2025-01-01", "Owner Capital Contribution", 20000.00, "Cash", "Initial capital"],
    ["CAP002", "2025-01-02", "Equipment Purchase", -5000.00, "Equipment", "Bottling machine"],
    ["CAP003", "2025-01-03", "Kitchen Lease Agreement", -12000.00, "Prepaid Rent", "1-year commercial kitchen rental"]
]
expenses = [
    ["EXP001", "2025-01-04", "Business Registration", -250.00, "Fees", "LLC formation"],
    ["EXP002", "2025-01-05", "Food Production Permit", -150.00, "Fees", "Health department"],
    ["EXP003", "2025-01-06", "Ingredients", -500.00, "Supplies", "Peppers, vinegar, honey"],
    ["EXP004", "2025-01-07", "Website Setup", -300.00, "Marketing", "E-commerce platform"]
]

# Generate 20 sales transactions
sales = []
for i in range(20):
    transaction_id = f"SAL{i+1:04d}"
    date = f"2025-01-{8+i:02d}"
    product = random.choice(list(products.keys()))
    quantity = random.randint(1, 5)
    price = products[product]
    total_amount = quantity * price
    sales.append([transaction_id, date, f"Sale - {product}", total_amount, "Revenue", f"{quantity} bottles"])

# Combine all transactions
transactions = initial_investments + expenses + sales

# Write to CSV with month in filename
with open("hot_sauce_financials_january_2025.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Transaction_ID", "Date", "Description", "Amount", "Category", "Notes"])
    for transaction in transactions:
        writer.writerow(transaction)
