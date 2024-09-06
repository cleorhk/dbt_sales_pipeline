# dbt Sales Pipeline

This project loads sales data into a PostgreSQL database and uses dbt to transform the data.

## Prerequisites

- Python 3.x
- PostgreSQL
- dbt

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/<username>/dbt_sales_pipeline.git
    ```

2. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your PostgreSQL database and update the connection details in `load_data_to_postgres.py`.

4. Load data from CSV to PostgreSQL:

    ```bash
    python load_data_to_postgres.py
    ```

5. Navigate to the dbt project folder and run the dbt models:

    ```bash
    cd my_dbt_project
    dbt run
    ```

## Models

- **transform_sales_data**: Cleans and transforms the sales data.
- **rank_customers_by_quantity**: Ranks customers based on the quantity of items purchased.
- **rank_regions_by_sales**: Ranks regions based on the number of sales.
