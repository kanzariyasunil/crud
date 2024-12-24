import psycopg2
from dotenv import load_dotenv
load_dotenv()
import os


# Function to create a connection and cursor
def get_connection():
    try:
        conn = psycopg2.connect(database =os.getenv("DB_NAME"),    
                                 user=os.getenv("DB_USER"),
                                 password=os.getenv("DB_PASS"),
                                 host=os.getenv("DB_HOST"),
                                 port=os.getenv("DB_PORT")
                                 )
        return conn
    except Exception as e:
        print("Your database is not connected:", e)
        return None

# Function to make a database call (query execution)
def make_db_call(query, returns=None, parameter=None):
    conn = get_connection()
    if conn is None:
        return None

    try:
        with conn.cursor() as cur:  # Use 'with' for automatic cursor management
            cur.execute(query, parameter)

            if returns:
                return cur.fetchall()
            else:
                conn.commit()  # For non-SELECT queries
    except Exception as e:
        conn.rollback()  # Rollback in case of error
        print("Error executing query:", e)
    finally:
        if conn:
            conn.close()  # Ensure connection is closed

