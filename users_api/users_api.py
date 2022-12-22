from flask import Flask, request
from users_db_interactions import select, insert
import bcrypt
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/create-account', methods=['POST'])
def set_username_and_password():
    data = request.json
    username = data["username"]
    password = data["password"].encode('utf8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt).decode('utf8')
    query = insert(
        """INSERT INTO users (username, hashed_password) 
        VALUES (%s, %s);""", 
        (username, hashed_password)
        )
    return query


@app.route('/login', methods=['POST'])
def check_username_and_password():
    data = request.json
    username = data["username"]
    query = select(
        """SELECT (hashed_password) FROM users
        WHERE username = %s""",
        (username,)
        )
    entered_password = data["password"].encode('utf8')
    if len(query) > 0:
        hashed_password = query[0][0].encode('utf8')
    if len(query) == 0:
        return jsonify({"status": "No matching user found", "code": 404})
    elif bcrypt.checkpw(entered_password, hashed_password):
        return_data = {"match": True, "status": 'success', "code": 200}
        return jsonify(data)
    else:
        return_data = {"match": False, "status": 'Unauthorised', "code": 400}
        return jsonify(return_data)