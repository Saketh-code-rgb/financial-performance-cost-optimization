-- Total Revenue
SELECT SUM(Revenue) AS Total_Revenue
FROM financial_data;

-- Total Cost
SELECT 
    SUM(Marketing_Cost + Operational_Cost + Employee_Cost) AS Total_Cost
FROM financial_data;

-- Net Profit
SELECT 
    SUM(Revenue) - SUM(Marketing_Cost + Operational_Cost + Employee_Cost) AS Net_Profit
FROM financial_data;

-- Profit Margin %
SELECT 
    ROUND(
        (SUM(Revenue) - SUM(Marketing_Cost + Operational_Cost + Employee_Cost)) 
        * 100.0 / SUM(Revenue), 2
    ) AS Profit_Margin_Percentage
FROM financial_data;

-- Department-wise Performance
SELECT 
    Department,
    SUM(Revenue) AS Total_Revenue,
    SUM(Marketing_Cost + Operational_Cost + Employee_Cost) AS Total_Cost,
    SUM(Revenue) - SUM(Marketing_Cost + Operational_Cost + Employee_Cost) AS Profit
FROM financial_data
GROUP BY Department
ORDER BY Profit DESC;

-- Monthly Profit Trend
SELECT 
    Month,
    SUM(Revenue) - SUM(Marketing_Cost + Operational_Cost + Employee_Cost) AS Monthly_Profit
FROM financial_data
GROUP BY Month
ORDER BY Month;
