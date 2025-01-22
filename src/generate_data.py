from faker import Faker
import random
import json
from datetime import date

fake = Faker('en-US')

# Quantidade de dados
num_customers = 100
num_products = 1000
num_orders = 10000

# Gerando Customers
customers_data = [
    {
        "customer_id": i,
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.address(),
        "city": fake.city(),
        "state": fake.state(),
        "country": fake.country(),
        "join_date": fake.date_between(start_date="-5y", end_date=date.today()).isoformat()
    }
    for i in range(1, num_customers + 1)
]

# Gerando Products
products_data = [
    {
        "product_id": i,
        "product_name": fake.word().capitalize(),
        "price": round(random.uniform(10, 1000), 2),
        "stock_quantity": random.randint(10, 500)
    }
    for i in range(1, num_products + 1)
]

# Gerando Orders
orders_data = [
    {
        "order_id": i,
        "customer_id": random.choice([c["customer_id"] for c in customers_data]),
        "product_id": random.choice([p["product_id"] for p in products_data]),
        "order_date": fake.date_between(start_date="-2y", end_date=date.today()).isoformat(),
        "quantity": random.randint(1, 10)
    }
    for i in range(1, num_orders + 1)
]

# Salvando em JSONL
with open("data/customers_data.jsonl", "w") as f:
    for customer in customers_data:
        f.write(json.dumps(customer) + "\n")

with open("data/products_data.jsonl", "w") as f:
    for product in products_data:
        f.write(json.dumps(product) + "\n")

with open("data/orders_data.jsonl", "w") as f:
    for order in orders_data:
        f.write(json.dumps(order) + "\n")
