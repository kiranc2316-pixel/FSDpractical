from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(
        dbname="employeedb",
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
    department = request.form['department']

    con = connect_db()
    cur = con.cursor()

    cur.execute(
        "INSERT INTO Employee (Name, Department) VALUES (%s, %s)",
        (name, department)
    )

    con.commit()
    cur.close()
    con.close()

    return "Employee Added Successfully! <a href='/'>Go Back</a>"

@app.route('/display')
def display():
    con = connect_db()
    cur = con.cursor()

    cur.execute("SELECT * FROM Employee ORDER BY Emp_ID")
    employees = cur.fetchall()

    cur.close()
    con.close()

    return render_template('index.html', employees=employees)

if __name__ == '__main__':
    con = connect_db()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Employee (
            Emp_ID SERIAL PRIMARY KEY,
            Name VARCHAR(100),
            Department VARCHAR(100)
        )
    """)

    con.commit()
    cur.close()
    con.close()

    app.run(debug=True, use_reloader=False)