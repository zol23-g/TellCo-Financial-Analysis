# db_connection.py
from sqlalchemy import create_engine
import pandas as pd

def get_db_connection(db_config):
    """
    Create a database connection and return the engine.
    """
    db_url = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    engine = create_engine(db_url)
    print("Connection to the database established successfully.")
    return engine

def close_db_connection(engine):
    """
    Close the database connection.
    """
    engine.dispose()
    print("Database connection closed successfully.")

def load_data(query, db_config):
    """
    Load data from the database using the provided query and return a DataFrame.
    """
    engine = get_db_connection(db_config)
    df = pd.read_sql(query, engine)
    close_db_connection(engine)
    return df

# Example usage within the script (optional)
if __name__ == "__main__":
    db_config = {
        'user': 'postgres',
        'password': 'password',
        'host': 'localhost',
        'port': 5432,
        'database': 'tellco_db'
    }
    
    query = "SELECT * FROM xdr_data"
    df = load_data(query, db_config)
    print(df.head())
