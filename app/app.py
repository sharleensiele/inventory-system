from flask import Flask, jsonify, request

from app.inventory import (
    get_all_items,
    get_item,
    add_item,
    update_item,
    delete_item
)

from app.services import fetch_product_from_api


app = Flask(__name__)


# -----------------------------
# HOME
# -----------------------------
@app.route("/")
def home():
    return jsonify({"message": "Inventory API Running"})


# -----------------------------
# GET ALL INVENTORY
# -----------------------------
@app.route("/inventory", methods=["GET"])
def inventory():
    return jsonify(get_all_items()), 200


# -----------------------------
# GET SINGLE ITEM
# -----------------------------
@app.route("/inventory/<int:item_id>", methods=["GET"])
def single_item(item_id):
    item = get_item(item_id)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item), 200


# -----------------------------
# ADD ITEM
# -----------------------------
@app.route("/inventory", methods=["POST"])
def create_item():
    data = request.json
    item = add_item(data)
    return jsonify(item), 201


# -----------------------------
# UPDATE ITEM
# -----------------------------
@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_inventory_item(item_id):
    data = request.json
    item = update_item(item_id, data)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item), 200


# -----------------------------
# DELETE ITEM
# -----------------------------
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_inventory_item(item_id):
    success = delete_item(item_id)

    if not success:
        return jsonify({"error": "Item not found"}), 404

    return jsonify({"message": "Item deleted"}), 200


# -----------------------------
# FETCH PRODUCT BY BARCODE
# -----------------------------
@app.route("/product/<barcode>", methods=["GET"])
def fetch_product(barcode):
    result = fetch_product_from_api(barcode)

    print("FINAL RESULT:", result)  # DEBUG

    if result is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(result), 200


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)