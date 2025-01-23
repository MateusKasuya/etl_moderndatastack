import os
import sys

# Adicione o diretório raiz ao PYTHONPATH
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

import json

from src.schema import Customers_Schemas


def test_customers_schema():
    with open('data/customers_data.json', 'r') as file:
        data = json.load(file)

    customer = Customers_Schemas(**data)

    if customer is not None:
        message = print('Schema Validation OK')

    return message
