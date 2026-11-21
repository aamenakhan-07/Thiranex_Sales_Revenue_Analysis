import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Calculate revenue for each order
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

# Save updated dataset
df.to_csv("sales_data_with_revenue.csv", index=False)

# Calculate key business metrics
total_revenue = df["Revenue"].sum()
total_orders = df["Order_ID"].nunique()
total_units = df["Quantity"].sum()
average_order_value = total_revenue / total_orders
total_customers = df["Customer_ID"].nunique()

# Display results
print("===== SALES & REVENUE ANALYSIS =====")

print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Units Sold: {total_units:,}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")
print(f"Unique Customers: {total_customers:,}")

print("\nRevenue column added successfully!")
print("Updated dataset saved as sales_data_with_revenue.csv")