import sys
import os

# Adicione o diretório raiz ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.schema import Customers_Schemas
import json

with open("data/customers_data.json", "r") as file:
    data = json.load(file)

customer = Customers_Schemas(**data)

if customer is not None:
    print("Schema Validation OK")