import pandas as pd

# Load dataset containing calculated revenue
df = pd.read_csv("sales_data_with_revenue.csv")

# Product-wise sales analysis
product_analysis = df.groupby("Product").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Quantity=("Quantity", "sum"),
    Total_Orders=("Order_ID", "nunique")
)

# Sort by revenue from highest to lowest
product_analysis = product_analysis.sort_values(
    by="Total_Revenue",
    ascending=False
)

# Save analysis to CSV
product_analysis.to_csv("product_analysis.csv")

# Display results
print("===== PRODUCT-WISE SALES ANALYSIS =====")
print(product_analysis)

# Highest revenue product
top_revenue_product = product_analysis["Total_Revenue"].idxmax()

# Highest quantity product
top_quantity_product = product_analysis["Total_Quantity"].idxmax()

print("\n===== TOP REVENUE PRODUCT =====")
print(top_revenue_product)

print("\n===== TOP SELLING PRODUCT (QUANTITY) =====")
print(top_quantity_product)

print("\nProduct analysis completed successfully!")