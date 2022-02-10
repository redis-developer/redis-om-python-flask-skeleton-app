from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<p>TODO Home Page...</p>"

