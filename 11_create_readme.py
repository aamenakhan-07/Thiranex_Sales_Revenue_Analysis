
# ==========================================
# CREATE PROJECT README
# ==========================================

readme = """# Sales & Revenue Analysis Dashboard

## Project Overview
This project analyzes a simulated sales dataset to understand sales performance, revenue trends, product performance, regional performance, and customer purchasing patterns.

An interactive dashboard was developed to help users explore sales data using multiple filters.

## Project Objectives
- Analyze overall sales and revenue.
- Identify top-performing products and categories.
- Explore monthly revenue trends.
- Compare sales performance across regions.
- Analyze payment methods.
- Build an interactive sales dashboard.

## Tools & Technologies
- Python
- Pandas
- CSV
- HTML
- CSS
- JavaScript
- Pydroid 3 (Android development environment)

## Dataset Details
- Total Records: 500
- Time Period: January to June 2026
- Total Columns: 9 original columns

### Dataset Columns
- Order_ID
- Order_Date
- Customer_ID
- Product
- Category
- Quantity
- Unit_Price
- Region
- Payment_Method

Revenue was calculated using:

Revenue = Quantity * Unit_Price

## Key Performance Indicators (KPIs)
- Total Revenue: Rs. 24,377,200
- Total Orders: 500
- Units Sold: 2,781
- Unique Customers: 145
- Average Order Value: Rs. 48,754.40

## Analysis Performed
1. Data overview and quality checks
2. Revenue analysis
3. Product analysis
4. Category analysis
5. Monthly sales analysis
6. Regional analysis
7. Payment method analysis

## Key Business Insights

### Product Performance
Laptop generated the highest revenue at Rs. 12,045,000.

Monitor recorded the highest quantity sold, with 343 units.

### Category Performance
Electronics generated Rs. 19,973,100 in revenue, contributing approximately 81.93% of total revenue.

### Monthly Performance
March 2026 recorded the highest monthly revenue at Rs. 5,127,800.

February 2026 recorded the lowest monthly revenue at Rs. 3,104,100.

### Regional Performance
East generated the highest regional revenue at Rs. 6,910,700.

North recorded the highest quantity sold, with 758 units.

### Payment Method
Credit Card generated the highest revenue among payment methods, with Rs. 8,554,400.

## Dashboard Features
- Total Revenue KPI
- Total Orders KPI
- Units Sold KPI
- Customer KPI
- Average Order Value KPI
- Monthly Revenue Trend
- Revenue by Product
- Revenue by Category
- Revenue by Region
- Revenue by Payment Method
- Interactive Month, Region, Category, Product, and Payment Method filters

## Business Recommendations
- Monitor inventory of high-revenue products.
- Investigate low-performing months.
- Explore opportunities in lower-revenue categories.
- Learn from high-performing regions.
- Continue offering multiple payment methods.
- Use the dashboard for regular sales performance monitoring.

## Project Files
- `sales_data.csv` — Original simulated dataset
- `sales_data_with_revenue.csv` — Dataset with calculated revenue
- `product_analysis.csv` — Product summary
- `category_analysis.csv` — Category summary
- `monthly_analysis.csv` — Monthly summary
- `region_analysis.csv` — Regional summary
- `payment_analysis.csv` — Payment summary
- `business_insights.txt` — Business insights report
- `sales_dashboard.html` — Interactive dashboard

## Disclaimer
This project uses simulated data created for educational and internship purposes. The results do not represent actual company sales or customer transactions.

## Author
Created as part of the Thiranex EduTech LLP Data Analytics Internship - Task 1.
"""

with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme)

print("README created successfully!")
print("File: README.md")
