from flask import Flask, request

app = Flask(__name__)

books = ["Python", "Java", "HTML", "CSS"]

@app.route('/', methods=['GET', 'POST'])
def search():

    if request.method == 'POST':
        book = request.form['book']

        if book in books:
            return f"Book Found: {book}"
        else:
            return "Book Not Found"

    return '''
    <form method="POST">
        Book Name: <input type="text" name="book" required><br><br>
        <input type="submit" value="Search">
    </form>
    '''

app.run(debug=True)