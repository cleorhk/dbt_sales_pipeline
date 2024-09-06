from sqlalchemy import create_engine
import pandas as pd

# Define your connection string
connection_string = "postgresql+psycopg2://postgres:cleo2030@localhost:5432/sales"

# Create an engine
engine = create_engine(connection_string)

# Define the SQL query
query = "SELECT * FROM sales_data WHERE 'Region' = 'West';"

# Execute the query and fetch the data into a DataFrame
df_west = pd.read_sql(query, engine)

# Display the resulting DataFrame
print(df_west)
