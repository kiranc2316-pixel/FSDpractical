
from flask import Flask, request, jsonify

app = Flask(__name__)

student = {
    "name": "Rahul",
    "course": "BSc IT"
}

# GET API
@app.route('/student', methods=['GET'])
def get_student():
    return jsonify(student)

# POST API
@app.route('/addstudent', methods=['POST'])
def add_student():
    data = request.get_json()

    student["name"] = data["name"]
    student["course"] = data["course"]

    return jsonify({
        "message": "Student added successfully",
        "student": student
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
