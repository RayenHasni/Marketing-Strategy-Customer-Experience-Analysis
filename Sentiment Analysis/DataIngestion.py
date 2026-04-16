import pandas as pd
from sqlalchemy import create_engine


def fetch_data_from_sql(server: str, database: str, query: str) -> pd.DataFrame:
    connection_string = f"mssql+pyodbc://{server}/{database}?driver=SQL+Server&trusted_connection=yes"
    engine = create_engine(connection_string)
    
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    
    return df


def fetch_data_from_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)
