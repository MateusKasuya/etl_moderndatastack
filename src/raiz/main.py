import json

from database import get_engine_from_settings
from load import load_to_database
from models import Base, Customer, Order, Product
from sqlalchemy import insert
from sqlalchemy.orm import Session


def main():

    engine = get_engine_from_settings()

    Base.metadata.create_all(engine)

    # Customers
    customer_json_file = 'customers_data.json'
    customer_Model = Customer

    # Products
    product_json_file = 'products_data.json'
    product_Model = Product

    # Order
    order_json_file = 'orders_data.json'
    order_Model = Order

    load_to_database(json_file=customer_json_file, Model=customer_Model)
    load_to_database(json_file=product_json_file, Model=product_Model)
    load_to_database(json_file=order_json_file, Model=order_Model)

    pass


if __name__ == '__main__':
    main()
