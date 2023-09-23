import requests
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'cart.sqlite') 

db = SQLAlchemy(app)

def get_all_products():
    response = requests.get('https://rest-assignment-2.onrender.com/products')
    data = response.json()
    return data

def get_product(product_id):
    response = requests.get(https://rest-assignment-2.onrender.com/products/{product_id}')
    data = response.json()
    return data

def add_product_to_cart(user_id, product_id, quantity):
    endpoint = https://rest-assignment-2.onrender.com/cart/{user_id}/add/{product_id}'
    data = {"quantity": quantity}
    response = requests.post(endpoint, json=data)
    return response.status_code

def remove_product_from_cart(user_id, product_id, quantity):
    endpoint = https://rest-assignment-2.onrender.com/cart/{user_id}/remove/{product_id}'
    data = {"quantity": quantity}
    response = requests.post(endpoint, json=data)
    return response.status_code

if __name__ == '__main__':
    all_products = get_all_products()
    print("All Products:")
    print(all_products)

    product_id = 2
    specific_product = get_product(product_id)
    print(f"\nProduct {product_id}:")
    print(specific_product)

    user_id = 1
    product_id_to_add = 3
    quantity_to_add = 2
    add_result = add_product_to_cart(user_id, product_id_to_add, quantity_to_add)
    if add_result == 200:
        print(f"\nAdded {quantity_to_add} of Product {product_id_to_add} to the cart for User {user_id}")
    else:
        print("Failed to add the product to the cart")

    product_id_to_remove = 4
    quantity_to_remove = 1
    remove_result = remove_product_from_cart(user_id, product_id_to_remove, quantity_to_remove)
    if remove_result == 200:
        print(f"\nRemoved {quantity_to_remove} of Product {product_id_to_remove} from the cart for User {user_id}")
    else:
        print("Failed to remove the product from the cart")
        
if __name__ == '__main__':
   
