import requests

BASE_URL = "http://127.0.0.1:5000"

def menu():
    print("\n--- Inventory System ---")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Fetch Product (API)")
    print("6. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        res = requests.get(f"{BASE_URL}/inventory")
        print(res.json())

    elif choice == "2":
        name = input("Name: ")
        brand = input("Brand: ")
        price = int(input("Price: "))
        stock = int(input("Stock: "))

        res = requests.post(f"{BASE_URL}/inventory", json={
            "name": name,
            "brand": brand,
            "price": price,
            "stock": stock
        })
        print(res.json())

    elif choice == "3":
        item_id = input("Item ID: ")
        price = input("New Price: ")
        stock = input("New Stock: ")

        res = requests.patch(f"{BASE_URL}/inventory/{item_id}", json={
            "price": int(price),
            "stock": int(stock)
        })
        print(res.json())

    elif choice == "4":
        item_id = input("Item ID: ")
        res = requests.delete(f"{BASE_URL}/inventory/{item_id}")
        print(res.json())

    elif choice == "5":
        barcode = input("Enter barcode: ")
        res = requests.get(f"{BASE_URL}/fetch-product?barcode={barcode}")
        print(res.json())

    elif choice == "6":
        break

    else:
        print("Invalid choice")