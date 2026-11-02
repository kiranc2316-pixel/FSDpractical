from flask import Flask

app = Flask(__name__)

@app.route("/")
def student_list():

    students = ["avi", "vikram", "dian", "john", "alex"]

    student_names = "<br>".join(students)
    
    return f"""
    <h2>List of Students</h2>
    {student_names}
    """

if __name__ == "__main__":
    app.run(debug=True)