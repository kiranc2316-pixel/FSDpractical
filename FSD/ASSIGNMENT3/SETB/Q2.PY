from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route('/')
def birthday():
    today = date.today()
    return f"Happy Birthday, Kiran! 🎂<br>Today's Date: {today}"

if __name__ == '__main__':
    app.run(debug=True)
