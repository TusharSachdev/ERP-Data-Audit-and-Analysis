Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
...     'Trusted_Connection=yes;'
... )
...
... # Query 1: Show all invoices
... query_all = "SELECT * FROM Invoices"
... df_all = pd.read_sql(query_all, conn)
... print("All Invoices:")
... print(df_all)
...
... # Query 2: Invoices with missing values
... query_missing = """
... SELECT * FROM Invoices
... WHERE InvoiceDate IS NULL OR Amount IS NULL OR DueDate IS NULL
... """
... df_missing = pd.read_sql(query_missing, conn)
... print("\nMissing Data:")
... print(df_missing)
...
... # Query 3: Overdue unpaid invoices
... query_overdue = """
... SELECT * FROM Invoices
... WHERE Paid = 0 AND DueDate < GETDATE()
... """
... df_overdue = pd.read_sql(query_overdue, conn)
... print("\nOverdue Unpaid Invoices:")
... print(df_overdue)
...
... # Close the connection
... conn.close()
...
<python-input-0>:14: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
All Invoices:
   InvoiceID  CustomerID InvoiceDate  Amount   Paid     DueDate
0          1         101  2025-10-01  1200.0   True  2025-10-10
1          2         102  2025-09-20   500.0  False  2025-09-30
2          3         103        None     NaN  False  2025-10-05
3          4         104  2025-10-05   750.0   True        None
4          5         105  2025-08-15  1000.0  False  2025-09-01
<python-input-0>:23: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.

Missing Data:
   InvoiceID  CustomerID InvoiceDate  Amount   Paid     DueDate
0          3         103        None     NaN  False  2025-10-05
1          4         104  2025-10-05   750.0   True        None
<python-input-0>:32: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.

Overdue Unpaid Invoices:
   InvoiceID  CustomerID InvoiceDate  Amount   Paid     DueDate
0          2         102  2025-09-20   500.0  False  2025-09-30
1          3         103        None     NaN  False  2025-10-05
2          5         105  2025-08-15  1000.0  False  2025-09-01
... # Plot missing data count
... plt.figure(figsize=(8,5))
... sns.barplot(x=missing_counts.index, y=missing_counts.values, palette='viridis')
... plt.title('Count of Missing Values by Column')
... plt.ylabel('Count')
... plt.xlabel('Columns')
... plt.show()
...
... # Overdue unpaid invoices
... query_overdue = """
... SELECT * FROM Invoices
... WHERE Paid = 0 AND DueDate < GETDATE()
... """
... df_overdue = pd.read_sql(query_overdue, conn)
...
... # Plot overdue invoices count
... plt.figure(figsize=(5,4))
... plt.bar(['Overdue Unpaid Invoices'], [len(df_overdue)], color='red')
... plt.title('Count of Overdue Unpaid Invoices')
... plt.show()
...
... # Paid vs unpaid invoices pie chart
... paid_counts = df_all['Paid'].value_counts()
... plt.figure(figsize=(6,6))
... plt.pie(paid_counts, labels=['Unpaid', 'Paid'], autopct='%1.1f%%', startangle=90, colors=['tomato', 'lightgreen'])
... plt.title('Paid vs Unpaid Invoices')
... plt.show()
...
... conn.close()
...
Traceback (most recent call last):
  File "<python-input-1>", line 4, in <module>
    import seaborn as sns
ModuleNotFoundError: No module named 'seaborn'
>>> python -m pip install matplotlib seaborn pandas pyodbc
  File "<python-input-2>", line 1
    python -m pip install matplotlib seaborn pandas pyodbc
              ^^^
SyntaxError: invalid syntax
... # Plot missing data count
... plt.figure(figsize=(8,5))
... sns.barplot(x=missing_counts.index, y=missing_counts.values, palette='viridis')
... plt.title('Count of Missing Values by Column')
... plt.ylabel('Count')
... plt.xlabel('Columns')
... plt.show()
...
... # Overdue unpaid invoices
... query_overdue = """
... SELECT * FROM Invoices
... WHERE Paid = 0 AND DueDate < GETDATE()
... """
... df_overdue = pd.read_sql(query_overdue, conn)
...
... # Plot overdue invoices count
... plt.figure(figsize=(5,4))
... plt.bar(['Overdue Unpaid Invoices'], [len(df_overdue)], color='red')
... plt.title('Count of Overdue Unpaid Invoices')
... plt.show()
...
... # Paid vs unpaid invoices pie chart
... paid_counts = df_all['Paid'].value_counts()
... plt.figure(figsize=(6,6))
... plt.pie(paid_counts, labels=['Unpaid', 'Paid'], autopct='%1.1f%%', startangle=90, colors=['tomato', 'lightgreen'])
... plt.title('Paid vs Unpaid Invoices')
... plt.show()
...
... conn.close()
...
<python-input-3>:16: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
<python-input-3>:23: FutureWarning:

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.

<python-input-3>:34: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
>>> # Export dataframes to CSV files
... df_all.to_csv('all_invoices.csv', index=False)
... df_missing.to_csv('missing_data.csv', index=False)
... df_overdue.to_csv('overdue_unpaid_invoices.csv', index=False)
... df_per_customer.to_csv('invoices_per_customer.csv', index=False)
... df_avg_amount.to_csv('average_invoice_amount.csv', index=False)
... df_paid_pct.to_csv('paid_vs_unpaid_percentage.csv', index=False)
...
... print("Exported dataframes to CSV files.")
...
Traceback (most recent call last):
  File "<python-input-4>", line 5, in <module>
    df_per_customer.to_csv('invoices_per_customer.csv', index=False)
    ^^^^^^^^^^^^^^^
