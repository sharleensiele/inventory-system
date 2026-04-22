import requests


BASE_URL = "http://127.0.0.1:5000"


def main_loop():
    while True:
        print("\n1. View Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Fetch Product (Barcode)")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            r = requests.get(f"{BASE_URL}/inventory")
            print(r.json())

        elif choice == "2":
            name = input("Name: ")
            data = {"name": name}
            r = requests.post(f"{BASE_URL}/inventory", json=data)
            print(r.json())

        elif choice == "3":
            item_id = input("ID: ")
            name = input("New Name: ")
            r = requests.patch(f"{BASE_URL}/inventory/{item_id}", json={"name": name})
            print(r.json())

        elif choice == "4":
            item_id = input("ID: ")
            r = requests.delete(f"{BASE_URL}/inventory/{item_id}")
            print(r.json())

        elif choice == "5":
            barcode = input("Barcode: ")
            r = requests.get(f"{BASE_URL}/product/{barcode}")
            print(r.json())

        elif choice == "6":
            break

        else:
            print("Invalid choice")


# Allow manual run
if __name__ == "__main__":
    main_loop()