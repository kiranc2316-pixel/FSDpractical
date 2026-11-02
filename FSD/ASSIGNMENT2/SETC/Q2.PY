from flask import Flask, request

app = Flask(__name__)

students = ["Kiran", "Gayatri", "Tanuja"]

@app.route('/', methods=['GET', 'POST'])
def search():

    if request.method == 'POST':
        name = request.form['name']

        if name in students:
            return f"Student Found: {name}"
        else:
            return "Student Not Found"

    return '''
    <form method="POST">
        Student Name: <input type="text" name="name" required><br><br>
        <input type="submit" value="Search">
    </form>
    '''

app.run(debug=True)