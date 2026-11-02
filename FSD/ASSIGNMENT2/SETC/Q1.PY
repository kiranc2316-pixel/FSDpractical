from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        name = request.form['name']
        return f"Student Name: {name}"

    return '''
    <form method="POST">
        Name: <input type="text" name="name" required><br><br>
        <input type="submit" value="Submit">
    </form>
    '''

app.run(debug=True)