import mysql.connector
import os

def connect_db():
    """
    Connects to MySQL database using environment variables.
    Returns connection object.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASS", "0817"),
            database=os.getenv("DB_NAME", "churn_db")
        )
        return connection
    except mysql.connector.Error as err:
        raise ConnectionError(f"MySQL connection failed: {err}")
