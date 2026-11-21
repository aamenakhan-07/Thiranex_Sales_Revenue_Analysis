import pandas as pd

# Load revenue dataset
df = pd.read_csv("sales_data_with_revenue.csv")

# Category-wise analysis
category_analysis = df.groupby("Category").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Quantity=("Quantity", "sum"),
    Total_Orders=("Order_ID", "nunique")
)

# Sort categories by revenue
category_analysis = category_analysis.sort_values(
    by="Total_Revenue",
    ascending=False
)

# Save report
category_analysis.to_csv("category_analysis.csv")

# Display results
print("===== CATEGORY-WISE SALES ANALYSIS =====")
print(category_analysis)

# Find top-performing category
top_revenue_category = category_analysis["Total_Revenue"].idxmax()
top_quantity_category = category_analysis["Total_Quantity"].idxmax()

print("\n===== TOP REVENUE CATEGORY =====")
print(top_revenue_category)

print("\n===== TOP SELLING CATEGORY (QUANTITY) =====")
print(top_quantity_category)

print("\nCategory analysis completed successfully!")