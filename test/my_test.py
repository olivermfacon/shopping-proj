import pytest
import datetime
from app.shopping import to_usd, human_friendly_timestamp, find_product, calculate_total_price

def test_to_usd():
    result = to_usd(5)
    assert result == "$5.00"
    result = to_usd(2100.1)
    assert result == "$2,100.10"
    result = to_usd(21.99)
    assert result == "$21.99"

def test_human_friendly_message():
    result = human_friendly_timestamp(datetime.datetime(2020, 4, 15, 14, 19, 11, 609990))
    assert result == "2020-04-15 14:19:11"

def test_find_product():
    products = [
        {"id":4, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per_pound": 0},
        {"id":1, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per_pound": 0},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per_pound": 0},
        {"id":2, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per_pound": 0}
    ]
    product_id = 2
    result = find_product(products, product_id)
    assert result == products[3]

def test_calculate_total_price():
    result = calculate_total_price(100)
    assert result == 108.75

