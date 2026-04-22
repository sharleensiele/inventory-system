from app.inventory import (
    get_all_items,
    add_item,
    update_item,
    delete_item
)


def test_add_item():
    item = add_item({"name": "TestItem"})
    assert item["name"] == "TestItem"


def test_get_all_items():
    items = get_all_items()
    assert isinstance(items, list)


def test_update_item():
    item = add_item({"name": "UpdateMe"})
    updated = update_item(item["id"], {"name": "Updated"})
    assert updated["name"] == "Updated"


def test_delete_item():
    item = add_item({"name": "DeleteMe"})
    result = delete_item(item["id"])
    assert result is True