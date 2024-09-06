import pandas as pd
from sqlalchemy import create_engine, text
import psycopg2

# Define database connection parameters
db_config = {
    'host': 'localhost',  # Update with your host
    'port': '5432',       # Update with your port
    'user': 'postgres',   # Update with your PostgreSQL username
    'password': 'cleo2030',  # Update with your PostgreSQL password
    'dbname': 'sales'     # Update with your PostgreSQL database name
}

# Create a connection string
connection_string = f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"

# Create a SQLAlchemy engine
engine = create_engine(connection_string)

# Define the path to the CSV file
csv_file_path = 'sales_data.csv'  # Update with the correct path to your CSV file

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path)

# Define the table name in PostgreSQL
table_name = 'sales_data'

# Create table schema in PostgreSQL
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    OrderID UUID PRIMARY KEY,
    Date DATE,
    CustomerID UUID,
    ProductID VARCHAR(50),
    Quantity INTEGER,
    Price NUMERIC(10, 2),
    SalesRep VARCHAR(100),
    Region VARCHAR(50),
    TotalAmount NUMERIC(10, 2)
);
"""

# Execute the create table query
with engine.connect() as connection:
    connection.execute(text(create_table_query))

# Load data into PostgreSQL
df.to_sql(table_name, engine, if_exists='append', index=False)

print("Data loaded successfully into PostgreSQL!")
