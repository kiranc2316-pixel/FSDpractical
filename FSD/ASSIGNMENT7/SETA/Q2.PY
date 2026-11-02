from flask import Flask ,request, jsonify

app = Flask(__name__)

employee =[ ("Rahul Sharma", "IT", 45000),
        ("Priya Patil", "HR", 40000),
        ("Amit Shrivastav", "Finance", 50000),
        ("Sneha Roy", "Marketing", 42000),
        ("Vikram Varma", "IT", 55000)]


@app.route('/employee',methods=['GET'])
def get_employee():
    return jsonify(employee)
  
@app.route('/addemployee', methods=['POST'])
def add_employee():

    data = request.get_json()

    employee.append(data)

    return jsonify(
        {
            "msg":"Employee added sucessfully",
            "employee":data
        }
    )

if __name__ == '__main__':
    app.run(debug = True)