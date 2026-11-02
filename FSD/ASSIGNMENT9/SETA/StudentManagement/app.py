from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(
        dbname="employee",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert():
    name = request.form['name']
    course = request.form['course']

    con = connect_db()
    cur = con.cursor()

    cur.execute(
        "INSERT INTO Student (Name, Course) VALUES (%s, %s)",
        (name, course)
    )

    con.commit()
    cur.close()
    con.close()

    return "Student Added Successfully! <br><a href='/'>Go Back</a> | <a href='/display'>View Students</a>"

@app.route('/display')
def display():
    con = connect_db()
    cur = con.cursor()

    cur.execute("SELECT * FROM Student ORDER BY Student_ID")
    students = cur.fetchall()

    cur.close()
    con.close()

    return render_template('index.html', students=students)

if __name__ == '__main__':
    con = connect_db()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            Student_ID SERIAL PRIMARY KEY,
            Name VARCHAR(100),
            Course VARCHAR(100)
        )
    """)

    con.commit()
    cur.close()
    con.close()

    app.run(debug=True, use_reloader=False)