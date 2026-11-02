from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def feedback():

    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        return f'''
        <h3>Thank you {name}!</h3>
        <p>Your feedback is: {message}</p>
        '''

    return '''
    <form method="POST">
        Name:<br>
        <input type="text" name="name"><br><br>

        Feedback:<br>
        <input type="text" name="message"><br><br>

        <input type="submit" value="Submit">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)