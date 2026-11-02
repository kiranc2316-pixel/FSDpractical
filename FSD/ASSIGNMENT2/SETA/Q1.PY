from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/students', methods=['GET'])
def get_students():
    students = [
        {"id": 1, "name": "Kiran", "course": "BSc IT"},
        {"id": 2, "name": "Gayatri", "course": "BSc IT"}
    ]
    return jsonify(students)

app.run(debug=True)