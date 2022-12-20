from flask import Flask, current_app, request

app=Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return 'Hello World'
