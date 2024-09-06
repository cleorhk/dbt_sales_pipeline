-- models/rank_regions_by_sales.sql

WITH region_sales AS (
    SELECT 
        "Region",
        COUNT("OrderID") AS total_sales
    FROM {{ source('postgres_db', 'sales_data') }}
    GROUP BY "Region"
)

SELECT 
    "Region",
    total_sales,
    RANK() OVER (ORDER BY total_sales DESC) AS sales_rank
FROM region_sales
ORDER BY sales_rank
