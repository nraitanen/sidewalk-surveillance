"""Serve video stream with Flask"""

from flask import Flask

app = Flask(__name__)

app.route("/", methods = ["GET"])
def index():
    return "Test index route"

@app.route("/stream/start", methods = ["GET"])
def start_stream():
    return "Stream started"