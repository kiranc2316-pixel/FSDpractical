from flask import Flask

app = Flask(__name__)

@app.route("/")
def employee_list():

    employees = [
        ("Riyansh", "IT", 45000),
        ("aditya", "HR", 40000),
        ("Shrivastav", "Finance", 50000),
        ("avinash", "Marketing", 42000),
        ("Vikram ", "IT", 55000)
    ]

    employee_details = ""

    for name, department, salary in employees:
        employee_details += f"""
        <p>
            Name: {name}<br>
            Department: {department}<br>
            Salary: ₹{salary}
        </p>
        <hr>
        """

    return f"""
    <h2>List of Employees</h2>
    {employee_details}
    """

if __name__ == "__main__":
    app.run(debug=True)