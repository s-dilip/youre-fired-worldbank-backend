import json
import psycopg2
import psycopg2.extras as pse  # We'll need this to convert SQL responses into dictionaries
from flask import Flask, current_app, request, jsonify

app=Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return 'Hello World'

@app.route("/countries", methods=['GET'])
def get_countries():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=pse.RealDictCursor)

        cur.execute("SELECT shortname from countries")

        countries_data = cur.fetchall()
        # countries = countries_data
        cur.close()

        return countries_data, 200, {'Content-Type': 'application/json'}

    except:
        return 'Failed to fetch Data', 404


def get_db_connection():
    try:
        conn = psycopg2.connect("dbname=czreijar user=czreijar password=TJ2StTuQIl2CoRoinQTwPxk8pBGfdf6t host=kandula.db.elephantsql.com port=5432")
        return conn
    except:
        print('Error Connecting to Database')

    