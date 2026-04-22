inventory = []
current_id = 1

def get_item(item_id):
    return next((item for item in inventory if item["id"] == item_id), None)

def add_item(data):
    global current_id
    item = {
        "id": current_id,
        "name": data.get("name"),
        "price": data.get("price"),
        "stock": data.get("stock")
    }
    inventory.append(item)
    current_id += 1
    return item

def update_item(item_id, data):
    item = get_item(item_id)
    if item:
        item.update(data)
        return item
    return None

def delete_item(item_id):
    global inventory
    item = get_item(item_id)
    if item:
        inventory = [i for i in inventory if i["id"] != item_id]
        return True
    return False