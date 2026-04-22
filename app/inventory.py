import json
import os

# -----------------------------
# JSON FILE PATH
# -----------------------------
DATA_FILE = os.path.join(os.path.dirname(__file__), "inventory.json")


# -----------------------------
# LOAD DATA
# -----------------------------
def load_inventory():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        return json.load(f)


# -----------------------------
# SAVE DATA
# -----------------------------
def save_inventory(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


# -----------------------------
# GET ALL ITEMS
# -----------------------------
def get_all_items():
    return load_inventory()


# -----------------------------
# GET ONE ITEM
# -----------------------------
def get_item(item_id):
    inventory = load_inventory()
    return next((item for item in inventory if item["id"] == item_id), None)


# -----------------------------
# ADD ITEM
# -----------------------------
def add_item(item):
    inventory = load_inventory()

    new_id = max([i["id"] for i in inventory], default=0) + 1
    item["id"] = new_id

    inventory.append(item)
    save_inventory(inventory)

    return item


# -----------------------------
# UPDATE ITEM
# -----------------------------
def update_item(item_id, data):
    inventory = load_inventory()

    for item in inventory:
        if item["id"] == item_id:
            item.update(data)
            save_inventory(inventory)
            return item

    return None


# -----------------------------
# DELETE ITEM
# -----------------------------
def delete_item(item_id):
    inventory = load_inventory()

    new_inventory = [item for item in inventory if item["id"] != item_id]

    if len(new_inventory) == len(inventory):
        return False

    save_inventory(new_inventory)
    return True