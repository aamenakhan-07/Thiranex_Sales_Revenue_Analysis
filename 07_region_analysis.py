import pandas as pd

# Load revenue dataset
df = pd.read_csv("sales_data_with_revenue.csv")

# Region-wise analysis
region_analysis = df.groupby("Region").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Orders=("Order_ID", "nunique"),
    Total_Quantity=("Quantity", "sum")
)

# Sort by revenue
region_analysis = region_analysis.sort_values(
    by="Total_Revenue",
    ascending=False
)

# Save report
region_analysis.to_csv("region_analysis.csv")

# Display results
print("===== REGION-WISE SALES ANALYSIS =====")
print(region_analysis)

# Identify top-performing region
top_revenue_region = region_analysis["Total_Revenue"].idxmax()
top_quantity_region = region_analysis["Total_Quantity"].idxmax()

print("\n===== TOP REVENUE REGION =====")
print(top_revenue_region)

print("\n===== TOP QUANTITY REGION =====")
print(top_quantity_region)

print("\nRegion analysis completed successfully!")