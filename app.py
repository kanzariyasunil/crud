from flask import Flask

app = Flask(__name__)


DB__NAME="postgres"
DB__USER="postgres.aidvzgclcdshlluhttpm"
DB__PASS="ls7ttN0QDKeHhY7y"
DB__HOST="aws-0-us-east-1.pooler.supabase.com"
DB__PORT="6543"

DB__POSTGRES_URL="postgres://postgres.aidvzgclcdshlluhttpm:ls7ttN0QDKeHhY7y@aws-0-us-east-1.pooler.supabase.com:6543/postgres?sslmode=require"

DB__SUPABASE_URL="https://aidvzgclcdshlluhttpm.supabase.co"
DB__SUPABASE_ANON_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFpZHZ6Z2NsY2RzaGxsdWh0dHBtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzUwMzUzODAsImV4cCI6MjA1MDYxMTM4MH0.LC3YWC--TWOpW_HRDDiCFylxKmTUHxoemi04ZYBriuA"
DB__SUPABASE_JWT_SECRET="zjubtmDgw8u6VD1TiVHa+1PUkwddEzNCUZB3ht8cdbcTtSBj65WnDgq2GMHKFTDiyrnlJ3Z1SSna9nfl4xqJOg=="
DB__SUPABASE_SERVICE_ROLE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFpZHZ6Z2NsY2RzaGxsdWh0dHBtIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczNTAzNTM4MCwiZXhwIjoyMDUwNjExMzgwfQ.LBDQWmZEoBN-RuIdeRsLRQjSKGVUb7BNTZT2nHtv6CE"



import psycopg2



# Function to create a connection and cursor
def get_connection():
    try:
        conn = psycopg2.connect(database =DB__NAME,    
                                 user=DB__USER,
                                 password=DB__PASS,
                                 host=DB__HOST,
                                 port=DB__PORT
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

@app.route('/')
def index():
    return "Hiii"

if __name__ == "__main__":
    app.run(debug=True)