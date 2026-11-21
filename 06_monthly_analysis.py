import pandas as pd

# Load revenue dataset
df = pd.read_csv("sales_data_with_revenue.csv")

# Convert order date into datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Extract month
df["Month"] = df["Order_Date"].dt.to_period("M")

# Monthly sales analysis
monthly_analysis = df.groupby("Month").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Orders=("Order_ID", "nunique"),
    Total_Quantity=("Quantity", "sum")
)

# Sort months chronologically
monthly_analysis = monthly_analysis.sort_index()

# Convert month index into readable format
monthly_analysis.index = monthly_analysis.index.strftime("%B %Y")

# Save monthly report
monthly_analysis.to_csv("monthly_analysis.csv")

# Display results
print("===== MONTHLY SALES ANALYSIS =====")
print(monthly_analysis)

# Find highest and lowest revenue months
highest_month = monthly_analysis["Total_Revenue"].idxmax()
lowest_month = monthly_analysis["Total_Revenue"].idxmin()

print("\n===== HIGHEST REVENUE MONTH =====")
print(highest_month)
print("Revenue:", monthly_analysis.loc[highest_month, "Total_Revenue"])

print("\n===== LOWEST REVENUE MONTH =====")
print(lowest_month)
print("Revenue:", monthly_analysis.loc[lowest_month, "Total_Revenue"])

print("\nMonthly analysis completed successfully!")