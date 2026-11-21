import csv
import random
from datetime import datetime, timedelta

random.seed(42)

products = {
    "Laptop": ("Electronics", 55000),
    "Monitor": ("Electronics", 12000),
    "Keyboard": ("Accessories", 1200),
    "Mouse": ("Accessories", 500),
    "Office Chair": ("Furniture", 4500),
    "Office Desk": ("Furniture", 8000),
    "Headphones": ("Electronics", 2500),
    "Printer": ("Electronics", 9500),
    "USB Drive": ("Accessories", 700),
    "Webcam": ("Electronics", 3200)
}

regions = ["North", "South", "East", "West"]
payment_methods = ["UPI", "Credit Card", "Debit Card", "Cash"]

start_date = datetime(2026, 1, 1)

file_name = "sales_data.csv"

with open(file_name, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Order_ID",
        "Order_Date",
        "Customer_ID",
        "Product",
        "Category",
        "Quantity",
        "Unit_Price",
        "Region",
        "Payment_Method"
    ])

    for i in range(1, 501):

        order_date = start_date + timedelta(
            days=random.randint(0, 180)
        )

        product = random.choice(list(products.keys()))

        category, price = products[product]

        quantity = random.randint(1, 10)

        region = random.choice(regions)

        payment = random.choice(payment_methods)

        customer_id = f"C{random.randint(1001, 1150)}"

        writer.writerow([
            10000 + i,
            order_date.strftime("%Y-%m-%d"),
            customer_id,
            product,
            category,
            quantity,
            price,
            region,
            payment
        ])

print("Dataset created successfully!")
print("File name:", file_name)
print("Total records: 500")
print("Data period: January 2026 to June 2026")