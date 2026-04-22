from flask import Flask, request, jsonify
from .inventory import inventory      # fixed import
from .services import fetch_product_data  # fixed import

app = Flask(__name__)

# GET all items
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

# GET single item
@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# POST new item
@app.route('/inventory', methods=['POST'])
def add_item():
    data = request.json

    new_item = {
        "id": len(inventory) + 1,
        "name": data.get("name"),
        "brand": data.get("brand", ""),
        "price": data.get("price"),
        "stock": data.get("stock")
    }

    inventory.append(new_item)
    return jsonify(new_item), 201

# PATCH update item
@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    data = request.json
    item = next((i for i in inventory if i["id"] == item_id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    item.update(data)
    return jsonify(item)

@app.route("/")
def home():
    return "Inventory API running! Use /inventory to view items."

# DELETE item
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global inventory
    inventory[:] = [i for i in inventory if i["id"] != item_id]
    return jsonify({"message": "Item deleted"})

# FETCH from OpenFoodFacts
@app.route('/fetch-product', methods=['GET'])
def fetch_product():
    barcode = request.args.get("barcode")
    if not barcode:
        return jsonify({"error": "Barcode required"}), 400

    product = fetch_product_data(barcode)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    new_item = {
        "id": len(inventory) + 1,
        "name": product["name"],
        "brand": product["brand"],
        "price": 0,
        "stock": 0
    }

    inventory.append(new_item)
    return jsonify(new_item)

if __name__ == "__main__":
    app.run(debug=True)