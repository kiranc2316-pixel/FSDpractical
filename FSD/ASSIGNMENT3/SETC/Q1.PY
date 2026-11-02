from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Welcome to the Information Technology Department"

app.run(debug=True)