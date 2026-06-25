import sqlite3
import pandas as pd

def get_results():

    conn = sqlite3.connect("database.db")

    df = pd.read_sql_query(
        "SELECT * FROM interview_results",
        conn
    )

    conn.close()

    return df