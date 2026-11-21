
import pandas as pd
import json

# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("sales_data_with_revenue.csv")

df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.strftime("%Y-%m")

data = df.to_dict(orient="records")
data_json = json.dumps(data, default=str)

# ==========================================
# 2. DASHBOARD HTML
# ==========================================

html = r'''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Sales & Revenue Dashboard</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 16px;
    background: #f3f5f9;
    font-family: Arial, sans-serif;
    color: #20253a;
}

.header {
    background: #18243e;
    color: white;
    padding: 24px;
    border-radius: 15px;
    margin-bottom: 20px;
}

.header h1 {
    margin: 0 0 8px;
    font-size: 25px;
}

.header p {
    margin: 0;
    color: #d2d9e8;
}

.filters {
    background: white;
    padding: 16px;
    border-radius: 12px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 12px;
    margin-bottom: 20px;
}

.filters label {
    font-size: 13px;
    font-weight: bold;
}

.filters select {
    width: 100%;
    padding: 10px;
    margin-top: 6px;
    border: 1px solid #d6dbe5;
    border-radius: 8px;
    background: white;
}

button {
    padding: 10px;
    background: #344f91;
    color: white;
    border: none;
    border-radius: 8px;
    margin-top: 20px;
}

.kpis {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(145px, 1fr));
    gap: 12px;
    margin-bottom: 20px;
}

.card {
    background: white;
    padding: 17px;
    border-radius: 12px;
    box-shadow: 0 2px 7px #00000008;
}

.card p {
    color: #69758a;
    margin: 0 0 10px;
    font-size: 13px;
}

.card h2 {
    margin: 0;
    font-size: 21px;
    color: #24385f;
    overflow-wrap: anywhere;
}

.charts {
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
}

.chart-card {
    background: white;
    border-radius: 12px;
    padding: 15px;
    min-width: 0;
}

.chart-card h3 {
    margin: 0 0 14px;
    font-size: 16px;
}

canvas {
    width: 100%;
    height: 300px;
    display: block;
}

.footer {
    text-align: center;
    padding: 22px 5px;
    font-size: 12px;
    color: #777;
}

@media (min-width: 800px) {
    .charts {
        grid-template-columns: 1fr 1fr;
    }
    .wide {
        grid-column: span 2;
    }
}

</style>
</head>

<body>

<div class="header">
    <h1>Sales & Revenue Dashboard</h1>
    <p>Sales performance overview | Sample Dataset | Jan–Jun 2026</p>
</div>

<!-- FILTERS -->

<div class="filters">

    <div>
        <label>Month</label>
        <select id="month">
            <option value="ALL">All Months</option>
        </select>
    </div>

    <div>
        <label>Region</label>
        <select id="region">
            <option value="ALL">All Regions</option>
        </select>
    </div>

    <div>
        <label>Category</label>
        <select id="category">
            <option value="ALL">All Categories</option>
        </select>
    </div>

    <div>
        <label>Product</label>
        <select id="product">
            <option value="ALL">All Products</option>
        </select>
    </div>

    <div>
        <label>Payment Method</label>
        <select id="payment">
            <option value="ALL">All Payments</option>
        </select>
    </div>

</div>

<!-- KPI CARDS -->

<div class="kpis">

    <div class="card">
        <p>Total Revenue</p>
        <h2 id="revenue">₹0</h2>
    </div>

    <div class="card">
        <p>Total Orders</p>
        <h2 id="orders">0</h2>
    </div>

    <div class="card">
        <p>Units Sold</p>
        <h2 id="units">0</h2>
    </div>

    <div class="card">
        <p>Customers</p>
        <h2 id="customers">0</h2>
    </div>

    <div class="card">
        <p>Average Order Value</p>
        <h2 id="aov">₹0</h2>
    </div>

</div>

<!-- CHARTS -->

<div class="charts">

    <div class="chart-card wide">
        <h3>Monthly Revenue Trend</h3>
        <canvas id="monthlyChart"></canvas>
    </div>

    <div class="chart-card">
        <h3>Revenue by Product</h3>
        <canvas id="productChart"></canvas>
    </div>

    <div class="chart-card">
        <h3>Revenue by Category</h3>
        <canvas id="categoryChart"></canvas>
    </div>

    <div class="chart-card">
        <h3>Revenue by Region</h3>
        <canvas id="regionChart"></canvas>
    </div>

    <div class="chart-card">
        <h3>Revenue by Payment Method</h3>
        <canvas id="paymentChart"></canvas>
    </div>

</div>

<div class="footer">
    Thiranex Internship — Task 1 | Sales & Revenue Analysis<br>
    Dashboard built using Python, Pandas, HTML, CSS and JavaScript
</div>

<script>

// ==========================================
// 3. DATA
// ==========================================

const data = DATA_PLACEHOLDER;

// ==========================================
// 4. FORMAT NUMBERS
// ==========================================

function money(value) {
    return "₹" + Math.round(value).toLocaleString("en-IN");
}

// ==========================================
// 5. CREATE FILTER OPTIONS
// ==========================================

function fillDropdown(id, values) {
    const dropdown = document.getElementById(id);

    [...new Set(values)]
        .sort()
        .forEach(value => {
            const option = document.createElement("option");
            option.value = value;
            option.textContent = value;
            dropdown.appendChild(option);
        });
}

fillDropdown("month", data.map(r => r.Month));
fillDropdown("region", data.map(r => r.Region));
fillDropdown("category", data.map(r => r.Category));
fillDropdown("product", data.map(r => r.Product));
fillDropdown("payment", data.map(r => r.Payment_Method));

// ==========================================
// 6. FILTER DATA
// ==========================================

function filteredData() {

    const selectedMonth =
        document.getElementById("month").value;

    const selectedRegion =
        document.getElementById("region").value;

    const selectedCategory =
        document.getElementById("category").value;

    const selectedProduct =
        document.getElementById("product").value;

    const selectedPayment =
        document.getElementById("payment").value;

    return data.filter(r =>

        (selectedMonth === "ALL" ||
         r.Month === selectedMonth) &&

        (selectedRegion === "ALL" ||
         r.Region === selectedRegion) &&

        (selectedCategory === "ALL" ||
         r.Category === selectedCategory) &&

        (selectedProduct === "ALL" ||
         r.Product === selectedProduct) &&

        (selectedPayment === "ALL" ||
         r.Payment_Method === selectedPayment)

    );
}

// ==========================================
// 7. UPDATE KPI CARDS
// ==========================================

function updateKPIs(records) {

    const totalRevenue = records.reduce(
        (sum, r) => sum + Number(r.Revenue), 0
    );

    const totalOrders = records.length;

    const totalUnits = records.reduce(
        (sum, r) => sum + Number(r.Quantity), 0
    );

    const customers = new Set(
        records.map(r => r.Customer_ID)
    ).size;

    const averageOrder = totalOrders > 0
        ? totalRevenue / totalOrders
        : 0;

    document.getElementById("revenue").textContent =
        money(totalRevenue);

    document.getElementById("orders").textContent =
        totalOrders.toLocaleString("en-IN");

    document.getElementById("units").textContent =
        totalUnits.toLocaleString("en-IN");

    document.getElementById("customers").textContent =
        customers.toLocaleString("en-IN");

    document.getElementById("aov").textContent =
        money(averageOrder);
}

// ==========================================
// 8. AGGREGATE DATA
// ==========================================

function aggregate(records, key) {

    const result = {};

    records.forEach(r => {
        const name = r[key];

        result[name] = (result[name] || 0) +
                        Number(r.Revenue);
    });

    return result;
}

// ==========================================
// 9. DRAW CHART
// ==========================================

function drawChart(canvasId, labels, values, type) {

    const canvas = document.getElementById(canvasId);
    const ctx = canvas.getContext("2d");

    const width = canvas.clientWidth;
    const height = canvas.clientHeight;

    canvas.width = width * window.devicePixelRatio;
    canvas.height = height * window.devicePixelRatio;

    ctx.scale(window.devicePixelRatio, window.devicePixelRatio);

    ctx.clearRect(0, 0, width, height);

    const left = 55;
    const right = 15;
    const top = 20;
    const bottom = 85;

    const chartWidth = width - left - right;
    const chartHeight = height - top - bottom;

    const maxValue = Math.max(...values, 1);
    const niceMax = maxValue * 1.15;

    // Grid lines and Y labels

    ctx.font = "11px Arial";
    ctx.fillStyle = "#718096";
    ctx.strokeStyle = "#e8ecf2";
    ctx.lineWidth = 1;

    for (let i = 0; i <= 4; i++) {

        const y = top + chartHeight -
                 (chartHeight * i / 4);

        ctx.beginPath();
        ctx.moveTo(left, y);
        ctx.lineTo(width - right, y);
        ctx.stroke();

        const value = niceMax * i / 4;

        let label;

        if (value >= 1000000) {
            label = (value / 1000000).toFixed(1) + "M";
        } else if (value >= 1000) {
            label = (value / 1000).toFixed(0) + "K";
        } else {
            label = value.toFixed(0);
        }

        ctx.fillText(label, 4, y + 4);
    }

    if (labels.length === 0) {
        ctx.fillStyle = "#777";
        ctx.fillText("No data available", width / 2 - 40, height / 2);
        return;
    }

    // LINE CHART

    if (type === "line") {

        const stepX = labels.length > 1
            ? chartWidth / (labels.length - 1)
            : chartWidth / 2;

        ctx.beginPath();
        ctx.strokeStyle = "#4267c8";
        ctx.lineWidth = 3;

        values.forEach((value, i) => {

            const x = labels.length > 1
                ? left + i * stepX
                : left + chartWidth / 2;

            const y = top + chartHeight -
                (value / niceMax) * chartHeight;

            if (i === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        });

        ctx.stroke();

        values.forEach((value, i) => {

            const x = labels.length > 1
                ? left + i * stepX
                : left + chartWidth / 2;

            const y = top + chartHeight -
                (value / niceMax) * chartHeight;

            ctx.beginPath();
            ctx.arc(x, y, 4, 0, Math.PI * 2);
            ctx.fillStyle = "#4267c8";
            ctx.fill();

            ctx.fillStyle = "#53627d";
            ctx.textAlign = "center";
            ctx.fillText(labels[i], x, top + chartHeight + 20);
        });

        ctx.textAlign = "left";
        return;
    }

    // BAR CHART

    const slotWidth = chartWidth / labels.length;
    const barWidth = Math.min(slotWidth * 0.65, 45);

    values.forEach((value, i) => {

        const barHeight = (value / niceMax) * chartHeight;

        const x = left + slotWidth * i +
                  (slotWidth - barWidth) / 2;

        const y = top + chartHeight - barHeight;

        ctx.fillStyle = "#4267c8";

        ctx.fillRect(x, y, barWidth, barHeight);

        // Labels

        ctx.save();

        ctx.translate(
            x + barWidth / 2,
            top + chartHeight + 18
        );

        ctx.rotate(-Math.PI / 4);

        ctx.fillStyle = "#58657b";
        ctx.textAlign = "right";
        ctx.font = "10px Arial";

        ctx.fillText(
            String(labels[i]),
            0,
            0
        );

        ctx.restore();
    });

}

// ==========================================
// 10. UPDATE ALL CHARTS
// ==========================================

function updateCharts(records) {

    // Monthly Revenue

    const monthly = aggregate(records, "Month");

    const months = Object.keys(monthly).sort();

    drawChart(
        "monthlyChart",
        months,
        months.map(m => monthly[m]),
        "line"
    );

    // Product Revenue

    const product = aggregate(records, "Product");

    const products = Object.keys(product).sort(
        (a, b) => product[b] - product[a]
    );

    drawChart(
        "productChart",
        products,
        products.map(p => product[p]),
        "bar"
    );

    // Category Revenue

    const category = aggregate(records, "Category");

    const categories = Object.keys(category).sort(
        (a, b) => category[b] - category[a]
    );

    drawChart(
        "categoryChart",
        categories,
        categories.map(c => category[c]),
        "bar"
    );

    // Region Revenue

    const region = aggregate(records, "Region");

    const regions = Object.keys(region).sort(
        (a, b) => region[b] - region[a]
    );

    drawChart(
        "regionChart",
        regions,
        regions.map(r => region[r]),
        "bar"
    );

    // Payment Revenue

    const payment = aggregate(records, "Payment_Method");

    const payments = Object.keys(payment).sort(
        (a, b) => payment[b] - payment[a]
    );

    drawChart(
        "paymentChart",
        payments,
        payments.map(p => payment[p]),
        "bar"
    );
}

// ==========================================
// 11. REFRESH DASHBOARD
// ==========================================

function refreshDashboard() {

    const records = filteredData();

    updateKPIs(records);
    updateCharts(records);
}

// ==========================================
// 12. FILTER EVENTS
// ==========================================

["month", "region", "category", "product", "payment"]
.forEach(id => {

    document.getElementById(id)
        .addEventListener("change", refreshDashboard);

});

// ==========================================
// 13. INITIAL DASHBOARD
// ==========================================

refreshDashboard();

// Redraw when screen size changes

window.addEventListener("resize", refreshDashboard);

</script>

</body>
</html>
'''

# ==========================================
# 3. INSERT DATA INTO HTML
# ==========================================

html = html.replace("DATA_PLACEHOLDER", data_json)

# ==========================================
# 4. SAVE DASHBOARD
# ==========================================

with open("sales_dashboard.html", "w", encoding="utf-8") as file:
    file.write(html)

print("================================")
print("Dashboard created successfully!")
print("File: sales_dashboard.html")
print("Open this HTML file in your browser.")
print("================================")
