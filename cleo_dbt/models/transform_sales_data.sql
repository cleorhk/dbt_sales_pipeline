-- models/transform_sales_data.sql

WITH cleaned_sales_data AS (
    SELECT 
        "OrderID",
        "Date",
        "CustomerID",
        "ProductID",
        "Quantity",
        "Price",
        "SalesRep",
        "Region",
        "TotalAmount",
        -- Example transformation: calculate the total sales per region
        SUM("TotalAmount") OVER (PARTITION BY "Region") AS TotalSalesByRegion
    FROM {{ source('postgres_db', 'sales_data') }}
)

SELECT * FROM cleaned_sales_data
