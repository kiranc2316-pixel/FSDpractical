
from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {"name": "Laptop", "price": 50000, "Category": "Electronic"},
    {"name": "Mobile", "price": 40000, "Category": "Electronic"},
    {"name": "Mackbook", "price": 100000, "Category": "Electronic"}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/addproducts', methods=['POST'])
def add_product():
    data = request.get_json()

    name = data.get("name")
    price = data.get("price")

    product = {
        "name": name,
        "price": price
    }

    products.append(product)

    return jsonify({
        "msg": "Product added successfully",
        "product": product
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
