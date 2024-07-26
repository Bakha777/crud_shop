import requests

def get_all_categories():
    response = requests.get('https://fakestoreapi.com/products/categories')
    if response.status_code == 200:
        categories = response.json()
        return categories

def get_specific_category(category_name):
    response = requests.get(f'https://fakestoreapi.com/products/category/{category_name}')
    if response.status_code == 200:
        product = response.json()
        return products