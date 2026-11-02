from flask import Flask

app = Flask(__name__)

@app.route('/')
def employee_list():

    employees = [
        ("alex", "IT", 45000),
        ("john", "HR", 40000),
        ("pitter", "Finance", 50000),
        ("hennry", "Marketing", 42000),
        ("vian", "IT", 55000)
    ]

    result = "<h2>Employee Details</h2>"

    for name, department, salary in employees:
        result += f"""
            Name  : {name}<br>
            Department : {department}<br>
            Salary : ₹{salary}<br><br>
        """
    return result

if __name__ == "__main__":
    app.run(debug=True)