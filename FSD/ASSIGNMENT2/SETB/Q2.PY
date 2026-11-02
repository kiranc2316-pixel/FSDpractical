from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        studentname = request.form['studentname']
        return f"Student Name: {studentname}"

    return '''
    <form method="POST">
        Student Name: <input type="text" name="studentname">
        <input type="submit" value="Submit">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)