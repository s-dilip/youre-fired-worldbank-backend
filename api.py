import json
import psycopg2
import psycopg2.extras as pse  # We'll need this to convert SQL responses into dictionaries
from flask import Flask, current_app, request, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def index():
    return 'Countries Application'

@app.route("/countries/<string:name>", methods=['GET'])
def get_countries(name):
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=pse.RealDictCursor)

        cur.execute("SELECT * from countries WHERE LOWER(shortname)= %s", [name])

        countries_data = cur.fetchall()
        cur.close()

        if (len(countries_data)<1):
            return 'No Country Found with such name', 404
        else:
            return countries_data, 200, {'Content-Type': 'application/json'}

    except:
        return 'Failed to fetch Data', 404


def get_db_connection():
    try:
        conn = psycopg2.connect("dbname=czreijar user=czreijar password=TJ2StTuQIl2CoRoinQTwPxk8pBGfdf6t host=kandula.db.elephantsql.com port=5432")
        return conn
    except:
        print('Error Connecting to Database')

    