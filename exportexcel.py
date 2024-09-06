import pandas as pd
from sqlalchemy import create_engine

# Define your PostgreSQL connection parameters
db_config = {
    'host': 'localhost',
    'port': '5432',  # Default PostgreSQL port
    'database': 'sales',
    'user': 'postgres',
    'password': 'cleo2030'
}

# Create SQLAlchemy engine for PostgreSQL
engine = create_engine(f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

# SQL query to fetch data from your dbt model/view
query = "SELECT * FROM public.salesrep_ranking;"  # Replace with your dbt model or view name

# Load data into a pandas DataFrame using the engine
df = pd.read_sql(query, engine)

# Export the DataFrame to a CSV file
df.to_csv('salesrep_ranking.csv', index=False)

# Export the DataFrame to an Excel file
df.to_excel('salesrep_ranking.xlsx', index=False)

print("Data has been exported successfully to 'salesrep_ranking.csv' and 'salesrep_ranking.xlsx'.")
