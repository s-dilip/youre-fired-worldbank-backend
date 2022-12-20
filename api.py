from flask import Flask, current_app, request

app=Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return 'Hello World'

@app.route("/draftpull", methods=['GET'])
def index():
    return 'Draft Pull Request'
