import requests

def get_all_cart():
    response = requests.get('https://fakestoreapi.com/carts')
    if response.status_code == 200:
        products = response.json()
        return products

def get_single_product(product_id):
    response = requests.get(f'https://fakestoreapi.com/carts/{product_id}')
    if response.status_code == 200:
        product = response.json()
        return product

def sort_result(desc):
    response = requests.get(f'https://fakestoreapi.com/carts?sort={desc}')
    if response.status_code == 200:
        product = response.json()
        return product
    
def get_limit_result(limit):
    response = requests.get(f'hhttps://fakestoreapi.com/carts?limit={limit}')
    if response.status_code == 200:
        products = response.json()
        return products

def get_users_cart(user_id):
    response = requests.get(f'https://fakestoreapi.com/carts/user/{user_id}')
    if response.status_code == 200:
        products = response.json()
        return products        

def get_carts_in_date_range(date):
    response = requests.get(f'https://fakestoreapi.com/carts?startdate=2019-12-10&enddate={date}')
    if response.status_code == 200:
        products = response.json()
        return products

def add_new_cart(data):
    response = requests.post('https://fakestoreapi.com/carts', data)
    if response.status_code == 200:
        new_product = response.json()
        return new_product
    
def edit_product(product_id, new_data):
    response = requests.patch(f'https://fakestoreapi.com/carts/{product_id}', new_data)
    if response.status_code == 200:
        edited_product = response.json()
        return edited_product
    
def delete_cart(product_id):
    response = requests.delete(f'https://fakestoreapi.com/carts/{product_id}')
    if response.status_code == 200:
        return 'Продукт был успешно удалёен.'