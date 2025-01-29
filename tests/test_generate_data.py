import os
import sys

# Adicione o diretório raiz ao PYTHONPATH
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

import json

from src.schema import Customers_Schemas, Orders_Schemas, Products_Schemas


def test_customers_schema():
    with open('data/customers_data.json', 'r') as file:
        data = json.load(file)

    customer = Customers_Schemas(**data)

    if customer is not None:
        message = print('Schema Validation OK')

    return message


def test_products_schema():
    with open('data/products_data.json', 'r') as file:
        data = json.load(file)

    product = Products_Schemas(**data)

    if product is not None:
        message = print('Schema Validation OK')

    return message


def test_orders_schema():
    with open('data/orders_data.json', 'r') as file:
        data = json.load(file)

    order = Orders_Schemas(**data)

    if order is not None:
        message = print('Schema Validation OK')

    return message
