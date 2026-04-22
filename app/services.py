import requests

def fetch_product_data(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] == 1:
            product = data["product"]
            return {
                "name": product.get("product_name"),
                "brand": product.get("brands"),
                "ingredients": product.get("ingredients_text")
            }
        else:
            return None
    except Exception:
        return None