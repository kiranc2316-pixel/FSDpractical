

from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )

@app.route('/')
def home():
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
    cur.execute("SELECT * FROM Student ORDER BY Student_ID")
    students = cur.fetchall()

    cur.close()
    con.close()

    return render_template("index.html", students=students)


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

    return redirect('/')


@app.route('/update/<int:student_id>', methods=['POST'])
def update(student_id):
    course = request.form['course']

    con = connect_db()
    cur = con.cursor()

    cur.execute(
        "UPDATE Student SET Course = %s WHERE Student_ID = %s",
        (course, student_id)
    )

    con.commit()
    cur.close()
    con.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
