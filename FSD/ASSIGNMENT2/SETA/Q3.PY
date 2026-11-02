from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])

        return f"Product of {a} and {b} is {a*b}"

    return '''
    <form method="POST">
        Num 1: <input type="number" name="a">
        Num 2: <input type="number" name="b">
        <input type="submit" value="Product">
    </form>
    '''

app.run(debug=True)