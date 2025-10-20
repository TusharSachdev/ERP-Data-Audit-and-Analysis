# ERP Data Audit and Analysis

## Description  
This repository contains SQL and Python scripts designed to audit and analyze invoice data stored in a SQL Server 2022 database. The goal is to provide insights on invoice status, identify data inconsistencies, and support decision-making within an ERP (Enterprise Resource Planning) system.

## Objective  
- Create and manage invoice-related tables in SQL Server 2022  
- Insert sample data reflecting real-world invoice scenarios (paid, unpaid, overdue, missing data)  
- Perform audit queries to identify missing or overdue invoices  
- Visualize key metrics using Python (pandas, matplotlib, seaborn)  
- Export analyzed data for reporting and further use  
- Demonstrate how such audit processes add value to ERP systems by improving data accuracy and financial oversight  

## Tools Used  
- **Microsoft SQL Server 2022** — Database management and querying  
- **Python 3.10+** — Data extraction, analysis, and visualization  
- **pyodbc** — Python ODBC connector for SQL Server  
- **pandas** — Data manipulation  
- **matplotlib** & **seaborn** — Data visualization libraries  
- **Git** and **GitHub** — Version control and repository hosting  

## Data Obtained  
The dataset consists of an `Invoices` table with columns:  
- `InvoiceID` (Primary key)  
- `CustomerID`  
- `InvoiceDate`  
- `Amount`  
- `Paid` (boolean)  
- `DueDate`  

Sample records include various scenarios: fully paid invoices, unpaid invoices, overdue payments, and entries with missing data.

## Data Interpretation  
- Identification of missing or incomplete invoice data to highlight potential data entry issues  
- Counting overdue unpaid invoices to prioritize collection efforts  
- Visualization of paid vs unpaid invoices to monitor cash flow health  
- Calculating average invoice amount and invoice counts per customer for financial analysis  

## Why is this useful for ERP?  
ERP systems rely heavily on accurate and timely financial data. Auditing invoice data helps:  
- Detect errors early, improving data quality  
- Provide actionable insights on payment statuses and customer behavior  
- Support finance and accounting teams with clear, visual reports  
- Enhance overall financial management and operational efficiency  
