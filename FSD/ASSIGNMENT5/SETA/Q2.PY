
from flask import Flask, request

app = Flask(__name__)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        num1 = int(request.form.get("num1"))
        num2 = int(request.form.get("num2"))
        total = num1 + num2
        return f"The sum is: {total}"

    return '''
        <form method="post">
            Enter first number: <input type="number" name="num1"><br><br>
            Enter second number: <input type="number" name="num2"><br><br>
            <input type="submit" value="Add">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
