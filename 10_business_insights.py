
import pandas as pd

# ==========================================
# 1. LOAD ANALYSIS FILES
# ==========================================

product = pd.read_csv("product_analysis.csv")
category = pd.read_csv("category_analysis.csv")
monthly = pd.read_csv("monthly_analysis.csv")
region = pd.read_csv("region_analysis.csv")
payment = pd.read_csv("payment_analysis.csv")

# ==========================================
# 2. TOTAL REVENUE
# ==========================================

total_revenue = product["Total_Revenue"].sum()

# ==========================================
# 3. PRODUCT INSIGHTS
# ==========================================

top_product = product.sort_values(
    "Total_Revenue", ascending=False
).iloc[0]

top_quantity_product = product.sort_values(
    "Total_Quantity", ascending=False
).iloc[0]

# ==========================================
# 4. CATEGORY INSIGHTS
# ==========================================

top_category = category.sort_values(
    "Total_Revenue", ascending=False
).iloc[0]

category_share = (
    top_category["Total_Revenue"] / total_revenue
) * 100

# ==========================================
# 5. MONTHLY INSIGHTS
# ==========================================

best_month = monthly.sort_values(
    "Total_Revenue", ascending=False
).iloc[0]

lowest_month = monthly.sort_values(
    "Total_Revenue", ascending=True
).iloc[0]

# ==========================================
# 6. REGION INSIGHTS
# ==========================================

top_region = region.sort_values(
    "Total_Revenue", ascending=False
).iloc[0]

top_region_quantity = region.sort_values(
    "Total_Quantity", ascending=False
).iloc[0]

# ==========================================
# 7. PAYMENT INSIGHTS
# ==========================================

top_payment = payment.sort_values(
    "Total_Revenue", ascending=False
).iloc[0]

# ==========================================
# 8. CREATE REPORT
# ==========================================

report = f"""
==================================================
        SALES & REVENUE ANALYSIS
              BUSINESS INSIGHTS
==================================================

Dataset: Simulated Sales Dataset
Period: January - June 2026
Total Revenue: Rs. {total_revenue:,.0f}

--------------------------------------------------
1. PRODUCT PERFORMANCE
--------------------------------------------------

Highest Revenue Product:
{top_product['Product']}

Revenue:
Rs. {top_product['Total_Revenue']:,.0f}

Highest Quantity Sold Product:
{top_quantity_product['Product']}

Units Sold:
{top_quantity_product['Total_Quantity']:,.0f}

Insight:
The product generating the highest revenue is an important
contributor to overall sales performance.

--------------------------------------------------
2. CATEGORY PERFORMANCE
--------------------------------------------------

Top Revenue Category:
{top_category['Category']}

Category Revenue:
Rs. {top_category['Total_Revenue']:,.0f}

Revenue Contribution:
{category_share:.2f}%

Insight:
The leading category contributes a significant share of
the total revenue.

--------------------------------------------------
3. MONTHLY PERFORMANCE
--------------------------------------------------

Best Performing Month:
{best_month['Month']}

Revenue:
Rs. {best_month['Total_Revenue']:,.0f}

Lowest Performing Month:
{lowest_month['Month']}

Revenue:
Rs. {lowest_month['Total_Revenue']:,.0f}

Insight:
Monthly revenue changes over time. The lowest performing
month can be investigated to identify possible reasons
for the decrease.

--------------------------------------------------
4. REGIONAL PERFORMANCE
--------------------------------------------------

Highest Revenue Region:
{top_region['Region']}

Revenue:
Rs. {top_region['Total_Revenue']:,.0f}

Highest Quantity Region:
{top_region_quantity['Region']}

Units Sold:
{top_region_quantity['Total_Quantity']:,.0f}

Insight:
Regional sales performance differs in terms of revenue
and quantity sold.

--------------------------------------------------
5. PAYMENT METHOD PERFORMANCE
--------------------------------------------------

Highest Revenue Payment Method:
{top_payment['Payment_Method']}

Revenue:
Rs. {top_payment['Total_Revenue']:,.0f}

Insight:
The leading payment method contributes the highest
revenue among the available payment options.

--------------------------------------------------
6. BUSINESS RECOMMENDATIONS
--------------------------------------------------

1. Maintain sufficient inventory for high-revenue products.

2. Investigate the lowest-performing month to understand
   seasonal or sales-related changes.

3. Explore opportunities to increase sales in categories
   with lower revenue contributions.

4. Study high-performing regions to identify strategies
   that may help improve other regions.

5. Continue supporting different payment methods to
   provide flexibility to customers.

6. Use the dashboard filters to monitor sales trends,
   revenue, and product performance regularly.

--------------------------------------------------
NOTE
--------------------------------------------------

This report is generated from a simulated dataset
created for an internship project.

The insights represent sample data analysis and
not actual company sales.

==================================================
END OF REPORT
==================================================
"""

# ==========================================
# 9. SAVE REPORT
# ==========================================

with open("business_insights.txt", "w", encoding="utf-8") as file:
    file.write(report)

# ==========================================
# 10. DISPLAY REPORT
# ==========================================

print(report)

print("\nBusiness insights report saved successfully!")
print("File: business_insights.txt")
