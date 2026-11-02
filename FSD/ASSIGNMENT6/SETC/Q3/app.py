
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/student_marks")
def student_marks():

    students = {
        "anu":[85,45,87],
        "neha":[45,55,65],
        "Riya": [56,78,67],
        "pyaa": [78,98,67]
    }
    
    results =[]

    for name,marks in students.items():
        total = sum(marks)
        average = total / len(marks)
        highest = max(marks)
        lowest = min(marks)

        results.append({
            "name": name,
            "marks": marks,
            "total": total,
            "average": average,
            "highest": highest,
            "lowest": lowest
        })
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)