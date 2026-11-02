from flask import Flask, render_template, request
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


def create_table():
    con = connect_db()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            Student_ID SERIAL PRIMARY KEY,
            Name VARCHAR(100),
            Course VARCHAR(100),
            Marks INTEGER
        )
    """)
    con.commit()
    cur.close()
    con.close()


@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    con = connect_db()
    cur = con.cursor()

    if request.method == 'POST':
        action = request.form['action']

        if action == 'insert':
            cur.execute(
                "INSERT INTO Student (Name, Course, Marks) VALUES (%s, %s, %s)",
                (request.form['name'], request.form['course'], request.form['marks'])
            )
            message = "Student added successfully"

        elif action == 'update':
            cur.execute(
                "UPDATE Student SET Name=%s, Course=%s, Marks=%s WHERE Student_ID=%s",
                (request.form['name'], request.form['course'],
                 request.form['marks'], request.form['id'])
            )
            message = "Student updated" if cur.rowcount else "Student ID not found"

        elif action == 'delete':
            cur.execute("DELETE FROM Student WHERE Student_ID=%s",
                        (request.form['id'],))
            message = "Student deleted" if cur.rowcount else "Student ID not found"

        con.commit()

    cur.execute("SELECT * FROM Student ORDER BY Student_ID")
    students = cur.fetchall()
    cur.close()
    con.close()

    return render_template("index.html", students=students, message=message)


if __name__ == '__main__':
    create_table()
    app.run(debug=True)