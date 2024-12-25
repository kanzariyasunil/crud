import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Function to create a connection
def get_connection():
    conn_params = {
        "dbname": "postgres",
        "user": "postgres.zleiplxecgllndvtfeln",
        "password": "0vNtq1jP2rjzHZuz",
        "host": "aws-0-ap-south-1.pooler.supabase.com",
        "port": 6543,
        "sslmode": "require"
    }
    try:
        # Establish a connection using individual parameters
        conn = psycopg2.connect(**conn_params)
        return conn
    except Exception as e:
        print(f"An error occurred while connecting: {e}")
        return None

# Function to execute a query
def make_db_call(query, returns=False, parameters=None):
    conn = get_connection()
    if conn is None:
        print("Failed to get a database connection.")
        return None

    try:
        with conn.cursor() as cur:
            # Execute the query with parameters if provided
            if parameters:
                cur.execute(query, parameters)
            else:
                cur.execute(query)
            
            # If the query expects results (e.g., SELECT)
            if returns:
                return cur.fetchall()
            else:
                conn.commit()  # Commit for non-SELECT queries
    except Exception as e:
        conn.rollback()  # Rollback in case of error
        print("Error executing query:", e)
        return None
    finally:
        if conn:
            conn.close() 