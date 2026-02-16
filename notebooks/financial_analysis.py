import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/financial_data.csv")

# Create Total Cost column
df['Total_Cost'] = df['Marketing_Cost'] + df['Operational_Cost'] + df['Employee_Cost']

# KPIs
total_revenue = df['Revenue'].sum()
total_cost = df['Total_Cost'].sum()
net_profit = total_revenue - total_cost
profit_margin = (net_profit / total_revenue) * 100

print("Total Revenue:", total_revenue)
print("Total Cost:", total_cost)
print("Net Profit:", net_profit)
print("Profit Margin %:", round(profit_margin, 2))

# Department-wise Profit
dept_profit = df.groupby('Department').apply(
    lambda x: x['Revenue'].sum() - x['Total_Cost'].sum()
)

dept_profit.plot(kind='bar')
plt.title("Department-wise Profit")
plt.ylabel("Profit")
plt.show()

# Monthly Profit Trend
monthly_profit = df.groupby('Month').apply(
    lambda x: x['Revenue'].sum() - x['Total_Cost'].sum()
)

monthly_profit.plot(kind='line')
plt.title("Monthly Profit Trend")
plt.ylabel("Profit")
plt.show()

# Cost Breakdown
cost_breakdown = df.groupby('Department')[['Marketing_Cost','Operational_Cost','Employee_Cost']].sum()
cost_breakdown.plot(kind='bar', stacked=True)
plt.title("Cost Breakdown by Department")
plt.ylabel("Cost")
plt.show()
