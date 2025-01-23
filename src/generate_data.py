import json
import random
from datetime import date

from faker import Faker

fake = Faker('en-US')


def generate_customer_data(num_customers: int):

    # Gerando Customers
    customers_data = [
        {
            'customer_id': i,
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'address': fake.address(),
            'city': fake.city(),
            'state': fake.state(),
            'country': fake.country(),
            'join_date': fake.date_between(
                start_date='-5y', end_date=date.today()
            ).isoformat(),
        }
        for i in range(1, num_customers + 1)
    ]

    data_dict = {'customers': customers_data}

    # Salvando em JSONL
    with open('data/customers_data.json', 'w') as f:
        json.dump(data_dict, f, indent=4)

    return customers_data


def generate_products_data(num_products: int):

    # Gerando Products
    products_data = [
        {
            'product_id': i,
            'product_name': fake.word().capitalize(),
            'price': round(random.uniform(10, 1000), 2),
            'stock_quantity': random.randint(10, 500),
        }
        for i in range(1, num_products + 1)
    ]

    data_dict = {'products': products_data}

    with open('data/products_data.json', 'w') as f:
        json.dump(data_dict, f, indent=4)

    return products_data


def generate_orders_data(
    num_orders: int, customers_data: dict, products_data: dict
):

    # Gerando Orders
    orders_data = [
        {
            'order_id': i,
            'customer_id': random.choice(
                [c['customer_id'] for c in customers_data]
            ),
            'product_id': random.choice(
                [p['product_id'] for p in products_data]
            ),
            'order_date': fake.date_between(
                start_date='-2y', end_date=date.today()
            ).isoformat(),
            'quantity': random.randint(1, 10),
        }
        for i in range(1, num_orders + 1)
    ]

    data_dict = {'orders': orders_data}

    with open('data/orders_data.json', 'w') as f:
        json.dump(data_dict, f, indent=4)

    return orders_data


if __name__ == '__main__':
    customers_data = generate_customer_data(num_customers=100)
    products_data = generate_products_data(num_products=1000)
    generate_orders_data(
        num_orders=10000,
        customers_data=customers_data,
        products_data=products_data,
    )
