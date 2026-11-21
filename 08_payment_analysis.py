import pandas as pd

# Load revenue dataset
df = pd.read_csv("sales_data_with_revenue.csv")

# Payment method analysis
payment_analysis = df.groupby("Payment_Method").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Orders=("Order_ID", "nunique"),
    Total_Quantity=("Quantity", "sum")
)

# Sort by revenue
payment_analysis = payment_analysis.sort_values(
    by="Total_Revenue",
    ascending=False
)

# Save analysis
payment_analysis.to_csv("payment_analysis.csv")

# Display results
print("===== PAYMENT METHOD ANALYSIS =====")
print(payment_analysis)

# Highest revenue payment method
top_payment = payment_analysis["Total_Revenue"].idxmax()

# Highest order payment method
top_order_payment = payment_analysis["Total_Orders"].idxmax()

print("\n===== TOP REVENUE PAYMENT METHOD =====")
print(top_payment)

print("\n===== MOST USED PAYMENT METHOD (ORDERS) =====")
print(top_order_payment)

print("\nPayment analysis completed successfully!")