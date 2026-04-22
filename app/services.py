import requests

OPENFOODFACTS_URL = "https://world.openfoodfacts.org/api/v0/product/{barcode}.json"


def fetch_product_from_api(barcode):
    """
    Fetch product info from OpenFoodFacts API using barcode.
    Returns a clean dict or None if not found / blocked.
    """

    headers = {
        "User-Agent": "InventorySystem/1.0 (student project)"
    }

    try:
        response = requests.get(
            OPENFOODFACTS_URL.format(barcode=barcode),
            headers=headers,
            timeout=5
        )

        # If API blocks request or fails
        if response.status_code != 200:
            print("HTTP ERROR:", response.status_code)
            return None

        try:
            data = response.json()
        except Exception as e:
            print("JSON ERROR:", e)
            return None

        # Validate API response
        if not isinstance(data, dict):
            return None

        if data.get("status") != 1:
            return None

        product = data.get("product")
        if not product:
            return None

        return {
            "barcode": barcode,
            "name": product.get("product_name", "Unknown"),
            "brand": product.get("brands", "Unknown"),
            "category": product.get("categories", "Unknown"),
            "quantity": product.get("quantity", "Unknown"),
            "ingredients": product.get("ingredients_text", "Not available"),
            "nutrition_grade": product.get("nutrition_grades", "Unknown")
        }

    except requests.exceptions.RequestException as e:
        print("REQUEST ERROR:", e)
        return None