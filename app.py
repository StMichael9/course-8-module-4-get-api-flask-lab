from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():
    return "<h1>Welcome<h1>"

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products")
def get_products():
     # Return all products or filter by ?category=
    category_filter = request.args.get("category")
    if category_filter:
        filtered = [p for p in products if p["category"] == category_filter]
        return jsonify(filtered)
    return jsonify(products)

   

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>")
def get_product_by_id(id):
    # Return product by ID or 404
    for p in products:
        if p['id'] == id:
            return jsonify(p)
    return jsonify({"error": "Products not found"}), 404



if __name__ == "__main__":
    app.run(debug=True)
