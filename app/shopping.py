import datetime 

TAX_RATE = 0.0875

def to_usd(price):
    """
    Converts a number into a formatted price with dollar sign, two decimal places, and thousand separators

    Params:
        price: the number to be formatted

    Example:
        to_usd(3.1)
    """
    return "${0:,.2f}".format(price)

def human_friendly_timestamp(current_datetime):
    """
    Converts a complicated datetime value into a more legible format 

    Params:
        current_datetime: the date and time to be formatted

    Example:
        human_friendly_timestamp(datetime.datetime.now())
    """
    return str(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

def find_product(products, product_id):
    """
    Finds a product in dictionary given a certain product ID

    Params:
        products: all products in dictionary
        product_id: product ID of product to find in dictionary 

    Example:
        find_product(products, 3)
    """
    matching_products = [product for product in products if str(product["id"]) == str(product_id)]
    return matching_products[0]

def calculate_total_price(subtotal):
    """
    Calculates total price given a tax rate andf subtotal (tax rate is constant in this case)

    Params:
        subtotal: the subtotal of all orders before applying tax rate

    Example:
        calculate_total_price(21.99)
    """
    tax_expense = subtotal * TAX_RATE
    return subtotal + tax_expense


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per_pound": 0},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per_pound": 0},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per_pound": 0},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per_pound": 0},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per_pound": 0},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per_pound": 0},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per_pound": 0},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per_pound": 0},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per_pound": 0},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per_pound": 0},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per_pound": 0},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per_pound": 0},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per_pound": 0},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per_pound": 0},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per_pound": 0},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per_pound": 0},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per_pound": 0},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per_pound": 0},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per_pound": 0},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per_pound": 0}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

product_id_list = []
valid_ids = [str(p["id"]) for p in products]
total_price = tax_expense = subtotal = 0
divider = "------------------------------"
error_message = "Invalid entry. Please try again."
store_name = "PYTHON GROCERIES"
web_address = "www.pythongroceries.com"
phone = "+1(202)763-2634"
thank_you_note = "Thank you for choosing Python Groceries! Please come again soon."

if __name__ == "__main__":
    while True:
        match = False
        product_id = input("Please input a product identifier: ")  #entering product IDs
        product_id = product_id.lower().title() 
        if product_id == "Done": #break when done
            break
        elif product_id not in valid_ids: 
            print(error_message)
        else:
            product_id_list.append(int(product_id))
            
    print(divider)
    print(store_name)
    print(divider)
    print("Web: " + web_address)
    print("Phone: " + phone)
    print("Checkout Time: " + human_friendly_timestamp(datetime.datetime.now())) # https://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component
    print(divider)
    print("Shopping Cart Items: ")

    for product_id in product_id_list: 
        matching_product = find_product(products, product_id)
        subtotal = subtotal + matching_product["price"]
        item_price = "(" + to_usd(matching_product["price"]) + ")"
        print(" + " + matching_product["name"] + " " + item_price)
    

    print(divider)
    
    total_price = calculate_total_price(subtotal)

    print("SUBTOTAL: " + to_usd(subtotal))
    print("Plus NYC Sales Tax (8.75%): " + to_usd(tax_expense))
    print("TOTAL PRICE: " + to_usd(total_price))
    print(divider)
    print(thank_you_note)
    print(divider)
















