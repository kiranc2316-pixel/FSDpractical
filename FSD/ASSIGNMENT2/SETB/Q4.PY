from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'Kiran' and password == '1234':
            return "Login Successful"
        else:
            return "Invalid Details"

    return '''
    <form method="POST">
        Username: <input type="text" name="username" required><br><br>
        Password: <input type="password" name="password" required><br><br>
        <input type="submit" value="Login">
    </form>
    '''

app.run(debug=True)