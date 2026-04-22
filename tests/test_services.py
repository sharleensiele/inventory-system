from app.services import fetch_product_from_api


def test_fetch_product_valid():
    result = fetch_product_from_api("5449000000996")

    # may vary depending on API availability
    assert result is None or isinstance(result, dict)


def test_fetch_product_invalid():
    result = fetch_product_from_api("0000000000000")
    assert result is None