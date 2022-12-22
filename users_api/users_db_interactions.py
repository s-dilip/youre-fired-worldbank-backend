import psycopg2
import psycopg2.extras as pse  # We'll need this to convert SQL responses into dictionaries

def get_db_connection():
  try:
    conn = psycopg2.connect("dbname=users user=louisglanfield host=localhost")
    return conn
  except:
    print("Error connecting to database.")

def insert(query, params=()):
  try:
    conn = get_db_connection()
    with conn.cursor() as cur:
      cur.execute(query, params)
      conn.commit()
    return "Insert completed.", 200
  except:
    conn.close()
    return "Error inserting data", 304

