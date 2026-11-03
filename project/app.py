from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)


# Connect to database
def db_connect():
    return psycopg2.connect(
        dbname="gymdb",
        user="postgres",
        password="your_password",
        host="localhost",
        port="5432"
    )


# Create Users table
def create_table():
    con = db_connect()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            User_ID SERIAL PRIMARY KEY,
            Full_Name VARCHAR(100),
            Email VARCHAR(100),
            Phone VARCHAR(20),
            Password VARCHAR(100)
        )
    """)
    con.commit()
    cur.close()
    con.close()


# Login
@app.route("/", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        con = db_connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM Users WHERE Email = %s AND Password = %s", (email, password))
        user = cur.fetchone()
        cur.close()
        con.close()

        if user:
            return redirect("/dashboard")
        error = "Invalid email or password."

    return render_template("index.html", error=error)


# Registration
@app.route("/register", methods=["GET", "POST"])
def register():
    error = ""

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]

        con = db_connect()
        cur = con.cursor()

        cur.execute("SELECT * FROM Users WHERE Email = %s", (email,))
        if cur.fetchone():
            error = "This email is already registered."
        else:
            cur.execute(
                "INSERT INTO Users (Full_Name, Email, Phone, Password) VALUES (%s, %s, %s, %s)",
                (name, email, phone, password)
            )
            con.commit()

        cur.close()
        con.close()

        if error == "":
            return redirect("/")

    return render_template("register.html", error=error)


# Dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    create_table()
    app.run(debug=True)