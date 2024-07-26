import requests

def get_all_categories():
    response = requests.get('https://fakestoreapi.com/products/categories')
    if response.status_code == 200:
        products = response.json()
        return products

def get_specific_category(category_id):
    response = requests.get(f'https://fakestoreapi.com/products/category/{category_id}')
    if response.status_code == 200:
        product = response.json()
        return product