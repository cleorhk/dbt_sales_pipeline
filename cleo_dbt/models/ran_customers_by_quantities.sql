-- models/rank_customers_by_quantity.sql

WITH customer_purchases AS (
    SELECT 
        "CustomerID",
        SUM("Quantity") AS total_items_bought
    FROM {{ source('postgres_db', 'sales_data') }}
    GROUP BY "CustomerID"
)

SELECT 
    "CustomerID",
    total_items_bought,
    RANK() OVER (ORDER BY total_items_bought DESC) AS customer_rank
FROM customer_purchases
ORDER BY customer_rank
