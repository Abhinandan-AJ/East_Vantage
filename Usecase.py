import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect('mydatabase.db')

#SQL query
query = """
SELECT c.customer_id, i.item_name, IFNULL(SUM(o.quantity), 0) AS total_quantity
FROM Customer c
JOIN Sales s ON c.customer_id = s.customer_id
JOIN Orders o ON s.sales_id = o.sales_id
JOIN Items i ON o.item_id = i.item_id
WHERE c.age BETWEEN 18 AND 35
GROUP BY c.customer_id, i.item_name
HAVING total_quantity > 0
"""

#Create DataFrame
df = pd.read_sql_query(query, conn)

#Output file to csv
df.to_csv('item_quantities.csv', sep=';', index=False)

# Close the database connection
conn.close()
