import json
import psycopg2
import psycopg2.extras  # We'll need this to convert SQL responses into dictionaries
from flask import Flask, current_app, request, jsonify

app=Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return 'Hello World'

@app.route("/countries", methods=['GET'])
def get_countries():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT * from countries")

        countries_data = cur.fetchall()
        cur.close()

        return jsonify(countries_data), 200

    except:
        return 'Failed to fetch Data', 404


def get_db_connection():
    try:
        conn = psycopg2.connect("dbname=czreijar user=czreijar password=TJ2StTuQIl2CoRoinQTwPxk8pBGfdf6t host=kandula.db.elephantsql.com port=5432")
        return conn
    except:
        print('Error Connecting to Database')

    