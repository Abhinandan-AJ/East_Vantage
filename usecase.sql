.mode csv
.header on
.once item_quantities.csv

SELECT c.customer_id, i.item_name, COALESCE(SUM(o.quantity), 0) AS total_quantity
FROM Customer c
JOIN Sales s ON c.customer_id = s.customer_id
JOIN Orders o ON s.sales_id = o.sales_id
JOIN Items i ON o.item_id = o.item_id
WHERE c.age BETWEEN 18 AND 35
GROUP BY c.customer_id, i.item_name
HAVING total_quantity > 0;
