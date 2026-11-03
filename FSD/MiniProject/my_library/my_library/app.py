from flask import Flask, render_template, flash, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2

app = Flask(__name__)
app.secret_key = "my_secret_key"

def db_connect():
    conn = psycopg2.connect(
        dbname="project",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
    return conn

# Create users and books tables
def create_table():
    conn = db_connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            password VARCHAR(255)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id SERIAL PRIMARY KEY,
            title VARCHAR(100),
            author VARCHAR(100),
            copies INT
        )
    """)

    conn.commit()
    cur.close()
    conn.close()


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]


        if not name or not email or not password:
            flash("Please fill all fields.")
        else:
            conn = db_connect()
            cur = conn.cursor()

            cur.execute("SELECT * FROM users WHERE email = %s", (email,))
            if cur.fetchone():
                flash("This email is already registered.")
            else:
                cur.execute(
                    "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                    (name, email, generate_password_hash(password))
                )
                conn.commit()
                cur.close()
                conn.close()
                flash("Registered successfully! Please login.")
                return redirect(url_for("login"))

            cur.close()
            conn.close()

    return render_template("registration.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        conn = db_connect()
        cur = conn.cursor()
        cur.execute("SELECT name, password FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user and check_password_hash(user[1], password):
            session["name"] = user[0]
            return redirect(url_for("dashboard"))
        else:
            flash("Wrong email or password.")

    return render_template("login.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "name" not in session:
        return redirect(url_for("login"))

    conn = db_connect()
    cur = conn.cursor()

    # add a book
    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        copies = request.form["copies"].strip()

        if not title or not author or not copies:
            flash("Please fill all fields.")
        elif not copies.isdigit():
            flash("Copies must be a number.")
        else:
            cur.execute(
                "INSERT INTO books (title, author, copies) VALUES (%s, %s, %s)",
                (title, author, copies)
            )
            conn.commit()
            flash("Book added successfully!")

    # show all books
    cur.execute("SELECT * FROM books ORDER BY book_id")
    books = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("dashboard.html", name=session["name"], books=books)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