NameError: name 'df_per_customer' is not defined
>>> # Count of invoices per customer
... query_per_customer = """
... SELECT CustomerID, COUNT(*) AS InvoiceCount
... FROM Invoices
... GROUP BY CustomerID
... ORDER BY InvoiceCount DESC
... """
... df_per_customer = pd.read_sql(query_per_customer, conn)
...
... # Average invoice amount
... query_avg_amount = "SELECT AVG(Amount) AS AverageAmount FROM Invoices WHERE Amount IS NOT NULL"
... df_avg_amount = pd.read_sql(query_avg_amount, conn)
...
... # Percentage of paid vs unpaid invoices
... query_paid_pct = """
... SELECT
...     Paid,
...     COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Invoices) AS Percent
... FROM Invoices
... GROUP BY Paid
... """
... df_paid_pct = pd.read_sql(query_paid_pct, conn)
...
<python-input-5>:8: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
Traceback (most recent call last):
  File "<python-input-5>", line 8, in <module>
    df_per_customer = pd.read_sql(query_per_customer, conn)
  File "C:\Users\abhis\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\sql.py", line 708, in read_sql
    return pandas_sql.read_query(
           ~~~~~~~~~~~~~~~~~~~~~^
        sql,
        ^^^^
    ...<6 lines>...
        dtype=dtype,
        ^^^^^^^^^^^^
    )
    ^
  File "C:\Users\abhis\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\sql.py", line 2728, in read_query
    cursor = self.execute(sql, params)
  File "C:\Users\abhis\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\sql.py", line 2662, in execute
    cur = self.con.cursor()
pyodbc.ProgrammingError: Attempt to use a closed connection.
...     'DATABASE=ERPDataAudit;'
...     'Trusted_Connection=yes;'
... )
...
... # Your queries here
... query_per_customer = """
... SELECT CustomerID, COUNT(*) AS InvoiceCount
... FROM Invoices
... GROUP BY CustomerID
... ORDER BY InvoiceCount DESC
... """
... df_per_customer = pd.read_sql(query_per_customer, conn)
...
... query_avg_amount = "SELECT AVG(Amount) AS AverageAmount FROM Invoices WHERE Amount IS NOT NULL"
... df_avg_amount = pd.read_sql(query_avg_amount, conn)
...
... query_paid_pct = """
... SELECT
...     Paid,
...     COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Invoices) AS Percent
... FROM Invoices
... GROUP BY Paid
... """
... df_paid_pct = pd.read_sql(query_paid_pct, conn)
...
... # After all queries are done, close connection
... conn.close()
...
... # Now you can use or export df_per_customer, df_avg_amount, df_paid_pct
...
<python-input-6>:19: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
<python-input-6>:22: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
<python-input-6>:31: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
Traceback (most recent call last):
  File "C:\Users\abhis\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\sql.py", line 2664, in execute
    cur.execute(sql, *args)
    ~~~~~~~~~~~^^^^^^^^^^^^
pyodbc.ProgrammingError: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Incorrect syntax near the keyword 'Percent'. (156) (SQLExecDirectW)")

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<python-input-6>", line 31, in <module>
    df_paid_pct = pd.read_sql(query_paid_pct, conn)
  File "C:\Users\abhis\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\sql.py", line 708, in read_sql
    return pandas_sql.read_query(
           ~~~~~~~~~~~~~~~~~~~~~^
        sql,
        ^^^^
    ...<6 lines>...
        dtype=dtype,
        ^^^^^^^^^^^^
    )
    ^
  File "C:\Users\abhis\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\sql.py", line 2728, in read_query
    cursor = self.execute(sql, params)
  File "C:\Users\abhis\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\sql.py", line 2676, in execute
    raise ex from exc
pandas.errors.DatabaseError: Execution failed on sql '
SELECT
    Paid,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Invoices) AS Percent
FROM Invoices
GROUP BY Paid
': ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Incorrect syntax near the keyword 'Percent'. (156) (SQLExecDirectW)")
... df_avg_amount = pd.read_sql(query_avg_amount, conn)
... print("\nAverage Invoice Amount:")
... print(df_avg_amount)
...
... # Percentage of paid vs unpaid invoices (fixed alias escaping)
... query_paid_pct = """
... SELECT
...     Paid,
...     COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Invoices) AS [Percent]
... FROM Invoices
... GROUP BY Paid
... """
... df_paid_pct = pd.read_sql(query_paid_pct, conn)
... print("\nPercentage of Paid vs Unpaid Invoices:")
... print(df_paid_pct)
...
... # Export dataframes to CSV files
... df_all.to_csv('all_invoices.csv', index=False)
... df_missing = df_all[df_all.isnull().any(axis=1)]
... df_missing.to_csv('missing_data.csv', index=False)
... df_overdue.to_csv('overdue_unpaid_invoices.csv', index=False)
... df_per_customer.to_csv('invoices_per_customer.csv', index=False)
... df_avg_amount.to_csv('average_invoice_amount.csv', index=False)
... df_paid_pct.to_csv('paid_vs_unpaid_percentage.csv', index=False)
...
... print("\nExported dataframes to CSV files.")
...
... # Close connection
... conn.close()
...
<python-input-7>:16: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
<python-input-7>:23: FutureWarning:

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.

<python-input-7>:34: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
<python-input-7>:58: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.

Invoices per Customer:
   CustomerID  InvoiceCount
0         101             1
1         102             1
2         103             1
3         104             1
4         105             1
<python-input-7>:64: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.

Average Invoice Amount:
   AverageAmount
0          862.5
<python-input-7>:76: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.

Percentage of Paid vs Unpaid Invoices:
    Paid  Percent
0  False     60.0
1   True     40.0

Exported dataframes to CSV files.
>>> import os
... print(os.getcwd())
...
C:\Users\abhis\AppData\Local\Programs\Python\Python314
>>>